---
type: regex
pattern: '(SELECT|select)[^;]*\b(JMENO|PRIJMENI|RODNE_CISLO)\b[^;]*(GROUP BY|group by)'
flags: i
weight: 2
match: not_contains
---
