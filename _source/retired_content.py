"""Content withdrawn by the owner. Originals are backed up outside the website.

Proof pages (2026) and the wholesale catalogue route (retired 2026-10-29) must never be
published again. The only file allowed at the retired catalogue route is the redirect
stub written by build.py, which sends visitors to /request-a-quote/ (GitHub Pages does
not read the .htaccess 301 rules; the stub is what actually redirects on the live site)."""
from pathlib import Path

PROOF_STEMS = (
    "proof-co-form-vj",
    "proof-fumigation-2021",
    "proof-phytosanitary-specimen",
    "proof-surrendered-bl-2022",
)


REDIRECT_STUB = "wholesale-catalogue/index.html"


def is_retired_path(relative):
    value = str(relative).replace("\\", "/").strip("/")
    if value == REDIRECT_STUB:
        return False
    return (
        value == "wholesale-catalogue" or value.startswith("wholesale-catalogue/")
        or value == "proof" or value.startswith("proof/")
        or value == "assets/img/proof" or value.startswith("assets/img/proof/")
        or any(value.startswith("assets/img/webp/" + stem + "-png-")
               for stem in PROOF_STEMS)
    )


def assert_retired_files_absent(root):
    root = Path(root)
    found = [str(path.relative_to(root)) for path in root.rglob("*")
             if path.is_file() and is_retired_path(path.relative_to(root))]
    if found:
        raise ValueError("Retired files must stay outside the website: " + ", ".join(found))
