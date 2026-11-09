"""Generate the five static language editions for GitHub Pages."""
from html import escape
from pathlib import Path
from string import Template
from urllib.parse import urlsplit
import re
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
        <div><dt>$updated</dt><dd><time datetime="2026-11-09">$as_of</time></dd></div>
      </dl>
    </section>
$subscribe
    <section class="card" id="chronologia">
      <h2>$timeline</h2>
      <ol class="timeline">
        <li id="2026-11-07-odbior">
          <time class="date" datetime="2026-11-07T18:23:51+01:00">$date</time>
          <div><h3>$delivered</h3><p>$delivery_note</p></div>
        </li>
        <li id="2026-11-07-nadanie">
          <time class="date" datetime="2026-11-07T18:23:49+01:00">$date</time>
          <div><h3>$sent</h3><p>$sent_note</p></div>
        </li>
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
      <a href="./privacy.html">$privacy_title</a>
      <a href="$repo_url">$repo</a>
    </div>
  </footer>
</body>
</html>
""")

SUBSCRIBE = Template("""    <section class="card" id="subskrypcja">
      <h2>$subscription_title</h2>
      <p>$subscribe_intro</p>
      <p class="signup-actions"><a class="signup-button" href="$form_url" rel="noreferrer">$subscribe_action</a> <a href="./privacy.html#newsletter">$privacy_title</a></p>
    </section>""")

PRIVACY = Template("""<!doctype html>
<html lang="$lang">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>$privacy_title | $brand</title>
  <link rel="canonical" href="${url}privacy.html">
  $alternates
  <link rel="stylesheet" href="${base}assets/style.css">
</head>
<body>
  <header class="top">
    <div class="wrap">
      <a class="brand" href="./">$brand</a>
      <nav aria-label="$language_label">
        $language_links
      </nav>
    </div>
  </header>
  <main class="wrap">
    <article class="card document">
      <h1>$privacy_title</h1>
      <p class="date">$policy_date</p>
      <p>$controller</p>
      <p>$privacy_contact</p>
      <h2>$hosting_title</h2>
      <p>$hosting_note</p>
      <p>$cookies_note</p>
      <p><a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">$github_policy</a></p>
$newsletter_policy
      <h2>$correspondence_title</h2>
      <p>$correspondence_note</p>
      <p><a href="https://policies.google.com/privacy">$google_policy</a></p>
      <h2>$rights_title</h2>
      <p>$rights_note</p>
      <p><a href="https://www.uodo.gov.pl/526">$complaint</a></p>
    </article>
  </main>
</body>
</html>
""")

NEWSLETTER_POLICY = Template("""      <section id="newsletter">
        <h2>$subscription_title</h2>
        <p>$subscription_data</p>
        <p>$subscription_provider</p>
        <p><a href="https://www.beehiiv.com/dpa">beehiiv · Data Protection Addendum</a> · <a href="https://www.beehiiv.com/privacy">$beehiiv_policy</a></p>
        <p>$subscription_retention</p>
      </section>""")


def language_path(code):
    return "" if code == "pl" else f"{code}/"


def alternate_links(page=""):
    return "\n  ".join(
        f'<link rel="alternate" hreflang="{code}" href="{URL}{language_path(code)}{page}">'
        for code in LANGUAGES
    ) + f'\n  <link rel="alternate" hreflang="x-default" href="{URL}{page}">'


def language_links(code, base, page=""):
    links = []
    for target, name in LANGUAGES.items():
        current = ' aria-current="page"' if code == target else ""
        links.append(
            f'<a href="{base}{language_path(target)}{page}" lang="{target}" '
            f'hreflang="{target}"{current}>{name}</a>'
        )
    return "\n        ".join(links)


def subscription_settings(settings):
    email = settings["contact_email"].strip()
    url = settings["beehiiv_form_url"].strip()
    if email and not re.fullmatch(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", email, re.ASCII):
        raise ValueError("Set contact_email to a public contact email address.")
    if url:
        form = urlsplit(url)
        if (form.scheme != "https" or not form.hostname
                or not form.hostname.endswith(".beehiiv.com")
                or form.username or form.password or form.port is not None
                or form.path not in ("", "/", "/subscribe", "/subscribe/")
                or form.query or form.fragment or re.search(r"\s", url)):
            raise ValueError("Set beehiiv_form_url to the public HTTPS signup URL from beehiiv.")
        if not email:
            raise ValueError("A public contact_email is required to enable subscriptions.")
    return email, url


def build():
    with (ROOT / "content.toml").open("rb") as file:
        content = tomllib.load(file)
    with (ROOT / "privacy.toml").open("rb") as file:
        privacy = tomllib.load(file)
    email, form_url = subscription_settings(privacy["settings"])

    for code, translations in content.items():
        base = "./" if code == "pl" else "../"

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
        policy = {key: escape(value) for key, value in privacy[code].items()}
        page_url = URL + language_path(code)
        directory = SITE / language_path(code)
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "index.html").write_text(PAGE.substitute(
            labels, lang=code, base=base, url=page_url,
            repo_url=REPO, alternates=alternate_links(),
            language_links=language_links(code, base), images="\n        ".join(images),
            privacy_title=policy["privacy_title"],
            subscribe=SUBSCRIBE.substitute(policy, form_url=escape(form_url)) if form_url else "",
        ), encoding="utf-8")
        contact = (
            f'{policy["email_label"]} · <a href="mailto:{escape(email)}">{escape(email)}</a>'
            if email else f'<a href="https://github.com/sobolevbel">{policy["profile_contact"]}</a>'
        )
        (directory / "privacy.html").write_text(PRIVACY.substitute(
            policy, lang=code, base=base, url=page_url,
            brand=labels["brand"], language_label=labels["language_label"],
            alternates=alternate_links("privacy.html"),
            language_links=language_links(code, base, "privacy.html"),
            privacy_contact=contact,
            newsletter_policy=NEWSLETTER_POLICY.substitute(policy) if form_url else "",
        ), encoding="utf-8")


if __name__ == "__main__":
    build()
