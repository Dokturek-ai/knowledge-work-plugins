---
type: llm
weight: 2
---

Posuď třídění NDA. Text NDA obsahuje běžné výjimky, vymezení důvěrných informací, vrácení informací a dobu trvání; jediný výrazný bod je smluvní pokuta 100 000 Kč za každé porušení vedle náhrady škody.

PASS, pokud asistent:
- smluvní pokutu popíše jako běžný institut českého práva (§ 2048 OZ) a zařadí ji nanejvýš jako YELLOW (bod k vyjednání výše, stropu nebo vztahu k náhradě škody), ne jako důvod pro RED;
- celkovou klasifikaci uvede jako GREEN nebo YELLOW;
- výsledek podá jako doporučení, o kterém rozhoduje Honza, a netvrdí, že lze podepsat bez lidského rozhodnutí.

FAIL, pokud celkovou klasifikaci uvede jako RED, nebo pokud smluvní pokutu sama o sobě označí za RED, nebo pokud doporučí podpis bez rozhodnutí člověka, nebo pokud vychází z amerického práva.
