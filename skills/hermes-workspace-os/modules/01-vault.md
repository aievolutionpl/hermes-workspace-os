# 01 · Vault — struktura i warstwy pamięci

Vault (Obsidian folder na dysku) = trwała pamięć agenta, dostępna zawsze.

## Struktura startowa

```
VAULT/
├── 00_START_HERE.md        # mapowanie vaultu, jak go czytać
├── 01_Memory/
│   ├── ACTIVE_CONTEXT.md   # CO SIĘ DZIEJE TERAZ (aktualizowany przy każdej akcji)
│   └── TASKS.md            # otwarte zadania
├── 02_Brands/<brand>/      # CONFIG.md, BRAND_OVERVIEW.md, assets — per brand/projekt
├── 03_Scripts/             # dokumentacja skryptów (same skrypty w ~/scripts)
├── 04_Archive/             # stare, ale cenne
├── 05_Research/            # raporty, benchmarki
├── 06_Clients/             # leady, konta, historia
└── 07_Resources/           # indeksy (np. github-repos-index.md), snippety
```

## Warstwy pamięci (kluczowa decyzja architektoniczna)

| Warstwa | Co | Gdzie | Retencja |
|---|---|---|---|
| L0 | Injected memory | wbudowana pamięć agenta (limit znaków!) | na stałe, high-signal only |
| L1 | Vault | dysk/Obsidian | trwałe dokumenty |
| L2 | Baza kontekstowa | sidecar DB (opcjonalnie) | agregaty |
| L3 | Semantic memory | np. memU | duże korpusy |
| L4 | Historia rozmów | session_search | automat |

**Zasada:** injected memory to sklepik z paragonami, nie magazyn. Fakty stable → CORE_MEMORY,
praca bieżąca → ACTIVE_CONTEXT, reszta → pliki. PII i hasła NIGDY w injected memory.

## Aktualizacja

- Po każdej istotnej akcji → dopisz do ACTIVE_CONTEXT (krótko, datowane).
- CORE_MEMORY = tylko fakty, które będą prawdziwe za rok.
- Zakaz: logi wykonania, "zrobiłem X dziś", stany tymczasowe → to do sesji/archive.
