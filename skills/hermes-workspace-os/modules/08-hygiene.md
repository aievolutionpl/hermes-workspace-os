# 08 · Hygiene — naming, foldery, archiwizacja

## Reguła #1: ZERO luźnych plików na root
Root home i root dysku generacji = TYLKO foldery + symlinki.

## Struktura outputów
```
<GENERATION ROOT>/<brand-slug>/<asset-type>/<YYYY-MM-DD>/pliki
```
- brand slug: lowercase + myślniki (`home-fires-jersey`), NIGDY spacje/underscore
- asset-type: `ads/`, `carousel/`, `reels/`, `flyers/`...

## Skrypty
- Reużywalne → `~/scripts/`
- One-off → `_archive/analyze/` (nie zostawiaj 6 wersji tego samego)

## Archiwizacja
- Nigdy nie kasuj — przenieś do `_archive/<temat>/` lub `_archive/<YYYY-MM-opis>/`
- Wersje pośrednie → archive; final → folder brandu
- Sufiksy `_v2`, `_final`, `_FINAL2` zakazane na root

## Pytanie przed każdym zapisem
1. Folder brandu istnieje? → tam
2. One-off? → `_archive/`
3. Skrypt? → `scripts/`
4. Root? → NIE

## Chaos audit (raz w miesiącu)
Szukaj: plików na root, duplikatów `_final*`, cronów bez delivery, memory pełnej >90%,
skilli z nieaktualnymi komendami.
