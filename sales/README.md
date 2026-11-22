# Obchod (`sales`)

Pomáhá s prodejem Doktůrku ordinacím praktických lékařů: od průzkumu ordinace přes přípravu a shrnutí hovoru až po námitky a přehled obchodů v Pipedrive.

Pro koho: Filip (obchod a marketing) a Honza (zákaznické vztahy a smlouvy).

## Instalace v Claude Code

```text
/plugin marketplace add Dokturek-ai/knowledge-work-plugins
/plugin install sales@dokturek-work
```

V Claude Desktop a Cowork přidejte marketplace v **Customize → Plugins**.

## Skilly

Skill se spustí sám podle zadání, nebo ho zavolejte jménem, například `/sales:account-research`.

| Skill | K čemu slouží |
| --- | --- |
| `account-research` | Průzkum ordinace nebo sítě ordinací z veřejných zdrojů (NRPZS, web ordinace). |
| `call-prep` | Podklad před hovorem nebo ukázkou: kdo přijde, historie, otevřené otázky. |
| `call-summary` | Z poznámek nebo přepisu hovoru připraví návrh follow-up e-mailu, interní shrnutí a změny pro Pipedrive. |
| `draft-outreach` | Návrh oslovení nebo sekvence e-mailů pro ordinaci, jen jako koncept. |
| `handle-objection` | Odpověď na námitku: přechod z dosavadního AIS, státní integrace, ochrana dat, cena. |
| `competitive-intelligence` | Srovnání s PC Doktorem, SmartMedixem, Medistarem a dalšími AIS z doložených zdrojů. |
| `create-an-asset` | One-pager, prezentace nebo leave-behind pro ordinaci podle brandu Doktůrku. |
| `stakeholder-map` | Kdo v ordinaci rozhoduje a kdo ovlivňuje: majitel, další lékaři, sestry. |
| `pipeline-review` | Kontrola obchodů z exportu Pipedrive: stáří, riziko, chybějící další úkol. |
| `win-loss-review` | Co rozhodlo u získaných a ztracených ordinací. |
| `schedule-meeting` | Návrh termínu a pozvánky; rezervace jen po potvrzení. |

## Jak plugin pracuje

- Každý skill nejdřív načte [kontext Doktůrku](shared/dokturek-context.md): tým, zdroje pravdy, pravidla pro data a potvrzování, hlas značky a předávání jiným pluginům.
- Odpovídá česky. Fakta o Doktůrku cituje z `dokturek-docs` a značí [Z], [P], [N].
- Skill nic neodesílá ani nezapisuje sám. Ceny uvádí jen z [ceníku](https://dokturek.ai/cenik) s odkazem a nenabízí slevy.

## Konektory

Viz [CONNECTORS.md](CONNECTORS.md).

## Původ

Plugin vychází z pluginu `sales` v [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (Apache 2.0). Změny pro Doktůrek popisuje [CHANGELOG](https://github.com/Dokturek-ai/knowledge-work-plugins/blob/main/CHANGELOG.md).
