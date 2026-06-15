# 📁 Структура папки `landings/` — Портфолио JNN Factory

## Организация

Каждый лендинг — отдельная подпапка:

```
landings/
├── index.html          ← Главная страница портфолио (обзор всех работ)
├── README.md           ← Этот файл
├── TOP-20-CLIENTS.md   ← Аудит сайтов конкурентов (Firecrawl)
│
├── atelie-moda/        ← Швейная мастерская
│   ├── index.html
│   ├── README.md
│   └── screenshot.png
│
├── dentistry/          ← Стоматология
│   ├── index.html
│   ├── README.md
│   └── screenshot.png
│
├── fitness/            ← Фитнес / спорт
│   ├── index.html
│   ├── README.md
│   └── screenshot.png
│
├── repair/             ← Ремонт техники
│   ├── index.html
│   ├── README.md
│   └── screenshot.png
│
├── cafe/               ← Кафе / ресторан
│   ├── index.html
│   ├── README.md
│   └── screenshot.png
│
├── parikmaherskaya/    ← Парикмахерская
│   ├── index.html
│   ├── README.md
│   └── screenshot.png
│
├── it-services/        ← IT-услуги
│   ├── index.html
│   ├── README.md
│   └── screenshot.png
│
├── ai-b2b/             ← AI для бизнеса
│   ├── index.html
│   ├── README.md
│   └── screenshot.png
│
├── ai-chat-widget/     ← AI чат-виджет
│   ├── index.html
│   ├── README.md
│   └── screenshot.png
│
├── education/          ← Образование
│   ├── index.html
│   ├── README.md
│   └── screenshot.png
│
├── smart-landing/      ← Умный лендинг
│   ├── index.html
│   ├── README.md
│   └── screenshot.png
│
└── krepkiy-oreshek/    ← Крепкий орешек (пример)
    ├── index.html
    ├── README.md
    └── screenshot.png
```

## Категории лендингов

| Категория | Лендинги | Целевая аудитория |
|-----------|----------|-------------------|
| **Услуги B2C** | dentistry, fitness, repair, cafe, parikmaherskaya | Малый бизнес, салоны, кафе |
| **Производство** | atelie-moda | Швейные мастерские, цеха |
| **IT / SaaS** | it-services, ai-b2b, ai-chat-widget, smart-landing | IT-компании, стартапы |
| **Образование** | education | Курсы, тренинги |

## Масштабирование

При росте количества проектов:

1. **Каждый проект — отдельная подпапка** (не плоский список файлов)
2. **Внутри проекта**: index.html + README.md + screenshot.png
3. **README.md** содержит: описание, стек, ссылку на live demo, отзыв клиента
4. **index.html** на верхнем уровне — автоматически генерируемый каталог
5. **При 100+ проектах** — добавить подпапки по категориям: `landings/services/`, `landings/ecommerce/`, `landings/saas/`

## Связь с IT-Услуги

Папка `landings/` — это **портфолио** (что умеем делать).
Папка `notes/IT-Услуги/` — это **бизнес-процесс** (как продаём и работаем).

Связь:
- `notes/IT-Услуги/Проекты/` — активные проекты клиентов
- `notes/IT-Услуги/Шаблоны/` — шаблоны сообщений и скриптов
- `landings/` — демо-версии для показа клиентам
- Когда проект завершён → копия лендинга в `landings/` + отзыв в `notes/IT-Услуги/Отзывы/`
