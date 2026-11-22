# Marketing (`marketing`)

Pomáhá s kampaněmi a texty pro lékaře: newsletter, e-mailové sekvence, texty na web a sociální sítě, kontrola tónu značky a SEO.

Pro koho: Filip (obchod a marketing).

## Instalace v Claude Code

```text
/plugin marketplace add Dokturek-ai/knowledge-work-plugins
/plugin install marketing@dokturek-work
```

V Claude Desktop a Cowork přidejte marketplace v **Customize → Plugins**.

## Skilly

Skill se spustí sám podle zadání, nebo ho zavolejte jménem, například `/marketing:campaign-plan`.

| Skill | K čemu slouží |
| --- | --- |
| `campaign-plan` | Plán kampaně: cíl, publikum, sdělení, kanály, kalendář (Meta reklamy, newsletter). |
| `draft-content` | Návrh textu pro web, newsletter, sociální sítě nebo případovou studii. |
| `email-sequence` | Sekvence e-mailů pro lékaře s jednou výzvou k akci v každém e-mailu. |
| `brand-review` | Kontrola textu proti hlasu a slovníku Doktůrku z `DESIGN.md`. |
| `seo-audit` | SEO audit `dokturek.ai` a `get.dokturek.ai` pro české hledané výrazy. |

## Jak plugin pracuje

- Každý skill nejdřív načte [kontext Doktůrku](shared/dokturek-context.md): tým, zdroje pravdy, pravidla pro data a potvrzování, hlas značky a předávání jiným pluginům.
- Odpovídá česky. Fakta o Doktůrku cituje z `dokturek-docs` a značí [Z], [P], [N].
- Klinická tvrzení v textech potvrzuje Anna. Tvrzení o MDR, certifikaci nebo přesnosti AI skill nepřipustí, pokud je dokumenty nedokládají.

## Konektory

Viz [CONNECTORS.md](CONNECTORS.md).

## Původ

Plugin vychází z pluginu `marketing` v [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (Apache 2.0). Změny pro Doktůrek popisuje [CHANGELOG](https://github.com/Dokturek-ai/knowledge-work-plugins/blob/main/CHANGELOG.md).
