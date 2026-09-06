# 11 · Smart workflow — nawyki, które się kumulują

## Cachowanie promptu = największa dźwignia kosztów
Providerzy cache'ują prefix konwersacji. Stabilny system prompt (te same context
files, memory) = tańsze tury. Każde `/model`, fallback providera, rotacja kluczy
unieważnia cache i cała historia czytana jest po pełnej cenie. Na długiej sesji:
zacznij NOWĄ sesję na innym modelu, zamiast skakać tam i z powrotem.

## Utrzymanie sesji
- `/usage` i `/context` (opcjonalnie `/context all` — koszt per skill/toolset) regularnie.
- Sesja gęstnieje → `/compress` (sumaryzuje historię, zachowuje kontekst), nie walka do końca okna.
- Sesje nazywaj (`/title auth-refactor`) → łatwo wznowić `hermes -r "auth-refactor"`.
- Jakość cicho spada w długich, brudnych sesjach → świeży czat zamiast pchania dalej.
- `/sethome` w docelowym czacie Discord/Telegram — tam lecą wyniki cronów.

## Niezaobsługiwane = zlimitowane
Każdy tick crona to pełna tura agenta. Automat celujący w płatne API potrafi
spalić budżet za noc. Budget caps na WSZYSTKO, co działa unattended — nie opcja.
Warstwy automatyzacji: `/loop` (polling w sesji) vs `/goal` (iteracja do celu) vs
cron (unattended) — zły wybór warstwy = zmarnowane tokeny.

## Start cronów: read-only najpierw
1. Uruchom workflow ręcznie 2× z przewidywalnym wynikiem.
2. Dopiero potem harmonogram — najpierw do prywatnego draft-channelu z review.
3. Sprawdź logi, retry i koszt po pierwszym zaplanowanym przebiegu.
4. Zapisz komendę wyłączania (disable) tam, gdzie operator ją znajdzie.
Nie zaczynaj od cronów, które wysyłają wiadomości publiczne albo mutują produkcję.

## Cykliczne audyty (tygodniowo / miesięcznie)
- `/journey` — timeline skilli i memory; edytuj/usuń co złe (self-improvement kumuluje błędy tak samo jak wygrane).
- Eksport/backup agenta (persona, skills, memory, cron, settings — bez sekretów) co tydzień i przed każdą przebudową.
- `hermes skills list` + audit auto-generowanych skilli: skill istnieje ≠ jest używany; ważne wywołuj jawnie.
- "Clean up your memory" — comiesięczna higiena.

## Batch i delegacja
- Operacje seryjne → `execute_code` (skrypt robi 10+ kroków za cenę jednej tury).
- Równoległy research/kod → `delegate_task`; context field musi zawierać CAŁOŚĆ
  (subagenci zaczynają zupełnie świeżo — "fix the bug we discussed" nic im nie mówi).
- Self-report subagenta ≠ fakt → zweryfikuj (tests, diff) sam.
