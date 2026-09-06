# 13 · Skill combos — pakiety skilli jako gotowe "działy"

Skilli łączą się w pakiety = wirtualni pracownicy. Przykład z praktyki (JARVIS OS):

## Pakiet: Poranny pracownik (morning ops)
```
morning-briefing (voice briefing MP3)
+ daily-news-pl (przegląd newsów)
+ cron continuity (dedupe vs wczoraj)
+ deliver: mail/voice o stałej godzinie
```
Efekt: 8:30 codziennie głosówka z tym, co ważne — zero pytań z Twojej strony.

## Pakiet: Content factory (produkcja treści)
```
brand style guide (look, kolory, fonty — KANON, nie improwizacja)
+ image-gen skill (routing do taniego/dobrego providera)
+ QA wizyjne (polskie znaki, typografia — zawsze przed deliver)
+ naming/hygiene (folder brandu + data, zero _final2)
+ social-autoposter (publikacja po aprobacie)
+ graph-memory (cross-brand: wykrywa kolizje i duplikaty treści między markami)
```
Efekt: brief → assety → QA → folder → publikacja, jeden łańcuch, pełna spójność.

## Pakiet: Research desk
```
deep-research (multi-source: firecrawl/exa)
+ competitor-news-monitor (cron, monitor-gated)
+ reddit-content-recovery (fallbacki gdy WAF blokuje)
+ grounded-citations (każda teza z linkiem)
+ deliver: digest do draft channelu
```

## Pakiet: Sales engine
```
apollo-prospecting (leady) → lead-email-verification (higiena bazy)
→ instantly-cold-outreach (sekwencje) → reply_log → sales-funnel digest (cron weekly)
```
Cały funnel zamyka się w 4 skillach + 1 cronie; dane w CSV, nie w pamięci.

## Pakiet: Self-care agenta (ops on ops)
```
jarvis-dreaming (nocna pętla self-improvement)
+ graph-memory (co się powtarza między sesjami)
+ skills audit cron (/journey co tydzień)
+ backup agenta (eksport bez sekretów)
```

## Zasady budowania pakietów
1. Każdy pakiet ma JEDEN output (briefing / asset / lead / digest) — nie "wiele rzeczy".
2. Granice na wejściu (źródła) i wyjściu (delivery target) określone wprost.
3. QA step w środku, PRZED delivery — nie po.
4. Cron tylko na stabilnym końcu łańcucha; eksperymenty ręcznie.
5. Skill bojowy po 2. użyciu → do repo (R3).
