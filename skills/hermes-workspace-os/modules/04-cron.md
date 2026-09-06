# 04 · Cron — rutyny produkcyjne

## Start
Ustaw rutyny ZANIM się o nie poproszono: briefing poranny, monitoring kanałów,
cotygodniowy przegląd. Cron = drugi pracownik, który pracuje, gdy Ty śpisz.

## Pułapki produkcyjne (wszystko przechodzone)
1. **Continuity** — cron działa w świeżej sesji bez kontekstu. Ustaw `continuity: true`
   żeby job widział swój poprzedni output (dedupe, kontynuacja). Prompt musi być w 100% self-contained.
2. **Model fallback** — gdy główny provider padnie (saldo 0, 402), cron dostał 503 z
   innego providera. Przypnij cron do stabilnego taniego modelu + napełniaj konto głównego.
3. **Model snapshot** — edycja crona może nie czyścić `model_snapshot` w jobs.json,
   który NADPISUJE pin modelu. Sprawdź plik jobs.json ręcznie przy problemach.
4. **Timeout** — crony tną się po 120s przy ciężkim agent-run. Ciężkie, deterministyczne
   prace → `no_agent: true` + skrypt (stdout = wynik, pusty stdout = brak wysyłki).
5. **Delivery** — zdecyduj cel (origin / kanał Discord / local) przy tworzeniu, nie po fakcie.
6. **Monitor gate** — `monitor:` (URL/skrypt) oszczędza 90% ticków: agent budzi się
   TYLKO przy zmianie. Output musi być deterministyczny (bez timestampów!).

## Zestaw startowy
- Poranny briefing (mail/voice, dni robocze)
- Monitoring źródeł (YouTube/reddit/trends — monitor-gated)
- Cotygodniowy review infrastruktury (co padło, co wyczyścić, koszty)
