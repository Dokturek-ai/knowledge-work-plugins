# Design (`design`)

Doplňuje plugin `ehr-design` o dvě věci, které tam nejsou: české texty rozhraní a kontrolu přístupnosti podle pravidel `DESIGN.md`.

Pro koho: Jan Uchytil (UI/UX) a frontend.

## Instalace v Claude Code

```text
/plugin marketplace add Dokturek-ai/knowledge-work-plugins
/plugin install design@dokturek-work
```

V Claude Desktop a Cowork přidejte marketplace v **Customize → Plugins**.

## Skilly

Skill se spustí sám podle zadání, nebo ho zavolejte jménem, například `/design:ux-copy`.

| Skill | K čemu slouží |
| --- | --- |
| `ux-copy` | Texty rozhraní v češtině: tlačítka, chyby, prázdné stavy, potvrzení. |
| `accessibility-review` | Audit přístupnosti WCAG 2.1 AA podle pravidel kontrastu a fokusu z `DESIGN.md`. |

## Jak plugin pracuje

- Každý skill nejdřív načte [kontext Doktůrku](shared/dokturek-context.md): tým, zdroje pravdy, pravidla pro data a potvrzování, hlas značky a předávání jiným pluginům.
- Odpovídá česky. Fakta o Doktůrku cituje z `dokturek-docs` a značí [Z], [P], [N].
- Klinické obrazovky a human factors posuzuje plugin `ehr-design` (`ehr-ux-reference`).

## Konektory

Viz [CONNECTORS.md](CONNECTORS.md).

## Původ

Plugin vychází z pluginu `design` v [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (Apache 2.0). Změny pro Doktůrek popisuje [CHANGELOG](https://github.com/Dokturek-ai/knowledge-work-plugins/blob/main/CHANGELOG.md).
