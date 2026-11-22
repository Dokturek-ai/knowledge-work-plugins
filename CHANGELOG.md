# Historie změn

Formát vychází z [Keep a Changelog](https://keepachangelog.com/cs/1.1.0/), verze podle [SemVer](https://semver.org/lang/cs/).

## 2026-11-22 — Review pluginem plugin-development (marketplace 1.1.0)

Všech osm pluginů prošlo review agentem `plugin-reviewer` z pluginu `plugin-development`. Opravené nálezy:

### Změněno

- Sdílený kontext: potvrzení platí i pro akce, o které uživatel požádá, a přebíjí opačný text skillu; plánované běhy jen čtou a navrhují. Nové pravidlo 9: žádné SLA, sliby termínů ani tvrzení o hotové práci. Doplněný Adrian Golian, ceník podle Q-772, zdroje obchodních kanálů, potlačení skupin pod 5, Notion jen ke čtení.
- `sales` 3.1.0: blok pravidel ve všech 11 skillech už neříká „nikdy neodmítni akci“; odeslání, rezervace a zápis do Pipedrive jen po potvrzení. Bez Gong, Outlook, Calendly a Salesforce; `win-loss-review` bez procent; `argument-hint` u 9 skillů.
- `customer-support` 2.1.0: šablony bez SLA a bez „už jsme opravili“, české šablony s vykáním, eskalace na jmenované vlastníky, eRecept a eNeschopenka do `incident-response`.
- `marketing` 2.1.0: bez slev, pobídek a vymyšlených benchmarků; české konvence místo amerických; hlas jen z `DESIGN.md`.
- `product-management` 2.1.0: rozhodnutí jen jako návrh do registru 10; bez facilitace standupů (OpenClaw); issues až po potvrzení.
- `legal` 2.1.0: české právo místo amerického (licence podle 121/2000 Sb., § 2048 a § 2898 OZ); GREEN u NDA je doporučení pro Honzu; žádost subjektu údajů jako předání správci; `vendor-check` kontroluje dalšího zpracovatele podle čl. 28.
- `operations` 2.1.0: zápisy jen po potvrzení; větev pro porušení zabezpečení osobních údajů; brány G01–G10 v `deploy-checklist`; Telegram jen jako dohoda bez termínu.
- `design` 2.1.0: WCAG 2.5.5 (AAA) nahrazeno 2.5.8 (AA); bez hravého tónu.
- `data` 2.1.0: z reálných dat jen agregace bez hodnot identifikátorů; Firebird 3; barvy Doktůrku.

### Odstraněno

- `data/data-context-extractor`: předpokládal datový sklad a balicí skript měl chybu v cestách.

### Přidáno

- Evaly `claude plugin eval` pro osm pluginů ([evals/README.md](evals/README.md)) a workflow `plugin-evals.yml`.
- `scripts/check_repo.py`: kategorie `~~` proti CONNECTORS.md, povinný oddíl Doktůrek specifics, verze v README, sken tajemství, rodných čísel a absolutních cest.

## 2026-11-22 — Obálka a mapa v README (marketplace 1.0.1)

### Přidáno

- Obálka [`assets/cover.png`](assets/cover.png) a mapa marketplace Doktůrku [`assets/map.png`](assets/map.png) ve stylu `DESIGN.md` (logo, Geist, teal), se zdrojovými SVG.
- Odznaky CI v README.

## 2026-11-22 — Personalizace pro Doktůrek (marketplace 1.0.0)

Fork `anthropics/knowledge-work-plugins` je přestavěný na marketplace `dokturek-work` pro práci týmu Doktůrek.ai mimo vývoj.

### Přidáno

- Sdílený kontext [`shared/dokturek-context.md`](shared/dokturek-context.md): firma, tým a kdo rozhoduje, zdroje pravdy, pravidla pro data a potvrzování, hlas značky, předávání pluginům `dokturek-team`. Každý plugin má kopii a každý skill odkaz.
- Oddíl `## Doktůrek specifics` ve všech 49 skillech: DPA s ordinacemi, Pipedrive a ceník, GitHub Issues a týmové sprinty, vlastníci incidentů, ruční dořešení nejasného eReceptu, pravidla `DESIGN.md`, zákaz dat na úrovni pacienta.
- Kontrola [`scripts/check_repo.py`](scripts/check_repo.py) a workflow `Validate Plugins` (`claude plugin validate --strict`).
- Projektové [`.claude/settings.json`](.claude/settings.json) s marketplace `dokturek-work`.

### Změněno

- Všechny README a `CONNECTORS.md` jsou česky a odpovídají skutečným skillům.
- Konektory: jen Slack a Notion (archiv jen ke čtení) s ověřenými adresami. Prázdné adresy Gmail, Google Kalendáře, Snowflake a Databricks a zastaralý Atlassian `v1` jsou odstraněné.
- `operations` 2.0.0 převzal z `engineering` skilly `incident-response`, `deploy-checklist` a `tech-debt`. Incident už nepředpokládá PagerDuty a zprávy do kanálu jen navrhuje.
- `sales` 3.0.0: z 36 skillů zůstává 11 pro prodej ordinacím; zápisy do CRM jsou checklist pro Pipedrive.
- `product-management`, `marketing`, `customer-support`, `legal`, `design`, `data` 2.0.0: zúžené a přizpůsobené.

### Odstraněno

- Pluginy, které duplikují `dokturek-team` nebo OpenClaw: `engineering`, `cowork-plugin-management`, `productivity`, `enterprise-search`.
- Pluginy mimo obor nebo bez vlastníka v týmu: `finance`, `human-resources`, `small-business`, `bio-research`, `pdf-viewer` a pět partnerských pluginů.
- Duplicitní nebo nerelevantní skilly v ponechaných pluginech: `content-creation`, `performance-report`, `sql-queries`, `data-visualization`, `competitive-brief` (marketing i produkt), `metrics-review`, `runbook`, `status-report`, `vendor-review`, `risk-assessment`, `compliance-tracking`, `process-optimization`, `signature-request`, `brief`, `meeting-briefing`, příkaz `brainstorm`, pět skillů `design` pokrytých `ehr-design` a 25 skillů `sales` vázaných na CRM.
- Všech 101 externích položek katalogu.
- Workflow navázané na infrastrukturu Anthropicu: noční aktualizace SHA, policy sken, revert a automatické zavírání PR.
