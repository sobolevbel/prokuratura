"""Generate the five static language editions for GitHub Pages."""
from datetime import date, datetime
from html import escape
from pathlib import Path
from string import Template
import tomllib

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "docs"
REPO = "https://github.com/sobolevbel/prokuratura"
URL = "https://sobolevbel.github.io/prokuratura/"
LANGUAGES = {
    "pl": "Polski",
    "en": "English",
    "be": "Беларуская",
    "uk": "Українська",
    "ru": "Русский",
}

MONTHS = {
    "pl": "stycznia lutego marca kwietnia maja czerwca lipca sierpnia września października listopada grudnia",
    "en": "January February March April May June July August September October November December",
    "be": "студзеня лютага сакавіка красавіка мая чэрвеня ліпеня жніўня верасня кастрычніка лістапада снежня",
    "uk": "січня лютого березня квітня травня червня липня серпня вересня жовтня листопада грудня",
    "ru": "января февраля марта апреля мая июня июля августа сентября октября ноября декабря",
}

EVENTS = (
    (datetime.fromisoformat("2026-11-07T18:23:51+01:00"), "odbior", "delivered", "delivery_note"),
    (datetime.fromisoformat("2026-11-07T18:23:49+01:00"), "nadanie", "sent", "sent_note"),
)

EVENT = Template("""        <li id="$day-$slug">
          <time class="date" datetime="$timestamp">$label</time>
          <div><h3>$title</h3><p>$note</p></div>
        </li>""")

PAGE = Template("""<!doctype html>
<html lang="$lang">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>$title | $brand</title>
  <meta name="description" content="$intro">
  <link rel="canonical" href="$url">
  $alternates
  <meta property="og:type" content="website">
  <meta property="og:title" content="$title">
  <meta property="og:description" content="$intro">
  <meta property="og:url" content="$url">
  <link rel="stylesheet" href="${base}assets/style.css">
</head>
<body>
  <header class="top">
    <div class="wrap">
      <span class="brand">$brand</span>
      <nav aria-label="$language_label">
        $language_links
      </nav>
    </div>
  </header>
  <div class="wrap hero">
    <p class="eyebrow">$eyebrow</p>
    <h1>$title</h1>
    <p class="lead">$intro</p>
    <div class="jump">
      <a href="#status">$status</a>
      <a href="#chronologia">$timeline</a>
      <a href="#materialy">$materials</a>
    </div>
  </div>
  <main class="wrap">
    <section class="card status" id="status">
      <h2>$status</h2>
      <p class="badge">$badge</p>
      <p>$status_note</p>
      <dl>
        <div><dt>$recipient</dt><dd>$office</dd></div>
        <div><dt>$updated</dt><dd><time datetime="$as_of_iso">$as_of</time></dd></div>
      </dl>
    </section>
    <section class="card" id="chronologia">
      <h2>$timeline</h2>
      <ol class="timeline">
$events
      </ol>
    </section>
    <section class="card" id="kontekst">
      <h2>$context</h2>
      <p>$context_note</p>
      <p>$request</p>
    </section>
    <section class="card" id="materialy">
      <h2>$materials</h2>
      <ul>
        <li><a href="${base}zawiadomienie.html" hreflang="pl">$filing</a></li>
        <li><a href="${base}potwierdzenia.html" hreflang="pl">$receipt</a></li>
        <li><a href="https://www.reddit.com/r/Polska/comments/1xqgiv7/" hreflang="pl">$reddit</a></li>
      </ul>
      <h3>$sources</h3>
      <ul>
        <li><a href="https://niezalezna.pl/polska/tragedia-na-rynku-w-krakowie-sa-zabici-w-strzelaninie-wstrzasajaca-relacja-tomasza-sakiewicza/583564" hreflang="pl">Niezalezna.pl · 15:32</a></li>
        <li><a href="https://new.tvrepublika.pl/W-Telewizji-Republika/Strzelanina-w-Krakowie-Sakiewicz-na-miejscu-wciaz-nie-ma-policji/225389" hreflang="pl">TV Republika · 15:46</a></li>
        <li><a href="https://wiadomosci.onet.pl/krakow/strzelanina-w-krakowie-najnowsze-informacje-relacja/p16e8gh" hreflang="pl">$live</a></li>
      </ul>
      <h3>$screens</h3>
      <div class="media">
        $images
      </div>
    </section>
  </main>
  <footer>
    <div class="wrap">
      <span>$author</span>
      <a href="$repo_url">$repo</a>
    </div>
  </footer>
</body>
</html>
""")


def language_path(code):
    return "" if code == "pl" else f"{code}/"


def format_date(value, code):
    month = MONTHS[code].split()[value.month - 1]
    return f"{value.day} {month} {value.year}"


def build():
    with (ROOT / "content.toml").open("rb") as file:
        content = tomllib.load(file)

    as_of_iso = content.pop("as_of_iso", None)
    try:
        as_of = date.fromisoformat(as_of_iso)
    except (TypeError, ValueError):
        raise ValueError("as_of_iso must be a valid date string in YYYY-MM-DD format") from None
    if as_of.isoformat() != as_of_iso:
        raise ValueError("as_of_iso must use YYYY-MM-DD")

    for code in LANGUAGES:
        expected = format_date(as_of, code)
        if content.get(code, {}).get("as_of") != expected:
            raise ValueError(
                f"{code}.as_of must be {expected!r} to match as_of_iso={as_of_iso}"
            )

    alternates = "\n  ".join(
        f'<link rel="alternate" hreflang="{code}" href="{URL}{language_path(code)}">'
        for code in LANGUAGES
    ) + f'\n  <link rel="alternate" hreflang="x-default" href="{URL}">'

    pages = {}
    for code in LANGUAGES:
        translations = content[code]
        base = "./" if code == "pl" else "../"
        links = []
        for target, name in LANGUAGES.items():
            current = ' aria-current="page"' if code == target else ""
            links.append(
                f'<a href="{base}{language_path(target)}" lang="{target}" '
                f'hreflang="{target}"{current}>{name}</a>'
            )

        images = []
        for index, label in enumerate(translations["captions"], start=1):
            src = f"{base}assets/{index:02}.webp"
            caption = escape(label)
            images.append(
                f'<figure><a href="{src}"><img src="{src}" alt="{caption}" '
                f'width="1348" height="926" loading="lazy"></a>'
                f'<figcaption>{caption}</figcaption></figure>'
            )

        labels = {key: escape(value) for key, value in translations.items() if key != "captions"}
        events = "\n".join(
            EVENT.substitute(
                day=timestamp.date().isoformat(), slug=slug, timestamp=timestamp.isoformat(),
                label=format_date(timestamp.date(), code), title=labels[title], note=labels[note],
            )
            for timestamp, slug, title, note in EVENTS
        )
        path = SITE / language_path(code) / "index.html"
        pages[path] = PAGE.substitute(
            labels, lang=code, base=base, url=URL + language_path(code),
            repo_url=REPO, alternates=alternates, as_of_iso=as_of_iso,
            language_links="\n        ".join(links), images="\n        ".join(images), events=events,
        )

    for path, html in pages.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    build()
