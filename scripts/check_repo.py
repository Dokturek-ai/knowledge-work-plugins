#!/usr/bin/env python3
"""Kontroly repozitáře dokturek-work, které `claude plugin validate` nedělá.

Spuštění z kořene repozitáře: python3 scripts/check_repo.py
Vyžaduje PyYAML (pip install pyyaml).
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CANON = ROOT / "shared" / "dokturek-context.md"
POINTER = "../../shared/dokturek-context.md"
DESC_LIMIT = 1024  # limit pro nahrání skillu do claude.ai
errors = []


def err(path, msg):
    errors.append(f"{path.relative_to(ROOT) if isinstance(path, Path) else path}: {msg}")


def frontmatter(path):
    m = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    return yaml.safe_load(m.group(1)) if m else None


market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
for key in ("$schema", "name", "owner", "version", "plugins"):
    if key not in market:
        err(".claude-plugin/marketplace.json", f"chybí pole {key}")
names = [p["name"] for p in market.get("plugins", [])]
for dup in {n for n in names if names.count(n) > 1}:
    err(".claude-plugin/marketplace.json", f"duplicitní plugin {dup}")

canon = CANON.read_text(encoding="utf-8")
for entry in market.get("plugins", []):
    src = entry.get("source")
    if not isinstance(src, str):
        err(".claude-plugin/marketplace.json", f"{entry['name']}: externí zdroj není povolený")
        continue
    pdir = (ROOT / src).resolve()
    manifest = pdir / ".claude-plugin/plugin.json"
    if not manifest.is_file():
        err(manifest, "chybí")
        continue
    pj = json.loads(manifest.read_text(encoding="utf-8"))
    if pj.get("name") != entry["name"] or pdir.name != entry["name"]:
        err(manifest, "název neodpovídá katalogu nebo adresáři")
    if not isinstance(pj.get("version"), str):
        err(manifest, "chybí verze")

    copy = pdir / "shared/dokturek-context.md"
    if not copy.is_file() or copy.read_text(encoding="utf-8") != canon:
        err(copy, "kopie kontextu se liší od shared/dokturek-context.md")

    skill_dirs = [p for p in (pdir / "skills").iterdir() if p.is_dir()]
    for d in skill_dirs:
        if not (d / "SKILL.md").is_file():
            err(d, "adresář skillu bez SKILL.md")
    skills = sorted(d.name for d in skill_dirs if (d / "SKILL.md").is_file())
    conn_file = pdir / "CONNECTORS.md"
    conn_text = conn_file.read_text(encoding="utf-8") if conn_file.is_file() else ""
    if not conn_text:
        err(conn_file, "chybí")
    declared = set(re.findall(r"~~([a-z][a-z ]*[a-z])", conn_text, re.I))
    declared = {c.lower() for c in declared}
    for s in skills:
        sk = pdir / "skills" / s / "SKILL.md"
        fm = frontmatter(sk)
        if not fm:
            err(sk, "chybí YAML frontmatter")
            continue
        if fm.get("name") != s:
            err(sk, f"name '{fm.get('name')}' neodpovídá adresáři")
        desc = str(fm.get("description") or "").strip()
        if not desc:
            err(sk, "chybí description")
        elif len(desc) > DESC_LIMIT:
            err(sk, f"description má {len(desc)} znaků > {DESC_LIMIT}")
        if "when_to_use" in fm:
            err(sk, "pole when_to_use claude.ai odmítne")
        body = sk.read_text(encoding="utf-8")
        if POINTER not in body:
            err(sk, "chybí odkaz na kontext Doktůrku")
        if "\n## Doktůrek specifics\n" not in body:
            err(sk, "chybí oddíl ## Doktůrek specifics")
        # Kategorie v textu může pokračovat dalšími slovy ("~~chat channels I should check"),
        # proto stačí, když začíná některou kategorií z CONNECTORS.md.
        for used in set(re.findall(r"~~([a-zA-Z][a-zA-Z ]*[a-zA-Z])", body)):
            u = used.lower()
            if not any(u == c or u.startswith(c + " ") for c in declared):
                err(sk, f"kategorie ~~{used} chybí v CONNECTORS.md pluginu")

    readme = pdir / "README.md"
    listed = sorted(set(re.findall(r"^\| `([a-z0-9-]+)` \|", readme.read_text(encoding="utf-8"), re.M)))
    if listed != skills:
        err(readme, f"tabulka skillů {listed} neodpovídá adresáři skills/ {skills}")

    mcp = pdir / ".mcp.json"
    if mcp.is_file():
        servers = json.loads(mcp.read_text(encoding="utf-8")).get("mcpServers", {})
        for key, cfg in servers.items():
            if "command" in cfg:
                args = " ".join(cfg.get("args", []))
                if re.search(r"(npx|uvx)\b", cfg["command"] + " " + args) and not re.search(r"(@|==)\d+\.\d+", args):
                    err(mcp, f"{key}: balíček musí mít připnutou verzi")
            elif not str(cfg.get("url", "")).startswith("https://"):
                err(mcp, f"{key}: chybí https URL")

root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
for entry in market.get("plugins", []):
    pj_path = ROOT / entry["source"] / ".claude-plugin/plugin.json"
    if pj_path.is_file():
        ver = json.loads(pj_path.read_text(encoding="utf-8")).get("version")
        if not re.search(rf"\[`{re.escape(entry['name'])}`\]\([^)]*\) \| {re.escape(str(ver))} \|", root_readme):
            err("README.md", f"tabulka pluginů neuvádí {entry['name']} ve verzi {ver}")

SECRET = re.compile(r"(sk-ant-[A-Za-z0-9_-]{10,}|ghp_[A-Za-z0-9]{30,}|xox[bpa]-[0-9A-Za-z-]{10,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY)")
RODNE_CISLO = re.compile(r"(?<![\d/])\d{6}/\d{3,4}(?![\d/])")
ABS_PATH = re.compile(r"(/home/[a-z]|/Users/[A-Za-z]|/root/|/tmp/claude)")
for f in ROOT.rglob("*"):
    if ".git" in f.parts or not f.is_file() or f.suffix in {".png", ".jpg", ".webp"}:
        continue
    try:
        text = f.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    if f.name == "check_repo.py":
        continue
    if SECRET.search(text):
        err(f, "vypadá jako tajemství")
    if RODNE_CISLO.search(text):
        err(f, "vypadá jako rodné číslo (jen syntetická data, bez lomítkového tvaru)")
    if ABS_PATH.search(text):
        err(f, "absolutní lokální cesta")

for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    text = re.sub(r"```.*?```", "", md.read_text(encoding="utf-8"), flags=re.S)
    for link in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text):
        if re.match(r"^[a-z]+:", link) or link.startswith("/"):
            continue
        if not (md.parent / link).exists():
            err(md, f"nefunkční odkaz {link}")

if errors:
    print("\n".join(f"✗ {e}" for e in errors))
    sys.exit(1)
print(f"✓ {len(names)} pluginů v pořádku")
