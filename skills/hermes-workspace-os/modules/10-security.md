# 10 · Bezpieczeństwo i izolacja

## Sekwencja wdrożenia (kolejność ma znaczenie)
**Memory first, persona second, interfaces last.** Najczęstszy błąd: piękny
dashboard + agent, który nic o Tobie nie wie. Najpierw pamięć/vault, potem SOUL.md,
na końcu kanały i integracje.

## Profile = izolacja
- **Jeden profil per rola** (research / content / inbox / outreach) i per eksperymentowany model.
- Izolowana pamięć = eksperymenty nie zaśmiecają roboczego agenta, porównania uczciwe.
- Osobny profil/bot token dla każdego bota, który ma nie dzielić stanu.

## Approval i dostępy
- Tryb bez potwierdzeń kusi szybkością — podczas nauki zostaw approvals ON.
- Przy zatwierdzaniu niebezpiecznych komend: "session" zamiast "always" (always =
  permanentny allowlist wzorca). Przeglądaj allowlisty co jakiś czas.
- Nigdy `GATEWAY_ALLOW_ALL_USERS=true` przy bocie z terminalem — tylko allowlisty
  per platforma lub DM pairing.
- Sekrety: env / 1Password / SOPS. Nie w chacie, nie w memory, nie w docs.

## Izolacja wykonania
- Nieznane repo / niezaufany kod → terminal backend w Dockerze (`TERMINAL_ENV=docker`).
  Destrukcyjne komendy w kontenerze nie zabijają hosta.

## Test prawdziwy
Setup, który pięknie odpowiada na chat, a pada przy pierwszym tool callu, jest bezużyteczny.
Przed zaufaniem nowemu modelowi/profilowi: kaź wykonać skill, przeczytać plik, szukać w sieci.
Testuj tool calls, nie rozmowę.
