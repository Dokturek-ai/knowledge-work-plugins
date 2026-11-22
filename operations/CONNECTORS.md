# Konektory: Provoz

Skilly odkazují na nástroje obecnou kategorií se znaky `~~` (například `~~chat`). Tabulka uvádí, čím je kategorie v Doktůrku obsazená a jestli plugin konektor přibaluje v `.mcp.json`.

| Kategorie | Nástroj v Doktůrku | Server v `.mcp.json` | Poznámka |
| --- | --- | --- | --- |
| `~~chat` | Slack | slack | Upozornění na selhání nasazení zatím neběží: tým se jen dohodl (úkol bez termínu, [`46-porada-retro-a-planning-2026-11-13.md`](https://github.com/Dokturek-ai/dokturek-docs/blob/main/46-porada-retro-a-planning-2026-11-13.md)), že mají chodit do Telegramu. |
| `~~project tracker` | GitHub Issues | — | V Claude Code přes `gh`, v claude.ai přes konektor GitHub. |
| `~~knowledge base` | `dokturek-docs`, Notion (archiv) | notion |  |
| `~~source control, ~~CI` | GitHub, GitHub Actions | — |  |
| `~~monitoring, ~~ITSM, ~~calendar` | — | — | Nástroj pro monitoring ani ITSM dokumentace neuvádí. |

Kategorie bez nástroje skill obejde: pracuje s vloženým textem nebo nahraným souborem a řekne, co nepoužil. Přidání konektoru popisuje [CONTRIBUTING](https://github.com/Dokturek-ai/knowledge-work-plugins/blob/main/CONTRIBUTING.md#konektory).
