# Pluto BV Services — Image System

## How to replace a placeholder with a real photo

1. Add the real file to the matching folder, e.g. `/images/services/pluto-live-in-care-01.jpg`
   (use descriptive filenames — never `IMG_1234.jpg`).
2. Open `image-config.json` and edit that one entry:
   - `src` → the new file path
   - `alt` → a real, descriptive sentence (never "photo" / "care image")
   - `decorative` → set `false` if it's meaningful, leave `true` only for
     purely atmospheric CTA-band imagery
   - `objectPosition` → adjust if a face/subject needs recentring under crop
   - `widths` → the resolutions you actually have, if you're providing more
     than one size (see "Multiple resolutions" below)
3. From the project root, run:
   ```
   python3 build_images.py
   ```
   This regenerates the `<picture>`/`<img>` markup for every page from the
   config. No HTML file is ever hand-edited.
4. Re-deploy the static files.

No component/page markup needs to change — the config is the only file you touch.

## Multiple resolutions / modern formats (when real photography arrives)

`render_picture()` in `build_images.py` is the single place image markup is
produced. Once real photos exist in more than one size/format, extend it to
emit `<source type="image/avif" srcset="...">` / `<source type="image/webp" ...>`
before the fallback `<img>`, using the `widths` list already present in each
config entry. The `<picture>` wrapper is already in place on every image on
the site specifically so this upgrade requires no HTML changes — only an
edit to `render_picture()` and a re-run of `build_images.py`.

## Decorative vs. meaningful images

`"decorative": true` → rendered with `alt=""` (screen readers skip it).
`"decorative": false` → rendered with the real `alt` text in the config.

## Current state

Every image on the site is currently `/images/placeholders/*.svg` — branded
abstract artwork (not stock photography, not real Pluto photos). They are
intentionally illustrative so nothing looks broken, and nothing pretends to
be a real client, employee, or Pluto location.
