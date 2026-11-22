# Konektory: Produkt

Skilly odkazují na nástroje obecnou kategorií se znaky `~~` (například `~~chat`). Tabulka uvádí, čím je kategorie v Doktůrku obsazená a jestli plugin konektor přibaluje v `.mcp.json`.

| Kategorie | Nástroj v Doktůrku | Server v `.mcp.json` | Poznámka |
| --- | --- | --- | --- |
| `~~chat` | Slack | slack |  |
| `~~project tracker` | GitHub Issues v `Dokturek-ai/dokturek-docs` | — | V Claude Code přes `gh`, v claude.ai přes konektor GitHub. |
| `~~knowledge base` | `dokturek-docs`, Notion (archiv) | notion | Notion je archiv jen ke čtení. |
| `~~meeting transcription` | přepisy porad | — | Zápisy z porad připravuje OpenClaw; vložte přepis přímo. |
| `~~design, ~~product analytics, ~~user feedback` | — | — | Nástroje dokumentace neuvádí. |

Kategorie bez nástroje skill obejde: pracuje s vloženým textem nebo nahraným souborem a řekne, co nepoužil. Přidání konektoru popisuje [CONTRIBUTING](https://github.com/Dokturek-ai/knowledge-work-plugins/blob/main/CONTRIBUTING.md#konektory).
