# Konektory: Obchod

Skilly odkazují na nástroje obecnou kategorií se znaky `~~` (například `~~chat`). Tabulka uvádí, čím je kategorie v Doktůrku obsazená a jestli plugin konektor přibaluje v `.mcp.json`.

| Kategorie | Nástroj v Doktůrku | Server v `.mcp.json` | Poznámka |
| --- | --- | --- | --- |
| `~~chat` | Slack | slack | Kanál `#pr-and-outreach` dostává nové leady z `get.dokturek.ai`. |
| `~~crm` | Pipedrive | — | Konektor není součástí pluginu. Pracujte s exportem z Pipedrive, nebo připojte konektor, který používá váš účet. Změny skill připraví jako checklist. |
| `~~knowledge base` | Notion (archiv), `dokturek-docs` | notion | Notion je archiv jen ke čtení; platný stav je v `dokturek-docs`. |
| `~~email, ~~calendar` | Gmail a Google Kalendář | — | Vestavěné konektory claude.ai, pokud je máte zapnuté. Bez nich skill připraví text ke zkopírování. |

Kategorie bez nástroje skill obejde: pracuje s vloženým textem nebo nahraným souborem a řekne, co nepoužil. Přidání konektoru popisuje [CONTRIBUTING](https://github.com/Dokturek-ai/knowledge-work-plugins/blob/main/CONTRIBUTING.md#konektory).
