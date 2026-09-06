# 03 · Skills — proceduralna pamięć

## Kiedy pisać skill
- Zadanie wykonane 2+ razy lub wymagające dokładnych kroków/komend
- Procedura z pułapkami, które odkryłeś krwią
- Wszystko, co musi być zrobione TAK SAMO za miesiąc

## Anatomia dobrego SKILL.md
```yaml
---
name: nazwa-kebab
description: Use when <trigger>. <one-line behavior>.   # trigger w pierwszych 57 znakach!
---
```
Body: numerowane kroki z DOKŁADNYMI komendami → weryfikacja (jak sprawdzić, że działa)
→ ⚠️ Pitfalls (każdy realnie napotkany problem z fixem).

## Zasady
- Skills ewoluują — zawsze `skill_view` przed użyciem, nie ufaj pamięci.
- Skill przestarzały/naprawiony w trakcie pracy → **patch natychmiast**, nie "potem".
- Po trudnym/iteracyjnym zadaniu → zaproponuj zapis jako skill.
- Jeden skill = jedna procedura. Nie robić mega-SKILLA na wszystko.
- Sekrety (klucze API) NIGDY w SKILL.md — odwołanie do env var / pliku z umask.

## Repo skilli na GitHub
Skills warto trzymać w repo (backup + przenośność między maszynami/profilami):
```
repo/
├── README.md
└── skills/<skill-name>/SKILL.md
```
Klonuj do `~/.hermes/skills/` przez symlink lub kopiuj wybrane — agent czyta standardową strukturę.
