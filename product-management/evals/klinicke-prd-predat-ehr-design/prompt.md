---
description: >-
  write-spec: zadání klinické obrazovky (dekurz) patří pluginu ehr-design. Výstup to musí uvést a
  nevydávat se za klinickou specifikaci.
tags: [routing, trigger, cs]
max_turns: 20
timeout_seconds: 420
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: >-
  Asistent upozorní, že PRD klinické obrazovky patří do pluginu ehr-design (skill ehr-prd) z
  marketplace dokturek-team, a nabídne, co může udělat sám.
---

Napiš PRD pro novou obrazovku zápisu dekurzu v kartě pacienta.
