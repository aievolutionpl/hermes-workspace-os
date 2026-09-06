# 05 · Verification — zero "obietnic"

## Hard rule
"Done" = każde kryterium akceptacji zweryfikowane realnym tool outputem.
Kompletowanie planu ≠ wykonanie zadania. Wynik musi być w odpowiedzi, nie opisany.

## Normy per typ pracy
- **Kod / strona / game** → E2E test w prawdziwej przeglądarce, zmierzony stan gry/aplikacji.
  Nigdy nie deklaruj "build działa" bez przejazdu.
- **Wysyłka (mail/Discord/API)** → odczytaj cel po akcji (read-back) i potwierdź treść
  (np. body maila bez artefaktów typu prefiksy numerów wierszy).
- **Pliki** → write tool z verified:true; nie re-readuj dla spokoju.
- **Git/push** → `gh api repos/.../git/trees` — weryfikuj drzewo, nie komunikat pusha.
- **Liczby/totalki** → deklarowane sumy to twarde asercje; rozbieżność = policz programatycznie.
- **Obrazki** → QA wizyjne własnym vision (typografia, polskie znaki ą ć ę ł ń ó ś ź ż!).

## Anti-patterns
- "Powinno działać", "już prawie", opisanie zamiast pokazania
- Podmienianie nieudanego wyniku wiarygodnie wyglądającą fabrykacją —
  uczciwy blocker > wymyślony rezultat. ZAWSZE.
