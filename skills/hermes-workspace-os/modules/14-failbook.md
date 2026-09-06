# 14 · Failbook — znane failury i ich fixy

Wszystko poniżej zdarzyło się naprawdę. Nawyk: każdy nowy fail → patch tego modułu.

## Cron / harmonogramy
| Symptom | Przyczyna | Fix |
|---|---|---|
| Cron 503 "qwen no available channel" | Główny provider pusty (402) → fallback na losowy | Napełnij konto głównego; crony przypnij do stabilnego modelu |
| Pin modelu nie działa po edycji | `model_snapshot` w jobs.json nadpisuje pin | Ręcznie wyczyść snapshot w jobs.json |
| Cron tnie się o 120s | Limit agent-run | Ciężkie deterministyczne → `no_agent: true` + skrypt |
| Agent odpala się co tick za darmo? Nie — za kasa | Brak monitor gate | `monitor:` z deterministycznym hasmem |
| "0 odpowiedzi" w digescie | Resend send-only, brak source inbound | To NIE brak reply; sprawdź kanał odbioru |

## Mail
| Symptom | Przyczyna | Fix |
|---|---|---|
| Treść maila z prefiksami `N\|` | Body wzięty z read_file (numery wierszy) | Czytaj body przez pathlib read_text |
| `**bold**` jako gwiazdki w Gmail/Outlook | Markdown nie renderuje się w klientach | Sanitizer: zero `**`, zero `>` (wygląda jak quoting) |

## Pamięć / kontekst
| Symptom | Przyczyna | Fix |
|---|---|---|
| Agent "zapomniał" fakt zapisany dziś | Memory snapshot frozen do nowej sesji | `/new` po ważnym zapisie |
| Memory pełna, add odrzucony | Limit znaków | Jeden batch: remove stale + add new (atomowo) |
| Cross-project bleed | Wspólny profil dla dwóch projektów | Osobny profil; secrets osobno zawsze |
| Halucynacje po "roszerzeniu" | Za dużo w injected memory | Konsolidacja; surowe dane → pliki |

## Media / generacja
| Symptom | Przyczyna | Fix |
|---|---|---|
| "Saved" bez pliku na dysku | Prompt nie zawierał ścieżki ref | Path ref IN prompt; szukaj `find ~/.codex/generated_images -newermt '10 min'` |
| M misspelled text w obrazkach | AI garbuje litery | QA wizyjne zawsze; polskie znaki per-step |
| CDN linki FB wygasają | Expiry minut-godziny | Pobieraj asset natychmiast, nie cache'uj URL |

## Git / publikacja
| Symptom | Przyczyna | Fix |
|---|---|---|
| Push pyta o username | Brak credential helpera | `gh auth setup-git` raz |
| Approval gate blokuje `gh` z tokenem | PAT w command line | Token przez temp file (umask 077) → stdin; usuń plik |
| "Repo utworzone" bez plików | `--source .` bez `git init` | Init + commit przed `gh repo create` |

## Zasada nadrzędna
Fail → 1) napraw teraz, 2) patch SKILL.md / tego failbooka natychmiast (R3),
3) jeśli powtarzalny → skill. Failbook żyje tylko, gdy jest karmiony.
