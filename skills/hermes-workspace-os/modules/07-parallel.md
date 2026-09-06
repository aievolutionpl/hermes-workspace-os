# 07 · Praca równoległa i delegacja

## Kiedy delegować (subagent)
- Ciężki reasoning / research, który zalałby kontekst głównego agenta
- Niezależne workstreamy (research A + generacja B + QA C) — równolegle
- Batch operacji na wielu plikach/źródłach

## Kiedy NIE
- Jedna proste komenda → wykonaj bezpośrednio
- Zadanie wymagające pytania do użytkownika → subagenci nie mogą pytać
- Mechaniczna pętla bez reasoningu → kod w execute_code, nie subagent

## Zasady bezpieczne
- Subagent widzi TYLKO swój context — przekaż wszystko: ścieżki, konwencje, język odpowiedzi.
- Self-report ≠ fakt: side effect zewnętrzny (upload, publish) wymaga handle'u
  (URL/ID/ścieżka) do zweryfikowania przez głównego agenta.
- Podczas biegu: patrz na transkrypty, koryguj przez steer zanim za daleko odjedzie.

## Wzorzec zbierania wyników
N-elementowe zadania (wszystkie produkty / wszystkie wpisy) → batch do pliku
JSON/CSV w workspace per pod-batch, potem agregacja programatyczna
(dedupe/count/sort w Pythonie), NIE w głowie. Zweryfikuj policzoną liczbę
z żądaniem przed odpowiedzią.
