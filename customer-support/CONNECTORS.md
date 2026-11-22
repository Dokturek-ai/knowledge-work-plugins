# Konektory: Podpora

Skilly odkazují na nástroje obecnou kategorií se znaky `~~` (například `~~chat`). Tabulka uvádí, čím je kategorie v Doktůrku obsazená a jestli plugin konektor přibaluje v `.mcp.json`.

| Kategorie | Nástroj v Doktůrku | Server v `.mcp.json` | Poznámka |
| --- | --- | --- | --- |
| `~~chat` | Slack | slack |  |
| `~~knowledge base` | `dokturek-docs`, Notion (archiv) | notion | Znalostní báze pro ordinace zatím není zdokumentovaná; skill se zeptá, kam článek patří. |
| `~~project tracker` | GitHub Issues v `Dokturek-ai/dokturek-docs` | — | V Claude Code přes `gh`, v claude.ai přes konektor GitHub. |
| `~~support platform, ~~CRM` | —, Pipedrive | — | Helpdesk dokumentace neuvádí; vložte text požadavku. Pipedrive konektor není součástí pluginu. |
| `~~email` | Gmail | — | Vestavěný konektor claude.ai, pokud je zapnutý. |

Kategorie bez nástroje skill obejde: pracuje s vloženým textem nebo nahraným souborem a řekne, co nepoužil. Přidání konektoru popisuje [CONTRIBUTING](https://github.com/Dokturek-ai/knowledge-work-plugins/blob/main/CONTRIBUTING.md#konektory).
