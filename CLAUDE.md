# CLAUDE.md

Repozitář obsahuje marketplace `dokturek-work`: pluginy pro práci týmu Doktůrek.ai mimo vývoj. Přehled je v [`README.md`](README.md), pravidla přispívání v [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Pravidla pro práci v repozitáři

- Kontext Doktůrku upravujte jen v [`shared/dokturek-context.md`](shared/dokturek-context.md) a pak obnovte kopie v pluginech (příkaz v CONTRIBUTING).
- Fakta o Doktůrku berte z `Dokturek-ai/dokturek-docs` (`STAV.md`, `SLOVNIK.md`, `10-rozhodnuti-a-otevrene-otazky.md`) a odkazujte je. Nevymýšlejte jména, termíny, ceny ani stav smluv.
- Nepřidávejte skill, který už řeší `plugin-marketplace-healthcare-dev`, `developer-toolkit` nebo OpenClaw.
- README, CONNECTORS a CHANGELOG pište česky s vykáním. Texty skillů a jejich `description` pište anglicky.
- Repozitář je veřejný: žádná tajemství, data pacientů, finance, investoři ani obsah smluv.

## Kontrola před commitem

```bash
python3 scripts/check_repo.py
claude plugin validate . --strict
```

Zprávy commitů podle Conventional Commits.
