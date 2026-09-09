#!/usr/bin/env python3
"""
Проверка новых моделей из ClawLabsAI/free-ai-models (JSON).
Скачивает https://raw.githubusercontent.com/ClawLabsAI/free-ai-models/main/data/models.json,
фильтрует: free, 1M контекст, мультимодальные, сравнивает с нашей моделью-фоллбэком.
Выводит только новые или интересные изменения.
"""
import urllib.request, json, sys, os
from collections import Counter

JSON_URL = "https://raw.githubusercontent.com/ClawLabsAI/free-ai-models/main/data/models.json"
OUR_MODEL = "thinkingmachines/inkling:free"

def main():
    try:
        with urllib.request.urlopen(JSON_URL, timeout=30) as resp:
            data = json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"❌ Ошибка загрузки JSON: {e}")
        sys.exit(1)

    # Ожидаемый формат: список моделей или объект с ключом models
    models = data.get("models", []) if isinstance(data, dict) else data
    print(f"=== Free AI Models Report (источник: {JSON_URL}) ===")
    print(f"Моделей в списке: {len(models)}")
    print()

    # Фильтруем интересное для нас: 1M+ контекст, мультимодальное, free
    interesting = []
    for m in models:
        if not isinstance(m, dict):
            continue
        context_str = str(m.get("context_window", m.get("context", "0")))
        # Извлекаем число из "1M tokens" или "1,000,000 tokens"
        context_num = 0
        if "1m" in context_str.lower() or "1,000,000" in context_str or "1048576" in context_str or "1000000" in context_str:
            context_num = 1_000_000
        elif "262k" in context_str.lower() or "262000" in context_str or "262144" in context_str:
            context_num = 262_144
        elif "512k" in context_str.lower() or "524288" in context_str:
            context_num = 524_288
        else:
            try:
                context_num = int(context_str.replace(",", "").replace(" ", "").replace("tokens", ""))
            except:
                context_num = 0

        # Фильтр: free + 1M контекст + мультимодальное
        if context_num >= 1_000_000:
            modalities = str(m.get("modalities", m.get("modality", ""))).lower()
            is_multimodal = any(x in modalities for x in ["vision", "image", "video", "audio"])
            id_str = str(m.get("id", m.get("model", "")))
            provider = str(m.get("provider", m.get("maker", "?")))
            rate_limit = str(m.get("rate_limit", m.get("limit", "unknown")))
            name = str(m.get("name", m.get("model_name", id_str)))

            interesting.append({
                "id": id_str,
                "name": name,
                "provider": provider,
                "context": context_str,
                "multimodal": is_multimodal,
                "limit": rate_limit,
            })

    # Сортируем: сначала наша модель (если есть), затем остальные
    def sort_key(x):
        return (0 if OUR_MODEL in x["id"] else 1, x["provider"], x["name"])
    interesting.sort(key=sort_key)

    if not interesting:
        print("Ни одна модель с 1M контекстом не найдена в JSON.")
        return

    print(f"Найдено моделей с 1M+ контекстом: {len(interesting)}\n")
    # Показываем все, но выделяем нашу
    for item in interesting:
        is_our = OUR_MODEL in item["id"]
        marker = "← НАШ ФОЛЛБЭК" if is_our else ""
        multimodal_str = "✅ multimodal" if item["multimodal"] else "❌ text-only"
        print(f"  {item['provider']:20} | {item['name']:35} | {item['context']:>10} | {multimodal_str} | limit:{item['limit']}{(' ' + marker) if marker else ''}")
        print(f"  ID: {item['id']}")

    # Проверяем новые или отличающиеся от нашей
    others = [i for i in interesting if OUR_MODEL not in i["id"]]
    print(f"\n=== Альтернативы нашему фоллбэку ({OUR_MODEL}) ===")
    for item in others[:8]:  # Первые 8 альтернатив
        multimodal_str = "multimodal" if item["multimodal"] else "text-only"
        print(f"  • {item['provider']}/{item['id'].split('/')[-1].replace(':free','')} — {multimodal_str}, {item['context']}, limit:{item['limit']}")

    # Выводим рекомендацию в формате для Telegram
    best_alternatives = others[:3]
    if best_alternatives:
        print(f"\n=== Рекомендация ({len(best_alternatives)} альтернатив) ===")
        for i, item in enumerate(best_alternatives, 1):
            print(f"{i}. {item['id']} — {item['multimodal'] and 'multimodal' or 'text'}, контекст {item['context']}, {item['provider']}")

if __name__ == "__main__":
    main()
