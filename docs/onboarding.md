# Onboarding

Repo jest biblioteką zasad i przykładów, nie instalatorem. Instrukcje są propozycjami, nie gwarancją działania w każdej wersji Hermes.

## Nowy użytkownik
1. Zainstaluj i skonfiguruj Hermes według [oficjalnej dokumentacji](https://hermes-agent.nousresearch.com/docs/). Zapoznaj się z kosztami, dostawcą i zatwierdzaniem poleceń. Nie udostępniaj sekretów w promptach.
2. Sklonuj repo: `git clone https://github.com/aievolutionpl/hermes-workspace-os.git`, następnie `cd hermes-workspace-os`. Przejrzyj [workflow](workflows.md) i [szablon](../templates/task.md); same pliki nie zmieniają Hermesa.
3. Poproś agenta o bezpieczne zadanie tylko do odczytu: „Przeczytaj templates/task.md i zaproponuj wypełnienie fikcyjnymi danymi. Nie zmieniaj plików ani ustawień”. Sprawdź wynik.
4. Opcjonalnie zapoznaj się z [oficjalną dokumentacją skilli](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/). Najpierw przeczytaj wybrany SKILL.md, porównaj nazwę z istniejącymi i sprawdź aktualne opcje instalacji w dokumentacji. Nie nadpisuj istniejących skilli.
5. Dodaj pamięć lub pliki kontekstu wyłącznie świadomie; nie zapisuj danych osobowych bez potrzeby. Harmonogramy, integracje i dostęp do kont zostaw na później.

## Masz już workspace
1. Sprawdź istniejące instrukcje, skille, konfigurację i zmiany użytkownika tylko do odczytu; nie zakładaj, że nazwy lub lokalizacje są standardowe.
2. Porównaj jeden istniejący proces z [workflow](workflows.md); zachowaj istniejące reguły i zaproponuj najmniejszą zmianę.
3. Przed zmianą skopiuj lub wersjonuj własne pliki, ustal zakres i sposób cofnięcia; nie zmieniaj konfiguracji, pamięci ani automatyzacji bez zgody.
4. Wykonaj zadanie testowe i zweryfikuj wynik, a nie tylko obecność pliku. Dokumentuj ograniczenia.

Materiały w `skills/` są samodzielnymi propozycjami, nie zostały w tym repo zweryfikowane przez instalację ani uruchomienie w Hermes. Odsyłacze do repozytorium wewnątrz głównego SKILL.md są przeznaczone do przeglądania z checkoutu; pojedyncza kopia skilla bez reszty repo ich nie zawiera.
