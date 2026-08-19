# -*- coding: utf-8 -*-
"""
build_images.py — the reusable "ResponsiveImage" component for this project.

This project is plain static HTML (no React/build framework), so the brief's
JSX <ResponsiveImage/> is adapted as a build-time Python renderer reading the
same central config (/images/image-config.json). Pages are generated with the
correct final markup already in place (no client-side image-swap JS), which:
  - keeps the hero eligible for real LCP/fetchpriority optimisation
  - keeps alt text and <img> tags visible to crawlers/screen readers immediately
  - avoids layout shift / flash-of-placeholder that a runtime swap would cause

HOW TO REPLACE A PLACEHOLDER WITH A REAL PHOTO:
  1. Add the real file under /images/<category>/ (e.g. /images/services/pluto-live-in-care-01.jpg)
  2. Edit the matching entry in /images/image-config.json (src / alt / objectPosition / widths)
  3. Run:  python3 build_images.py
  4. Re-run generate_placeholders.py only if you want to regenerate placeholder artwork itself.
No HTML file is ever hand-edited — the config is the only thing that changes.
"""
import json, re, os

BASE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE, "images", "image-config.json"), encoding="utf-8") as f:
    CONFIG = json.load(f)
CONFIG.pop("_readme", None)

def get(key):
    node = CONFIG
    for part in key.split("."):
        node = node[part]
    return node

# ---------------------------------------------------------------------------
# The reusable component: one image, in, one <picture> markup, out.
# ---------------------------------------------------------------------------
def render_picture(key, sizes="(max-width: 768px) 100vw, 50vw", loading="lazy", fetchpriority=None):
    data = get(key)
    alt = "" if data.get("decorative") else data.get("alt", "")
    style = ""
    if data.get("objectPosition"):
        style = ' style="object-position:' + data["objectPosition"] + '"'
    attrs = ' loading="' + loading + '" decoding="async"'
    if fetchpriority:
        attrs += ' fetchpriority="' + fetchpriority + '"'
    # <picture> is included now (ready for future <source type="image/avif|webp">
    # once real, multi-format photography exists) even though today's placeholder
    # is a single SVG and needs no extra <source> yet.
    img = ('<img class="pluto-img" data-img-key="' + key + '" src="' + data["src"] + '" '
           'sizes="' + sizes + '" alt="' + alt + '"' + style + attrs + '>')
    return '<picture data-img-key="' + key + '">' + img + '</picture>'

# ---------------------------------------------------------------------------
# Migration: replace each existing `<div class="photo-placeholder">…</div>`
# (in document order) with the rendered component for the mapped config key.
# This is a one-time structural migration; after this run, editing images is
# just: change image-config.json -> rerun this script.
# ---------------------------------------------------------------------------
PLACEHOLDER_RE = re.compile(r'<div class="photo-placeholder">.*?</div>', re.S)

PAGE_MAPPINGS = {
    "index.html": [
        ("hero", dict(loading="eager", fetchpriority="high", sizes="(max-width: 1024px) 100vw, 50vw")),
        ("about.main", dict()),
        ("services.liveInCare.card", dict(sizes="(max-width: 768px) 100vw, 25vw")),
        ("services.domiciliaryCare.card", dict(sizes="(max-width: 768px) 100vw, 25vw")),
        ("services.companionship.card", dict(sizes="(max-width: 768px) 100vw, 25vw")),
        ("services.specialistSupport.card", dict(sizes="(max-width: 768px) 100vw, 25vw")),
        ("organisations.hero", dict()),
        ("careers.hero", dict()),
    ],
    "about.html": [
        ("about.main", dict(loading="eager")),
        ("about.team", dict()),
    ],
    "resources.html": [
        ("stories.hero", dict(loading="eager")),
        ("stories.card1", dict(sizes="(max-width: 768px) 100vw, 25vw")),
        ("stories.card2", dict(sizes="(max-width: 768px) 100vw, 25vw")),
        ("stories.card3", dict(sizes="(max-width: 768px) 100vw, 25vw")),
        ("stories.card4", dict(sizes="(max-width: 768px) 100vw, 25vw")),
    ],
    "staffing-solutions.html": [
        ("organisations.hero", dict(loading="eager")),
    ],
    "areas-we-support.html": [
        ("areasWeSupport.hero", dict(loading="eager")),
        ("areasWeSupport.secondary", dict()),
    ],
    os.path.join("care-services", "index.html"): [
        ("services.liveInCare.card", dict(sizes="(max-width: 768px) 100vw, 25vw")),
        ("services.domiciliaryCare.card", dict(sizes="(max-width: 768px) 100vw, 25vw")),
        ("services.companionship.card", dict(sizes="(max-width: 768px) 100vw, 25vw")),
        ("services.specialistSupport.card", dict(sizes="(max-width: 768px) 100vw, 25vw")),
    ],
    os.path.join("care-services", "live-in-care.html"): [
        ("services.liveInCare.hero", dict(loading="eager", fetchpriority="high")),
        ("services.liveInCare.lifestyle", dict()),
        ("services.liveInCare.detail", dict()),
        ("services.liveInCare.cta", dict()),
    ],
    os.path.join("care-services", "domiciliary-care.html"): [
        ("services.domiciliaryCare.hero", dict(loading="eager", fetchpriority="high")),
        ("services.domiciliaryCare.lifestyle", dict()),
        ("services.domiciliaryCare.detail", dict()),
        ("services.domiciliaryCare.cta", dict()),
    ],
    os.path.join("care-services", "companionship-care.html"): [
        ("services.companionship.hero", dict(loading="eager", fetchpriority="high")),
        ("services.companionship.lifestyle", dict()),
        ("services.companionship.detail", dict()),
        ("services.companionship.cta", dict()),
    ],
    os.path.join("care-services", "autism-specialist-support.html"): [
        ("services.specialistSupport.hero", dict(loading="eager", fetchpriority="high")),
        ("services.specialistSupport.lifestyle", dict()),
        ("services.specialistSupport.detail", dict()),
        ("services.specialistSupport.cta", dict()),
    ],
}

def migrate_file(path, mapping):
    full = os.path.join(BASE, path)
    with open(full, encoding="utf-8") as f:
        content = f.read()

    matches = list(PLACEHOLDER_RE.finditer(content))
    if len(matches) != len(mapping):
        print("SKIP (count mismatch %d found vs %d mapped): %s" % (len(matches), len(mapping), path))
        return 0

    # Build replacements in order, then splice from the end so earlier offsets stay valid.
    replacements = [render_picture(key, **opts) for key, opts in mapping]
    for m, repl in reversed(list(zip(matches, replacements))):
        content = content[:m.start()] + repl + content[m.end():]

    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return len(matches)

if __name__ == "__main__":
    total = 0
    for path, mapping in PAGE_MAPPINGS.items():
        total += migrate_file(path, mapping)
    print("TOTAL images wired to central config:", total)
