# Status zawiadomienia

Publiczna chronologia zawiadomienia dotyczącego wypowiedzi Tomasza Sakiewicza.
[Strona na GitHub Pages](https://sobolevbel.github.io/prokuratura/)

## Aktualizacja

1. Uzupełnij status w `content.toml` we wszystkich pięciu językach. Datę stanu zapisz w głównym polu `as_of_iso` jako tekst w formacie `YYYY-MM-DD` i zaktualizuj lokalizowane pola `as_of`. Generator sprawdza zgodność wszystkich pięciu dat przed zapisaniem stron. Przy nowym zdarzeniu dodaj do `EVENTS` w `build.py` datę i godzinę ze strefą czasową, identyfikator oraz klucze tłumaczeń. Tytuł i opis uzupełnij w `content.toml`.
2. Uruchom `python3 build.py` (Python 3.11 lub nowszy). Pliki `docs/**/index.html` są generowane z szablonu i tłumaczeń. Dokumenty po polsku edytuje się bezpośrednio w `docs/`.
3. Zapisz zmiany, w tym wygenerowane strony, i wypchnij je na `main`. GitHub Actions sprawdza, czy ponowne uruchomienie generatora nie zmienia plików w `docs/`. GitHub Pages publikuje katalog `/docs` z gałęzi `main`.

Publikuj wyłącznie kopie przeznaczone do udostępnienia. Oryginały korespondencji, dane kontaktowe i identyfikatory doręczeń przechowuj lokalnie.
