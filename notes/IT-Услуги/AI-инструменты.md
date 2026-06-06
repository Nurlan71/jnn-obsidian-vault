# AI-инструменты для производства лендингов

> Установлены и настроены: 06.06.2026
> VPS: root@173.249.56.248

## Установленные инструменты

### 🔥 Firecrawl
- **Версия:** v4.28.2 (Python SDK)
- **Путь:** `/opt/tools-venv`
- **API Key:** `fc-723bc55ec5b74eeb9954d1d837482286`
- **Аккаунт:** nurlan710201@gmail.com (через Google)
- **Тариф:** Free — 1,000 credits/мес (~1000 страниц)
- **Проверено:** ✅ Scrape atelie-plus.ru — OK, ✅ Search — OK

**Тарифы Firecrawl:**
| План | Цена | Страниц | Concurrent |
|------|------|---------|------------|
| Free | $0 | 1,000 | 2 |
| Starter | $19/мес | 5,000 | 5 |
| Standard | $99/мес | 100,000 | 50 |
| Growth | $399/мес | 500,000 | 100 |

**Python API:**
```python
from firecrawl import Firecrawl
app = Firecrawl(api_key="fc-723bc55ec5b74eeb9954d1d837482286")

# Scrape сайта
result = app.scrape('https://example.com')
print(result.markdown)        # Markdown контент
print(result.metadata.title) # Заголовок

# Поиск
search = app.search('запрос', limit=5)
for item in search.web:
    print(item.url, item.title)

# Карта сайта
mapping = app.map('https://example.com')
for url in mapping.data:
    print(url)
```

### 🤖 Aider
- **Версия:** v0.86.2
- **Путь:** `/root/.local/bin/aider`
- **Назначение:** AI pair programming в терминале
- **Использование:** правки кода лендингов словами, авто git commit
- **Поддерживает:** Claude, GPT, DeepSeek, локальные модели

```bash
export PATH=/root/.local/bin:/opt/tools-venv/bin:$PATH
cd /папка/с/лендингом
aider --model sonnet --api-key anthropic=KEY
```

### 🧬 ai-website-cloner-template
- **Версия:** v0.3.1
- **Путь:** `/opt/data/ai-website-cloner`
- **Назначение:** Клонирует любой сайт в чистый Next.js код
- **Технологии:** Next.js 16, React 19, TypeScript, Tailwind CSS v4, shadcn/ui
- **Требует:** Claude Code (рекомендуется), Cursor, Codex, Aider
- **npm install:** выполнен

```bash
cd /opt/data/ai-website-cloner
/clone-website https://target-site.com
```

### 🕷️ ScraperAI
- **Версия:** v0.0.2
- **Путь:** `/opt/tools-venv`
- **Назначение:** AI-powered web scraping, автоопределение структуры
- **Бесплатный self-hosted** аналог Firecrawl для простых задач

```bash
export PATH=/opt/tools-venv/bin:$PATH
scraperai --url https://example.com
```

## Production Pipeline

```
1. Firecrawl → собираем контент с сайтов конкурентов
2. ai-website-cloner → клонируем структуру и дизайн
3. Aider → адаптируем тексты, цвета, цены под клиента
4. Surge.sh → деплоим за 2 минуты
```

**Результат:** лендинг за 1-2 часа вместо 2-3 дней.

## Что НЕ использовать
- **GPT-Engineer** — заархивирован (апрель 2026)
- **Astra AI / ai-website-builder** — слишком слабые

## Ссылки
- [[IT-Услуги]] — основная страница направления
- [[Клиенты]] — база клиентов
- [[Проекты]] — текущие проекты
- `/opt/data/landings/TOOLS-INSTALLED.md` — техническая документация на VPS
