# Provoz (`operations`)

Pomáhá s provozem: incidenty, kontrola před nasazením, změnové požadavky, kapacita týmu, technický dluh a popis procesů. Obsahuje i skilly přesunuté z původního pluginu engineering.

Pro koho: Petr, Kuba (infrastruktura) a Martin Marhold (Keycloak, gov-gateway).

## Instalace v Claude Code

```text
/plugin marketplace add Dokturek-ai/knowledge-work-plugins
/plugin install operations@dokturek-work
```

V Claude Desktop a Cowork přidejte marketplace v **Customize → Plugins**.

## Skilly

Skill se spustí sám podle zadání, nebo ho zavolejte jménem, například `/operations:incident-response`.

| Skill | K čemu slouží |
| --- | --- |
| `incident-response` | Postup při incidentu: vlastníci, komunikace, postmortem; nejasný pokus o eRecept se nikdy slepě neopakuje. |
| `deploy-checklist` | Kontrola před nasazením přes Coolify, včetně release gate Keycloaku a předprodukčního checklistu. |
| `change-request` | Změnový požadavek s dopadem a plánem návratu; schvaluje Petr, klinické chování i Anna. |
| `capacity-plan` | Kapacita týmu podle plánu první ordinace. |
| `tech-debt` | Třídění technického dluhu do existujících registrů. |
| `process-doc` | Popis obchodního nebo provozního procesu (onboarding ordinace, podpora); runbooky předá `technical-documentation`. |

## Jak plugin pracuje

- Každý skill nejdřív načte [kontext Doktůrku](shared/dokturek-context.md): tým, zdroje pravdy, pravidla pro data a potvrzování, hlas značky a předávání jiným pluginům.
- Odpovídá česky. Fakta o Doktůrku cituje z `dokturek-docs` a značí [Z], [P], [N].
- Skill nic nenasazuje, nerestartuje ani nemění Coolify, Medplum, Keycloak nebo gov-gateway.

## Konektory

Viz [CONNECTORS.md](CONNECTORS.md).

## Původ

Plugin vychází z pluginu `operations` v [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (Apache 2.0). Změny pro Doktůrek popisuje [CHANGELOG](https://github.com/Dokturek-ai/knowledge-work-plugins/blob/main/CHANGELOG.md).
