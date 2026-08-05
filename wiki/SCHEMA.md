---
name: jnn-wiki
description: "База знаний JNN Factory — сжатые конспекты договоров, клиентов, поставщиков, технологий"
version: 1.0.0
---

# Wiki Schema

## Domain
JNN Factory — швейное производство + IT-услуги (Кыргызстан). Заказы, клиенты, поставщики ткани/фурнитуры, технологии пошива, регламенты.

## Conventions
- File names: lowercase-kebab-case.md
- Every page has YAML frontmatter
- Use [[wikilinks]] between pages (min 2 outbound links)
- Every new page added to index.md
- Every action logged in log.md

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query
tags: [company, technology, material, client, supplier, contract]
sources: [raw/articles/source.md]
---
```

## Tag Taxonomy
- Entities: company, person, client, supplier, partner, employee
- Production: material, fabric, sewing, pattern, equipment
- Business: contract, order, finance, delivery
- Meta: comparison, process, regulation

## Page Thresholds
- Create page when entity/concept appears in 2+ sources
- Don't create pages for passing mentions
- Split pages over 200 lines
