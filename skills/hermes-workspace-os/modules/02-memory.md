# 02 · Memory — co zapamiętywać, a czego nie

Injected memory jest czytana w KAŻDEJ turze. Każdy znak to koszt i szum.

## ZAPISUJ (high-signal)
- Preferencje i korekty użytkownika ("Chris odrzuca X, chce Y") — najwyższy priorytet
- Fakty o środowisku (WSL, ścieżki mountów, gdzie są klucze/vault)
- Hard rules ("zero `**` w mailach", "flue zawsze do sufitu")
- Pitfalle narzędzi (każde odkryte metodą prób)
- Stan kluczowych projektów (kanon, wersje approved, backupy)

## NIE ZAPISUJ
- Logi wykonania, "co zrobiłem dziś" → sesja/archive
- TODO tymczasowe → plik TASKS, nie memory
- Fakty świeże < 7 dni, które się przedawnią
- Dane surowe (listy leadów, dumpy) → pliki CSV w vault
- Procedury → to rola SKILLS

## Format
Deklaracje, nie rozkazy ("User prefers X" ✓ / "Always do X" ✗ — rozkaz w memory
zostanie odczytany jako dyrektywa w przyszłej sesji i zablokuje bieżące polecenie).

## Higiena
- Limit znaków się przepełni — planuj od początku ~80% wykorzystania.
- Konsolidacja: jedno wywołanie batch (remove stale + add new) jest atomowe.
- Przy pełnej pamięci: najpierw usuń przedawnione, potem dodaj — w JEDNYM batchu.
