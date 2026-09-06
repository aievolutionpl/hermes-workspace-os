# Hermes Workspace OS 🧠

**Kompletny system operacyjny dla workspace agenta Hermes** — vault, pamięć, skills, cron,
weryfikacja, koszty i higiena. Zbudowany z ~1 roku realnej codziennej pracy
(11 marek, crony produkcyjne, media pipeline, outreach).

## Dla kogo
Każdy, kto stawia nowego agenta Hermes (albo audytuje istniejący) i chce uniknąć
chaosu, duplikacji i halucynacji w pierwszym miesiącu.

## Jak użyć

### Opcja A — instalacja jako skill (zalecane)
```bash
git clone https://github.com/aievolutionpl/hermes-workspace-os.git
cp -r hermes-workspace-os/skills/hermes-workspace-os ~/.hermes/skills/
```
Agent wykryje skill `hermes-workspace-os` automatycznie i użyje go przy stawianiu
nowego workspace lub onboardingu.

### Opcja B — lektura
Cały system to 8 modułów w `skills/hermes-workspace-os/modules/` — każdy samodzielny.

## Zawartość

| Moduł | Temat |
|-------|-------|
| [01-vault](skills/hermes-workspace-os/modules/01-vault.md) | Struktura vaultu i warstwy pamięci (L0–L4) |
| [02-memory](skills/hermes-workspace-os/modules/02-memory.md) | Co zapamiętywać — high-signal memory |
| [03-skills](skills/hermes-workspace-os/modules/03-skills.md) | Proceduralna pamięć — kiedy i jak pisać skills |
| [04-cron](skills/hermes-workspace-os/modules/04-cron.md) | Rutyny zaplanowane — 6 pułapek produkcyjnych |
| [05-verification](skills/hermes-workspace-os/modules/05-verification.md) | Zero "obietnic" — normy weryfikacji per typ pracy |
| [06-costs](skills/hermes-workspace-os/modules/06-costs.md) | Routowanie modeli, fallback, redukcja kosztów |
| [07-parallel](skills/hermes-workspace-os/modules/07-parallel.md) | Delegacja i subagenci |
| [08-hygiene](skills/hermes-workspace-os/modules/08-hygiene.md) | Naming, foldery, archiwizacja |
| [09-context-files](skills/hermes-workspace-os/modules/09-context-files.md) | AGENTS.md, SOUL.md, warstwy kontekstu |
| [10-security](skills/hermes-workspace-os/modules/10-security.md) | Sekwencja wdrożenia, profile, approvals, Docker |
| [11-smart-workflow](skills/hermes-workspace-os/modules/11-smart-workflow.md) | Prompt cache, sesje, cron caps, audyty cykliczne |
| [12-recipes](skills/hermes-workspace-os/modules/12-recipes.md) | 10 recipes — gotowe połączenia workflow |
| [13-skill-combos](skills/hermes-workspace-os/modules/13-skill-combos.md) | Pakiety skilli = wirtualni pracownicy |
| [14-failbook](skills/hermes-workspace-os/modules/14-failbook.md) | Znane failury i fixy |
| [15-anti-slop](skills/hermes-workspace-os/modules/15-anti-slop.md) | Quality gate outputu |

## Recipes — na szybko
| Recipe | Co robi |
|--------|---------|
| R1 Gather cheap, reason expensive | `execute_code` zbiera → subagent analizuje z clean context |
| R2 Monitor-gated cron + continuity | Agent budzi się TYLKO przy zmianie, dedupe vs poprzedni przebieg |
| R3 Korekta → skill → repo | Poprawka jednorazowa staje się permanentna i przenośna |
| R4 Session search → vault | Historyczne szczegóły awansują na trwałe fakty |
| R5 Subagent review | Fresh-context recenzent łapie to, autor przyzwyyczaił |
| R6 Cron → draft → approve → publish | Crony nigdy nie publikują bez review stepu |
| R8 Weekly ops audit | Infrastruktura audytuje samą siebie |
| R9 Profile per rola | Izolowane memory = brak biasów między działami |

## Trzy żelazne zasady
1. **Jedno miejsce na prawdę** — bez kanonicznego źródła agent duplikuje i halucynuje.
2. **Verified > fast** — żadne "it works" bez realnego testu.
3. **Korekta → reguła** — nigdy nie poprawiaj tego samego dwa razy; zapisuj jako skill/memory.

**Sekwencja wdrożenia:** memory first, persona second, interfaces last. Testuj tool calls, nie chat. Limituj wszystko, co działa unattended.

*Best practices uzupełnione researchem: oficjalne Hermes docs (tips, delegation patterns) + praktyki społeczności (profile-per-job, bezpieczne crony, prompt cache, warstwy pamięci).*

## Quick start — 60 minut
Szczegóły w [SKILL.md](skills/hermes-workspace-os/SKILL.md) → sekcja *Quick start*.

## Licencja
MIT
