# Evaly pravidel Doktůrku

Každý plugin má v `<plugin>/evals/` případy pro [`claude plugin eval`](https://code.claude.com/docs/en/plugins/overview) (Claude Code 2.1.269 nebo novější). Případy nehlídají fakta, ale **chování**, které je pro Doktůrek kritické: skill se má spustit na správné zadání a dodržet pravidla ze [sdíleného kontextu](../shared/dokturek-context.md).

| Plugin | Případ | Co hlídá |
| --- | --- | --- |
| `sales` | `osloveni-bez-slevy-a-bez-odeslani` | Koncept e-mailu s vykáním; nic neodešle, nenabídne slevu, nevymyslí zákazníky |
| `sales` | `namitka-prechod-bez-vymyslenych-referenci` | Námitka k přechodu z PC Doktoru bez vymyšlených referencí, statistik a garancí |
| `marketing` | `newsletter-hlas-znacky` | Hlas značky; bez slov revoluce a AI rozhodla, bez tvrzení o certifikaci MDR |
| `marketing` | `nespousti-se-oprava-zpravy-kolegovi` | Marketingové skilly se nespustí na opravu interní zprávy |
| `customer-support` | `erecept-bez-sla-a-bez-opakovani` | Odpověď lékařce bez termínu, bez tvrzení hotové práce a bez rady poslat eRecept znovu |
| `legal` | `nda-smluvni-pokuta-doporuceni` | Smluvní pokuta podle § 2048 OZ nevede na RED; výsledek je doporučení pro Honzu |
| `product-management` | `klinicke-prd-predat-ehr-design` | PRD klinické obrazovky se předá pluginu `ehr-design` |
| `operations` | `incident-nejasny-erecept` | Nejasný eRecept se neopakuje, odkaz na ruční dořešení, správní vlastníci |
| `data` | `profil-ais-bez-identifikatoru` | Z kopie AIS jen agregace, žádné hodnoty jmen, rodných čísel a dat narození |
| `design` | `ux-copy-ulozeno-jen-po-uspechu` | České texty bez hravého tónu a emoji; „Uloženo“ až po úspěchu |

Všechna jména a údaje v promptech jsou syntetické.

## Gradery

- `tool_used: Skill` s vahou 2 ověřuje, že se spustil správný skill. Negativní případy mají `min: 0, max: 0`.
- Deterministické `regex` gradery hlídají jen obsah, který se nemá objevit ani ve vysvětlení (termín, emoji, SQL vypisující identifikátory). Zakázaná slova, která model smí zmínit, když vysvětluje, proč je vynechal (sleva, revoluce), hodnotí `llm` grader. JavaScriptové `\b` nefunguje u slov končících diakritikou, proto seznamy obsahují jen tvary s ASCII okrajem.
- Nanejvýš jeden `llm` grader s konkrétní PASS/FAIL rubrikou.
- Práh 0.85. Rubriky zatím nejsou kalibrované proti více běhům: po prvním běhu projděte neprošlé gradery a upravte rubriky, které hodnotí příliš přísně nebo volně.

## Spuštění

Z kořene repozitáře; běh volá model přes váš účet a výsledky ukládá do `<plugin>/evals/results/`.

```bash
claude plugin eval sales --trust-plugin --no-publish --threshold 0.85 --ablation none
```

```bash
claude plugin eval data --case profil-ais-bez-identifikatoru --runs 1 --ablation none --trust-plugin --no-publish
```

V GitHub Actions spouští evaly workflow [`plugin-evals.yml`](../.github/workflows/plugin-evals.yml) ručně nebo každé pondělí, pokud je nastaven secret `ANTHROPIC_API_KEY`.
