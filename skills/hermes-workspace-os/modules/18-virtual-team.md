# 18 · Virtual team — agent jako cała drużyna pracowników

> "Nie zatrudniaj agenta. Zatrudnij drużynę." Każdy pracownik = profil/rola +
> pakiet skilli + crony + delivery target. Handoff przez wspólny vault, nie przez pamięć.

## Org chart startowy

| Pracownik | Rola | Skille pakiet | Crony | Delivery |
|---|---|---|---|---|
| **Chief of Staff** | orkiestracja, priorytety, daily brief | morning-briefing, content-calendar, kanban | poranny brief 8:30 | mail/głosówka |
| **Researcher** | monitoring, konkurencja, trendy | deep-research, competitor-news-monitor, trends | monitor-gated, weekly digest | draft channel |
| **Content Creator** | posty, carousele, reele | brand guide, image-gen, carousel, stop-slop QA | content calendar pon/śr/pt | folder brandu → approve |
| **Media Producer** | wideo, voice, montaż | video pipeline, TTS, captions, music | na zamówienie | draft channel |
| **Growth / Ads** | kampanie, lejki, creative testing | ads framework (mod. 17), competitor ads intel, GA4 | weekly raport metryk | raport czat |
| **Sales / SDR** | leady, outreach, follow-upy | apollo, email verification, cold outreach, funnel digest | leady dziennie, digest tygodniowo | CSV + digest |
| **Ops / Infra** | utrzymanie agenta | failbook, hygiene, ops audit, backup | weekly audit | draft channel |

## Zasady budowy drużyny

1. **Profil per pracownik** (izolowana memory) — Sales nie dziedziczy biasów Researchera; porównania modeli uczciwe.
2. **Handoff przez vault** — wspólny dysk to "biurko firmowe"; każdy zapisuje output w kanonicznym miejscu (mod. 08), każdy czyta z tego samego miejsca. Zero przekazywania "przez chat".
3. **Jeden output per pracownik** — Content Creator dostarcza assety, nie "pomaga wszystkim". Rozmycie roli = rozmyta odpowiedzialność.
4. **QA gate przed handoffem** — nic nie przechodzi dalej bez weryfikacji (mod. 05, 15).
5. **Cron na stabilnym końcu łańcucha** — eksperymenty ręcznie, dopiero stabilne → harmonogram (mod. 11).
6. **Eskalacja do człowieka** — każdy pracownik ma zdefiniowane, CO wymusza approve: publikacja, wysyłka do klienta, wydatek, kasowanie.

## Rekrutacja (jak dodawać kolejnych)

1. Zidentyfikuj powtarzalną czynność, którą robisz tygodniowo > 1h.
2. Zbuduj pakiet z istniejących skilli (mod. 13) — nie pisz od zera.
3. Uruchom ręcznie 2× → dopiero potem cron (R6).
4. Po 2 tygodniach: audyt — co robi dobrze, co poprawić, czy output trafia we właściwe miejsce.
5. Skill bojowy (2+ użycia) → do repo (R3).

## Scalenie: tygodniowy rytm drużyny

```
PON  Chief of Staff: weekly plan + priorytety
WT   Researcher: digest konkurencji/trendów
ŚR   Content Creator: batch produkcji (kalendaż) → approve
CZW  Growth: raport kampanii (blended CAC/MER) → decyzje
PT   Sales: funnel digest → follow-upy
SOB  Ops: audit infrastruktury + backup
NDZ  cicho (serwery pracują, ludzie nie)
```

## KPI drużyny
Ile godzin człowieka zaoszczędzone tygodniowo · Ile follow-upów zablokowanych
przez Step Beyond (mod. 16) · Ile faili złapanych przez QA przed delivery ·
Blended CAC / MER (jeśli drużyna zarabia) · Fill % memory i koszty providerów.
