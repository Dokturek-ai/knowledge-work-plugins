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
| `draft-content` | Návrh textu pro veřejné kanály: web, newsletter, sociální sítě, tiskové zprávy. Podklady pro jednu ordinaci připraví `sales:create-an-asset`. |
| `email-sequence` | Sekvence e-mailů pro seznam nebo segment lékařů s jednou výzvou k akci v každém e-mailu. Zprávu jedné ordinaci napíše `sales:draft-outreach`. |
| `brand-review` | Kontrola marketingových a obchodních textů proti hlasu a slovníku Doktůrku z `DESIGN.md` a českým pravidlům psaní. Texty v aplikaci kontroluje `design:ux-copy`. |
| `seo-audit` | SEO audit `dokturek.ai` a `get.dokturek.ai` pro české hledané výrazy. |

## Jak plugin pracuje

- Každý skill nejdřív načte [kontext Doktůrku](shared/dokturek-context.md): tým, zdroje pravdy, pravidla pro data a potvrzování, hlas značky a předávání jiným pluginům.
- Odpovídá česky. Fakta o Doktůrku cituje z `dokturek-docs` a značí [Z], [P], [N].
- Texty nenabízejí slevy, pobídky ani časově omezené nabídky; cenu uvádějí jen odkazem na `dokturek.ai/cenik`. Reference a případové studie ordinací před 1. 1. 2027 skill nevymýšlí.
- Klinická tvrzení v textech potvrzuje Anna. Tvrzení o MDR, certifikaci nebo přesnosti AI skill nepřipustí, pokud je dokumenty nedokládají.

## Konektory

Viz [CONNECTORS.md](CONNECTORS.md).

## Původ

Plugin vychází z pluginu `marketing` v [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (Apache 2.0). Změny pro Doktůrek popisuje [CHANGELOG](https://github.com/Dokturek-ai/knowledge-work-plugins/blob/main/CHANGELOG.md).
