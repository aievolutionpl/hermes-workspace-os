---
name: hermes-workspace-os
description: Use when setting up a NEW Hermes Agent workspace or onboarding a new agent/user — complete operating system for a fresh Hermes install: vault, memory, skills, cron, verification, cost control.
---

# Hermes Workspace OS — system startowy dla nowego agenta

Kompletny system organizacji workspace dla Hermes Agent. Powstał z ~1 roku realnej
pracy (11 brandów, codzienne crony, research, media, outreach). Zastosuj każdy moduł
przy stawianiu nowego workspace lub audycie istniejącego.

## Filozofia (przeczytaj najpierw)

Traktuj agenta jak **członka zespołu z pamięcią i nawykami**, nie chatbota.
Różnica między "używam AI" a "mam cyfrowego pracownika" to: Vault + Skills + korekty w czasie.

Trzy żelazne zasady:
1. **Jedno miejsce na prawdę** — agent bez kanonicznego źródła zaczyna duplikować i halucynować.
2. **Verified > fast** — żadne "it works" bez realnego testu. Wynik z tool outputu, nie z wyobraźni modelu.
3. **Korekta → reguła** — każde "nie tak, zrób tak" ląduje w memory/skill, nigdy nie poprawiasz tego samego dwa razy.

## Moduły

Każdy moduł to osobny plik — wczytaj potrzebne, nie wszystkie naraz:

| Plik | Moduł |
|------|-------|
| [modules/01-vault.md](modules/01-vault.md) | Struktura vaultu (Obsidian/dysk) — warstwy pamięci |
| [modules/02-memory.md](modules/02-memory.md) | Co zapamiętywać, a czego nie (high-signal memory) |
| [modules/03-skills.md](modules/03-skills.md) | Kiedy i jak pisać skills (proceduralna pamięć) |
| [modules/04-cron.md](modules/04-cron.md) | Zadania zaplanowane — pułapki produkcyjne |
| [modules/05-verification.md](modules/05-verification.md) | Weryfikacja wyników — zero "obietnic" |
| [modules/06-costs.md](modules/06-costs.md) | Modele, fallback, kontrola kosztów |
| [modules/07-parallel.md](modules/07-parallel.md) | Delegacja i praca równoległa |
| [modules/08-hygiene.md](modules/08-hygiene.md) | Naming, foldery, archiwizacja — zero chaosu |

## Quick start (nowy workspace, 60 minut)

1. **Vault** (30 min): załóż strukturę z `01-vault.md` + wypełnij `ACTIVE_CONTEXT.md`.
2. **Memory** (5 min): zapisz 5–10 najważniejszych faktów o użytkowniku i środowisku.
3. **Skills** (10 min): przenieś 2–3 najczęstsze procedury do SKILL.md.
4. **Cron** (10 min): ustaw 1–2 rutyny (briefing / monitoring) z continuity.
5. **Hygiene** (5 min): reguły naming w vault indexie, żeby agent je czytał.

## Checklist audytu istniejącego workspace

- [ ] Jest jedno kanoniczne ACTIVE_CONTEXT (aktualne < 7 dni)?
- [ ] Stabilne fakty oddzielone od historii sesji?
- [ ] Powtarzalne procedury są skills, nie w pamięciroboczej?
- [ ] Crony mają continuity + przypięty model (fallback)?
- [ ] Naming: zero luźnych plików na root, zero `_final2`?
- [ ] Weryfikacja E2E przy każdej deklaracji "działa"?
- [ ] Cotygodniowy przegląd infrastruktury ustawiony?
