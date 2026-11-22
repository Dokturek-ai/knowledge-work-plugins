# Produkt (`product-management`)

Pomáhá s produktovou prací mimo návrh klinických obrazovek: specifikace, roadmapa, týdenní sprinty v GitHub Issues, reporty pro tým a vedení a vyhodnocení rozhovorů s lékaři.

Pro koho: Honza (rozsah a priority) a Petr (technika, registr rozhodnutí).

## Instalace v Claude Code

```text
/plugin marketplace add Dokturek-ai/knowledge-work-plugins
/plugin install product-management@dokturek-work
```

V Claude Desktop a Cowork přidejte marketplace v **Customize → Plugins**.

## Skilly

Skill se spustí sám podle zadání, nebo ho zavolejte jménem, například `/product-management:write-spec`.

| Skill | K čemu slouží |
| --- | --- |
| `write-spec` | Specifikace neklinické funkce (onboarding ordinace, předplatné, migrace, web); klinické obrazovky předá `ehr-design`. |
| `roadmap-update` | Návrh změny `01-produkt/produktova-roadmapa.md` jako diff. |
| `sprint-planning` | Týdenní sprint jako milník v GitHub Issues `dokturek-docs`; issues zakládá až po potvrzení. |
| `stakeholder-update` | Report pro tým, vedení, poradce nebo pilotní ordinaci ze `STAV.md` a registru. |
| `synthesize-research` | Vyhodnocení rozhovorů s lékaři a zpětné vazby z pilotu. |
| `product-brainstorming` | Hledání nápadů vůči rozsahu prvního dne a hlavnímu sdělení. |

## Jak plugin pracuje

- Každý skill nejdřív načte [kontext Doktůrku](shared/dokturek-context.md): tým, zdroje pravdy, pravidla pro data a potvrzování, hlas značky a předávání jiným pluginům.
- Odpovídá česky. Fakta o Doktůrku cituje z `dokturek-docs` a značí [Z], [P], [N].
- Rozhodnutí skill nikdy nepřijímá. Navrhne položku R nebo Q do registru `10-rozhodnuti-a-otevrene-otazky.md` s vlastníkem.

## Konektory

Viz [CONNECTORS.md](CONNECTORS.md).

## Původ

Plugin vychází z pluginu `product-management` v [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (Apache 2.0). Změny pro Doktůrek popisuje [CHANGELOG](https://github.com/Dokturek-ai/knowledge-work-plugins/blob/main/CHANGELOG.md).
