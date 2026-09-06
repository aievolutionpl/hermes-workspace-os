# 06 · Koszty i modele

## Routowanie
- Rutyna (newsy, monitoring, proste crony) → tani/szybki model flash-klasy
- Myślenie/kreacja/research → model mocny
- Model na obrazki/wideo → osobny provider, osobny budżet

## Fallback
Główny provider PADNIE (saldo, rate limit, 402/503). Miej przypięty zapasowy
model do cronów i wiedzy, który. Objaw klasyk: cron zwraca 503 od losowego
providera z łańcucha fallback — przyczyna jest zawsze u GŁÓWNEGO dostawcy.

## Redukcja kosztów bez utraty jakości
- Monitor-gated crony (agent budzi się tylko przy zmianie)
- `no_agent` + skrypt dla deterministycznych zadań
- Subagenci z ograniczonymi toolsetami (mniej toolów = mniej tokenów na prompt)
- Pamięć compact — każdy znak injected memory płaci w każdej turze
- Extraction (web_extract) zamiast pełnych fetchy dla dużych stron
- Czat na Discord: wyłącz narrację narzędzi (tool_progress off) — mniej szumu, mniej kosztu

## Nawyk
Cotygodniowy przegląd: wydatki per provider, padnięcia, limity pamięci, klucze bliskie wygaśnięcia.
