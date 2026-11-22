# Data (`data`)

Pomáhá s analýzou dat: SQL, průzkum datové sady, statistika, grafy a dashboardy. Typické použití je vyhodnocení pilotu (čas na návštěvu před a po) a práce se schématem a agregacemi z kopie databáze AIS.

Pro koho: kdokoli z týmu, kdo vyhodnocuje pilot nebo datové podklady.

## Instalace v Claude Code

```text
/plugin marketplace add Dokturek-ai/knowledge-work-plugins
/plugin install data@dokturek-work
```

V Claude Desktop a Cowork přidejte marketplace v **Customize → Plugins**.

## Skilly

Skill se spustí sám podle zadání, nebo ho zavolejte jménem, například `/data:analyze`.

| Skill | K čemu slouží |
| --- | --- |
| `analyze` | Odpověď na datovou otázku od rychlého dotazu po celou analýzu. |
| `explore-data` | Profil datové sady; u kopie AIS jen schéma a agregace. |
| `write-query` | SQL pro PostgreSQL (Medplum) nebo Firebird 3 (kopie AIS), bez řádků s daty pacientů. |
| `statistical-analysis` | Statistika pro malé vzorky z pilotu s nejistotou místo tvrzení o významnosti. |
| `create-viz` | Graf v barvách Doktůrku. |
| `build-dashboard` | Interaktivní HTML dashboard se syntetickými nebo agregovanými daty. |
| `validate-data` | Kontrola analýzy před sdílením, včetně ochrany malých skupin. |

## Jak plugin pracuje

- Každý skill nejdřív načte [kontext Doktůrku](shared/dokturek-context.md): tým, zdroje pravdy, pravidla pro data a potvrzování, hlas značky a předávání jiným pluginům.
- Odpovídá česky. Fakta o Doktůrku cituje z `dokturek-docs` a značí [Z], [P], [N].
- Žádná data na úrovni pacienta. Jen syntetická data, agregace nebo skutečně anonymizované exporty.

## Konektory

Viz [CONNECTORS.md](CONNECTORS.md).

## Původ

Plugin vychází z pluginu `data` v [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (Apache 2.0). Změny pro Doktůrek popisuje [CHANGELOG](https://github.com/Dokturek-ai/knowledge-work-plugins/blob/main/CHANGELOG.md).
