# Právo (`legal`)

Připraví podklady k smlouvám s ordinacemi, zpracovatelským smlouvám (DPA), NDA, GDPR a rizikům. Advokát zatím není angažovaný, proto každý výstup končí seznamem bodů pro právníka.

Pro koho: Honza (smlouvy se zákazníky), Petr a poradce Lukáš Peter (GDPR, MDR).

## Instalace v Claude Code

```text
/plugin marketplace add Dokturek-ai/knowledge-work-plugins
/plugin install legal@dokturek-work
```

V Claude Desktop a Cowork přidejte marketplace v **Customize → Plugins**.

## Skilly

Skill se spustí sám podle zadání, nebo ho zavolejte jménem, například `/legal:review-contract`.

| Skill | K čemu slouží |
| --- | --- |
| `review-contract` | Revize smlouvy nebo DPA s ordinací: odchylky, rizika, návrh úprav. |
| `triage-nda` | Rychlé zařazení NDA podle českého práva: GREEN, YELLOW, RED. Výsledek je doporučení pro Honzu, bez něj se nic nepodepisuje. |
| `compliance-check` | GDPR, stav DPA a DPIA, retence dokumentace podle vyhlášky 444/2024 Sb.; MDR předá pluginu `mdr-compliance`. |
| `legal-risk-assessment` | Posouzení právního a smluvního rizika s vlastníkem a návrhem položky do registru. |
| `legal-response` | Textový návrh odpovědi na právní dotaz, například předání žádosti pacienta ordinaci jako správci. Nic neodesílá. |
| `vendor-check` | Kontrola dodavatele jako dalšího zpracovatele podle čl. 28 odst. 2 a 4 GDPR: povolení správce, smlouva se stejnými povinnostmi, zpracování v EU/EHP, uvedení v příloze DPA, SCC při přenosu mimo EHP. |

## Jak plugin pracuje

- Každý skill nejdřív načte [kontext Doktůrku](shared/dokturek-context.md): tým, zdroje pravdy, pravidla pro data a potvrzování, hlas značky a předávání jiným pluginům.
- Odpovídá česky. Fakta o Doktůrku cituje z `dokturek-docs` a značí [Z], [P], [N].
- Výstupy nejsou právní rada. Šablonu DPA skill nikdy nepředstaví jako hotovou k podpisu.

## Konektory

Viz [CONNECTORS.md](CONNECTORS.md).

## Původ

Plugin vychází z pluginu `legal` v [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (Apache 2.0). Změny pro Doktůrek popisuje [CHANGELOG](https://github.com/Dokturek-ai/knowledge-work-plugins/blob/main/CHANGELOG.md).
