# Přispívání do marketplace `dokturek-work`

## Kam změna patří

- Skill pro práci mimo vývoj (produkt, obchod, marketing, podpora, právo, provoz, data) patří sem.
- Skill pro vývoj EHR, FHIR, Medplum, CDS, MDR, vykazování nebo státní služby patří do [`plugin-marketplace-healthcare-dev`](https://github.com/Dokturek-ai/plugin-marketplace-healthcare-dev).
- Nástroj s přístupem k datům patří do [`developer-toolkit`](https://github.com/Dokturek-ai/developer-toolkit) s vlastním `RISK.md`.
- Opakující se týmový tok ve Slacku (standup, zápisy, připomínky) patří do OpenClaw.

Před přidáním skillu ověřte, že stejný úkol už neřeší jiný plugin v některém z těchto míst.

## Přidejte nebo upravte skill

1. Skill uložte do `<plugin>/skills/<název>/SKILL.md`. Název adresáře musí odpovídat poli `name` ve frontmatteru.
2. Popis (`description`) pište anglicky, nejvýše 1 024 znaků, a uveďte, kdy se má skill spustit. Pole `when_to_use` nepoužívejte: claude.ai ho odmítne.
3. Hned za frontmatter vložte odkaz na sdílený kontext:

   ```markdown
   > **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: ...
   ```

4. Konkrétní pravidla pro Doktůrek uveďte v oddílu `## Doktůrek specifics`. Fakta odkazujte na soubory v `dokturek-docs`; nevymýšlejte je.
5. Každou akci, která něco odesílá nebo zapisuje, podmiňte potvrzením uživatele s přesným příjemcem a obsahem.
6. Doplňte řádek do tabulky skillů v `README.md` pluginu. CI ověří, že tabulka odpovídá adresáři `skills/`.

## Sdílený kontext

Kanonická verze je [`shared/dokturek-context.md`](shared/dokturek-context.md). Plugin se instaluje samostatně, proto má každý plugin vlastní kopii v `<plugin>/shared/`. Po úpravě kanonické verze kopie obnovte:

```bash
for d in */.claude-plugin; do cp shared/dokturek-context.md "$(dirname "$d")/shared/"; done
```

## Konektory

1. Kategorie v textu skillu pište obecně se znaky `~~` (například `~~chat`).
2. Server přidejte do `<plugin>/.mcp.json` jen s ověřenou adresou `https://`. Prázdné adresy a nepřipnuté balíčky `npx` CI odmítne.
3. Kategorii a nástroj zapište do `CONNECTORS.md` pluginu.

Pro Pipedrive, GitHub a Google Workspace plugin konektor nepřibaluje: GitHub používejte přes `gh` v Claude Code nebo přes konektor v claude.ai, Google přes vestavěné konektory claude.ai, Pipedrive přes export nebo konektor, který si připojí uživatel.

## Ověřte změnu

Z kořene repozitáře:

```bash
python3 -m pip install pyyaml
python3 scripts/check_repo.py
claude plugin validate . --strict
```

V Claude Code ověřte plugin přes `/plugin list` a spusťte jeden skill z jeho README.

## Připravte verzi

1. Zvyšte verzi pluginu v `<plugin>/.claude-plugin/plugin.json` a v tabulce v kořenovém [README](README.md#pluginy).
2. Zvyšte verzi marketplace v `.claude-plugin/marketplace.json`.
3. Zapište změnu a důvod do [CHANGELOG](CHANGELOG.md).

## Pull request

- Zprávy commitů podle Conventional Commits, například `feat(sales): skill pro předobjednávky`.
- V popisu PR uveďte výsledek `scripts/check_repo.py` a `claude plugin validate`.
