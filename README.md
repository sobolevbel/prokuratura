# Status zawiadomienia

Publiczna chronologia zawiadomienia dotyczącego wypowiedzi Tomasza Sakiewicza.
[Strona na GitHub Pages](https://sobolevbel.github.io/prokuratura/)

## Aktualizacja

1. Uzupełnij status i datę stanu w `content.toml` we wszystkich pięciu językach. Przy nowym zdarzeniu dodaj odpowiadający mu wpis w sekcji chronologii w `build.py` oraz teksty w `content.toml`.
2. Uruchom `python3 build.py` (Python 3.11 lub nowszy). Pliki `docs/**/index.html` są generowane z szablonu i tłumaczeń. Dokumenty po polsku edytuje się bezpośrednio w `docs/`.
3. Zapisz zmiany, w tym wygenerowane strony, i wypchnij je na `main`. GitHub Pages publikuje katalog `/docs` z tej gałęzi.

Publikuj wyłącznie kopie przeznaczone do udostępnienia. Oryginały korespondencji, dane kontaktowe i identyfikatory doręczeń przechowuj lokalnie.

## Powiadomienia e-mail

Strona prowadzi do publicznego formularza beehiiv. Serwis obsługuje potwierdzenie adresu, listę subskrybentów, wysyłkę i wypisanie.

1. W beehiiv ustaw nazwę „Aktualizacje sprawy” i zostaw domyślny adres pocztowy dostawcy w stopce. Adres projektu może służyć do odpowiedzi. Sprawdź [umowę o ochronie danych](https://www.beehiiv.com/dpa).
2. Włącz [Double Opt-in Email](https://www.beehiiv.com/support/article/13081072798743-double-opt-in-and-smart-nudge-how-they-work-and-why-they-matter) w Settings → Emails → Preset Emails. Użyj jednego pola e-mail, opisz, czego dotyczy subskrypcja, i dodaj na formularzu link do polityki prywatności. Zostaw wyłączone rekomendacje i reklamy.
3. Sprawdź na własnych adresach zapis, przejście z Pending do Active po kliknięciu w link, treść i nagłówki wiadomości oraz adres pocztowy w stopce. Wypisanie z listy sprawdź na rzeczywistej wysyłce wyłącznie do testowych subskrybentów, ponieważ podgląd nie odtwarza całego procesu.
4. W [`privacy.toml`](privacy.toml) ustaw `contact_email` i `beehiiv_form_url`, a następnie uruchom `python3 build.py`. Pusty URL ukrywa zapis i część polityki dotyczącą subskrypcji. Zmiany publikuj po sprawdzeniu formularza i treści polityki.

Po aktualizacji strony opublikuj w beehiiv krótką wiadomość z linkiem do aktualizacji. Wysyłaj ją tylko do aktywnych subskrybentów. Po wypisaniu zachowaj jedynie dane potrzebne do zablokowania dalszej wysyłki.
