# Podpora (`customer-support`)

Pomáhá s požadavky ordinací od začátku placeného provozu: třídění, odpovědi lékařům, eskalace, dohledání odpovědi a články do znalostní báze.

Pro koho: tým, který od 1. 1. 2027 obsluhuje platící ordinace.

## Instalace v Claude Code

```text
/plugin marketplace add Dokturek-ai/knowledge-work-plugins
/plugin install customer-support@dokturek-work
```

V Claude Desktop a Cowork přidejte marketplace v **Customize → Plugins**.

## Skilly

Skill se spustí sám podle zadání, nebo ho zavolejte jménem, například `/customer-support:ticket-triage`.

| Skill | K čemu slouží |
| --- | --- |
| `ticket-triage` | Zařazení a priorita požadavku; selhání eReceptu nebo eNeschopenky jde do řešení incidentu. |
| `draft-response` | Návrh odpovědi lékaři nebo sestře: klidně, konkrétně, s dalším krokem. |
| `customer-escalation` | Eskalace na správného vlastníka (Petr, Kuba, Martin Marhold, Anna, Honza). |
| `customer-research` | Dohledání odpovědi v `dokturek-docs`, GitHub Issues a oficiálních zdrojích SÚKL, ČSSZ, MZČR. |
| `kb-article` | Článek do znalostní báze pro ordinace se syntetickými daty. |

## Jak plugin pracuje

- Každý skill nejdřív načte [kontext Doktůrku](shared/dokturek-context.md): tým, zdroje pravdy, pravidla pro data a potvrzování, hlas značky a předávání jiným pluginům.
- Odpovídá česky. Fakta o Doktůrku cituje z `dokturek-docs` a značí [Z], [P], [N].
- Doktůrek zatím nemá dohodnuté SLA ani úrovně podpory: skill ordinaci neslíbí termín odpovědi ani vyřešení a nenapíše, že je něco zapsáno, eskalováno nebo opraveno, dokud to nepotvrdíte.
- Šablony odpovědí jsou česky, s vykáním a s dalším krokem bez termínu. Eskalace jde na konkrétního vlastníka z týmu, ne na obecný tým.

## Konektory

Viz [CONNECTORS.md](CONNECTORS.md).

## Původ

Plugin vychází z pluginu `customer-support` v [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (Apache 2.0). Změny pro Doktůrek popisuje [CHANGELOG](https://github.com/Dokturek-ai/knowledge-work-plugins/blob/main/CHANGELOG.md).
