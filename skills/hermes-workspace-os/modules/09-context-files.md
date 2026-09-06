# 09 · Context files — AGENTS.md i SOUL.md

## Podział ról (mentalny model)
- `~/.hermes/SOUL.md` — KIM agent jest (osobowość, ton, co może). Per profil.
- `AGENTS.md` (root projektu) — JAKIE SĄ ZASADY projektu. Auto-ładowany co sesję.
- `@<path|url>` — jednorazowe wstrzyknięcie pliku/diff/URL do jednej wiadomości.
- Memory — CO agent wie (fakty). Skills — JAK robi (procedury).

## AGENTS.md — krótki i chirurgiczny
Wkładaj: decyzje architektoniczne, konwencje nazewnicze, podejście do testów,
"nigdy nie commituj .env", preferowane biblioteki.
**Przeładowany AGENTS.md jest gorszy niż brak** — każda linia leci w każdy prompt.
Skoro powtarzasz instrukcję po raz drugi → trafia do AGENTS.md.

## Zasady warstwowania
- Globalny głos (SOUL.md) + lokalne konwencje (AGENTS.md per projekt).
- `.cursorrules` jest rozpoznawany — nie duplikuj.
- Profile: SOUL.md jest per profil (aktywny profil = własne HERMES_HOME),
  AGENTS.md jest per katalog roboczy — nie mylić.
- Cron potrzebuje kontekstu projektu → ustaw jobowi working directory.

## Memory snapshot — pułapka
Memory zapisana w trakcie sesji trafia na dysk od razu, ale do promptu wejdzie
dopiero w NOWEJ sesji. Po ważnym zapisie pamięci → `/new`, jeśli dalsza praca
ma z niej korzystać.
