<div align="center">

![Hermes Workspace OS](assets/hero.png)

# Hermes Workspace OS 🧠

**Kompletny system operacyjny dla workspace agenta Hermes.**

Vault · Pamięć · Skills · Cron · Weryfikacja · Koszty · Bezpieczeństwo · Anti-slop

[![Modules](https://img.shields.io/badge/modules-15-00E7FF)](#zawartość)
[![License](https://img.shields.io/badge/license-MIT-7CFF1E)](LICENSE)
[![Agent](https://img.shields.io/badge/built%20for-Hermes%20Agent-cyan)](https://github.com/NousResearch/hermes-agent)

*Zbudowane z ~1 roku realnej codziennej pracy: 11 marek, crony produkcyjne, media pipeline, outreach.*

</div>

---

## Dlaczego to istnieje

Hermes nie zawodzi na możliwościach — zawodzi na **nawykach setupu**. Typowy miesiąc
pierwszy: agent duplikuje pracę, halucynuje fakty, spala budżet na cronach bez limitu,
"zapomina" ustalenia. Ten skill to antydot: 15 modułów z zasadami, recipe'ami,
failbookiem i quality gate'em — wszystko przetestowane w boju, nie teoretyczne.

## Trzy żelazne zasady

1. **Jedno miejsce na prawdę** — bez kanonicznego źródła agent duplikuje i halucynuje.
2. **Verified > fast** — żadne "it works" bez realnego testu. Wynik z tool outputu, nie z wyobraźni.
3. **Korekta → reguła** — nigdy nie poprawiaj tego samego dwa razy; zapisuj jako skill/memory.

**Sekwencja wdrożenia:** memory first → persona second → interfaces last.
Testuj tool calls, nie chat. Limituj wszystko, co działa unattended.

## Instalacja

```bash
git clone https://github.com/aievolutionpl/hermes-workspace-os.git
cp -r hermes-workspace-os/skills/hermes-workspace-os ~/.hermes/skills/
```

Agent wykryje skill `hermes-workspace-os` automatycznie — wywołaj go przy stawianiu
nowego workspace lub onboardingu: `skill_view("hermes-workspace-os")`.
Można też dodać repo jako custom tap (`hermes skills`).

## Zawartość

### Fundament (moduły 01–08)
| Moduł | Temat |
|-------|-------|
| [01-vault](skills/hermes-workspace-os/modules/01-vault.md) | Struktura vaultu i warstwy pamięci (L0–L4) |
| [02-memory](skills/hermes-workspace-os/modules/02-memory.md) | Co zapamiętywać — high-signal memory, deklaracje nie rozkazy |
| [03-skills](skills/hermes-workspace-os/modules/03-skills.md) | Proceduralna pamięć — kiedy i jak pisać skills |
| [04-cron](skills/hermes-workspace-os/modules/04-cron.md) | Rutyny zaplanowane — 6 pułapek produkcyjnych |
| [05-verification](skills/hermes-workspace-os/modules/05-verification.md) | Normy weryfikacji per typ pracy (E2E, read-back, QA wizyjne) |
| [06-costs](skills/hermes-workspace-os/modules/06-costs.md) | Routowanie modeli, fallback, redukcja kosztów |
| [07-parallel](skills/hermes-workspace-os/modules/07-parallel.md) | Delegacja i subagenci |
| [08-hygiene](skills/hermes-workspace-os/modules/08-hygiene.md) | Naming, foldery, archiwizacja |

### Zaawansowane (moduły 09–15)
| Moduł | Temat |
|-------|-------|
| [09-context-files](skills/hermes-workspace-os/modules/09-context-files.md) | AGENTS.md, SOUL.md, warstwy kontekstu |
| [10-security](skills/hermes-workspace-os/modules/10-security.md) | Sekwencja wdrożenia, profile, approvals, Docker |
| [11-smart-workflow](skills/hermes-workspace-os/modules/11-smart-workflow.md) | Prompt cache, sesje, cron caps, audyty cykliczne |
| [12-recipes](skills/hermes-workspace-os/modules/12-recipes.md) | 10 recipes — połączenia workflow, które się kumulują |
| [13-skill-combos](skills/hermes-workspace-os/modules/13-skill-combos.md) | Pakiety skilli jako wirtualni pracownicy |
| [14-failbook](skills/hermes-workspace-os/modules/14-failbook.md) | Znane failury + fixy (cron, mail, memory, media, git) |
| [15-anti-slop](skills/hermes-workspace-os/modules/15-anti-slop.md) | Quality gate — tekst, obrazki, UI |

## Recipes — na szybko

| Recipe | Co robi |
|--------|---------|
| **R1** Gather cheap, reason expensive | `execute_code` zbiera → subagent analizuje z clean context |
| **R2** Monitor-gated cron + continuity | Agent budzi się TYLKO przy zmianie; dedupe vs poprzedni przebieg |
| **R3** Korekta → skill → repo | Poprawka jednorazowa staje się permanentna i przenośna |
| **R4** Session search → vault | Historyczne szczegóły awansują na trwałe fakty |
| **R5** Subagent review | Fresh-context recenzent łapie to, co autor przyzwyyczaił |
| **R6** Cron → draft → approve → publish | Crony nigdy nie publikują bez review stepu |
| **R7** Asset pipeline z QA | Generacja → QA wizyjne → regeneracja → folder brandu |
| **R8** Weekly ops audit | Infrastruktura audytuje samą siebie |
| **R9** Profile per rola | Izolowane memory = brak biasów między działami |
| **R10** Interrupt-and-redirect | Cel + granice zamiast mikro-zarządzania krok po kroku |

## Quick start — 60 minut

Pełny plan w [SKILL.md](skills/hermes-workspace-os/SKILL.md). Skrót:

1. **Vault + memory** (35 min) → 2. **SOUL.md** (5) → 3. **AGENTS.md** (10) →
4. **Skills** (10) → 5. **Cron read-only z limitem** (10) → 6. **Test tool calls** (5)

## Checklist audytu istniejącego workspace

W [SKILL.md](skills/hermes-workspace-os/SKILL.md) — 13 pytań tak/nie: ACTIVE_CONTEXT,
continuity cronów, approvals, profile, prompt cache, budget caps, QA steps, failbook.

## Filozofia

> Traktuj agenta jak członka zespołu z pamięcią i nawykami, a nie chatbota.
> Różnica między "używam AI" a "mam cyfrowego pracownika" to: Vault + Skills + korekty w czasie.

## Licencja

MIT
