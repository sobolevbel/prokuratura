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

1. W beehiiv zostaw domyślny adres pocztowy dostawcy w stopce. Adres projektu może służyć do odpowiedzi. Sprawdź [umowę o ochronie danych](https://www.beehiiv.com/dpa).
2. Włącz [Double Opt-in Email](https://www.beehiiv.com/support/article/13081072798743-double-opt-in-and-smart-nudge-how-they-work-and-why-they-matter) w Settings → Emails → Preset Emails. Użyj jednego pola e-mail, opisz, czego dotyczy subskrypcja, i dodaj na formularzu link do polityki prywatności. Zostaw wyłączone rekomendacje i reklamy.
3. Sprawdź na własnych adresach zapis, przejście z Pending do Active po kliknięciu w link, treść i nagłówki wiadomości oraz adres pocztowy w stopce. Wypisanie można sprawdzić w profilu testowego subskrybenta, do którego prowadzi link w stopce wiadomości wysłanej na jego adres. Po wypisaniu sprawdź, czy status zmienił się na Inactive.
4. W [`privacy.toml`](privacy.toml) ustaw `contact_email` i `beehiiv_form_url`, a następnie uruchom `python3 build.py`. Pusty URL ukrywa zapis i część polityki dotyczącą subskrypcji. Zmiany publikuj po sprawdzeniu formularza i treści polityki.

Przed rozpoczęciem regularnych wysyłek ustal z beehiiv, czy można wyłączyć pomiar otwarć i kliknięć, i sprawdź źródło otrzymanej wiadomości. Zgoda na subskrypcję dotyczy wysyłki aktualizacji. Opcjonalna analityka wymaga osobnej oceny i, gdy jest wymagana, odrębnej zgody.

Link w stopce i nagłówki `List-Unsubscribe` sprawdź osobno w rzeczywistej wysyłce ograniczonej do testowych adresów. Podgląd i wiadomość testowa nie odtwarzają wszystkich mechanizmów zwykłego wydania. Jeśli bieżący plan nie pozwala ograniczyć odbiorców do testowych adresów, nie wysyłaj testu do całej listy.

Po aktualizacji strony przygotuj w beehiiv krótką wiadomość z linkiem do aktualizacji i polityki prywatności. Wysyłaj ją tylko do aktywnych subskrybentów. Raz w miesiącu przejrzyj niepotwierdzone zapisy i usuń te, dla których potwierdzenie nie jest już potrzebne. Po wypisaniu zachowaj tylko dane potrzebne do zablokowania dalszej wysyłki.
