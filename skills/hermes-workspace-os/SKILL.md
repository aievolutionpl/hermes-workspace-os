---
name: hermes-workspace-os
description: "Use when setting up a NEW Hermes Agent workspace or onboarding a new agent/user — complete operating system for a fresh Hermes install: vault, memory, skills, cron, verification, cost control."
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
| [modules/09-context-files.md](modules/09-context-files.md) | AGENTS.md, SOUL.md, @-references — warstwy kontekstu |
| [modules/10-security.md](modules/10-security.md) | Sekwencja wdrożenia, profile, approvals, Docker |
| [modules/11-smart-workflow.md](modules/11-smart-workflow.md) | Prompt cache, sesje, limity cronów, audyty cykliczne |
| [modules/12-recipes.md](modules/12-recipes.md) | 10 recipes — połączenia workflow, które się kumulują |
| [modules/13-skill-combos.md](modules/13-skill-combos.md) | Pakiety skilli jako wirtualni pracownicy (działy) |
| [modules/14-failbook.md](modules/14-failbook.md) | Znane failury + fixy (cron, mail, memory, media, git) |
| [modules/15-anti-slop.md](modules/15-anti-slop.md) | Quality gate — tekst, obrazki, UI |
| [modules/16-step-beyond.md](modules/16-step-beyond.md) | Step Beyond — agent jako przedłużenie myśli (L1/L2/L3) |
| [modules/17-marketing-psychology.md](modules/17-marketing-psychology.md) | Psychologia reklam — 6 aniołów, lejek 60/20/10, jasnopis |
| [modules/18-virtual-team.md](modules/18-virtual-team.md) | Virtual team — org chart, rekrutacja, tygodniowy rytm |
| [modules/19-design-taste.md](modules/19-design-taste.md) | Design & taste — anti-AI-look dla obrazków/UI/copy |

## Quick start (nowy workspace, orientacyjnie)

> **Ważne:** instalując ten skill, najpierw przeczytaj [README.md](../../README.md)
> (filozofia + recipes), potem wróć tutaj po plan wdrożenia.

Kolejność ma znaczenie: **memory first, persona second, interfaces last.**

1. Wybierz ścieżkę w [przewodniku onboardingu](../../docs/onboarding.md); najpierw poznaj granice dostępu.
2. Zacznij od fikcyjnego szablonu zadania i jednego workflow; pamięć i pliki kontekstu dostosuj wyłącznie za zgodą użytkownika.
3. Przetestuj bezpieczne zadanie i sprawdź wynik. Automatyzację planuj osobno, po ustaleniu limitów, zatwierdzeń i sposobu zatrzymania.

## Checklist audytu istniejącego workspace

- [ ] Jest jedno kanoniczne ACTIVE_CONTEXT (aktualne < 7 dni)?
- [ ] Stabilne fakty oddzielone od historii sesji?
- [ ] Powtarzalne procedury są skills, nie w pamięciroboczej?
- [ ] Crony mają continuity + przypięty model (fallback)?
- [ ] Naming: zero luźnych plików na root, zero `_final2`?
- [ ] Weryfikacja E2E przy każdej deklaracji "działa"?
- [ ] Cotygodniowy przegląd infrastruktury ustawiony?
- [ ] Approvals ON, allowlisty per platforma, sekrety poza memory/chat?
- [ ] Profile izolowane per rola/eksperyment?
- [ ] Prompt cache chroniony (bez skakania po modelach w sesji)?
- [ ] Wszystko unattended ma budget cap i disable command?
- [ ] Każdy workflow ma QA step PRZED delivery?
- [ ] Failbook karmiony (nowy fail → patch w 24h)?
