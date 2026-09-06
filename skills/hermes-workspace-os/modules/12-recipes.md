# 12 · Recipes — połączenia workflow, które się kumulują

Gotowe kombinacje narzędzi Hermes. Każdy recipe = wzorzec użyty produkcyjnie.

## R1 · Gather cheap, reason expensive
Mechaniczne zebranie danych przez `execute_code` (10+ tool calls za cenę jednej
tury, zero kosztu kontekstu) → wynik do pliku → JEDEN `delegate_task` z clean
contextem na ciężką analizę.
```
execute_code (scrape/CSV/API) → workspace/data.json
delegate_task("analiza X, context: ścieżka pliku + pytanie badawcze")
```
Dlaczego działa: koszt tokens leci na skrypt, nie na model; subagent dostaje
10-linijkowe podsumowanie zamiast 200-liniowego JSON.

## R2 · Monitor-gated cron + continuity digest
Cron z `monitor:` (URL/skrypt) budzi agenta TYLKO przy zmianie źródła.
`continuity: true` — agent widzi swój poprzedni output → dedupe, "tylko NOWE
od ostatniego przebiegu". Monitor script musi być deterministyczny (hash treści,
bez timestampów).
```
monitor: sha256(feed) → zmiana? → agent: "nowe vs poprzedni digest, dodaj do digest.md"
```

## R3 · Korekta → skill → repo (pętla uczenia)
1. Agent popełnia błąd / odkrywa working path.
2. `skill_manage(patch)` natychmiast — pitfall + fix do SKILL.md.
3. Skills w git repo → push → symlink do `~/.hermes/skills/` na każdej maszynie.
Efekt: poprawka jednorazowa staje się permanentna i przenośna.

## R4 · Session search → vault promotion
Szczegóły historyczne z `session_search` (L4) → gdy fakt okazuje się stabilny →
wpis do vault (L1). Nigdy odwrotnie. Decision tree zapisu:
secrets→env · kod→git · decyzje/runbook→vault · procedury→skill · preferencje→memory · temp→sesja.

## R5 · Subagent review (fresh-context QA)
Po produkcji (strona/tekst/kod) → `delegate_task` z rolą recenzenta, który NIE
widzi procesu powstania — łapie to, co autor przyzwyyczaił. Pass context:
ścieżki plików + checklist kryteriów. Self-report zweryfikuj sam (diff/test).

## R6 · Cron → draft → approve → publish (bezpieczna publika)
```
cron (research/draft) → deliver: draft-channel → człowiek: "go" → agent publikuje
```
Crony nigdy nie publikują publicznie bez review stepu. Draft channel = tarcza
przed "mały błąd powtarza się codziennie o 8:00".

## R7 · Image/asset pipeline z QA
Generacja batch → QA wizyjne (polskie znaki, typografia, brand) → odrzucone do
regeneracji z korektą promptu → final do folderu brandu (`08-hygiene` naming) →
approved vsze w vault indexie. Zawsze aprobata człowieka PRZED animacją/publikacją.

## R8 · Weekly ops audit (cron na samego siebie)
Cotydniowy cron: sprawdz memory fill %, martwe crony, allowlisty, koszty providerów,
skills nieużywane, chaos w folderach. Raport do draft channelu. Infrastruktura,
która audytuje samą siebie, nie gnije.

## R9 · One agent, many profiles (pull vs push)
Profile per rola: research-bot czyta, content-bot pisze, outreach-bot wysyła.
Izolowane memory = content-bot nie dziedziczy biasów researchu. Handoff między
rolami przez vault (wspólny dysk), nie przez pamięć.

## R10 · Interrupt-and-redirect zamiast mikro-zarządzania
Zamiast precyzować każdy krok: daj cel + granice ("nie publikuj bez zgody,
koszt < X") i pozwól agentowi iterować. Koryguj przez przerwanie w locie
(nowy komunikat = redirect), nie przez 5 rund doprecyzowań.
