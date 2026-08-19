# -*- coding: utf-8 -*-
"""Generates branded abstract SVG placeholder artwork for Pluto BV Services.
Each is 800x600, purple/lavender gradient family, a distinct restrained
abstract motif per category, subtle grain, and a small corner monogram
so it reads as intentional artwork rather than a broken image or a fake photo.
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "placeholders")
os.makedirs(OUT, exist_ok=True)

DEFS = """
<defs>
  <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#4E2278"/>
    <stop offset="52%" stop-color="#5B2A86"/>
    <stop offset="100%" stop-color="#8A5CC4"/>
  </linearGradient>
  <radialGradient id="glow1" cx="22%" cy="18%" r="55%">
    <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.30"/>
    <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="glow2" cx="85%" cy="88%" r="55%">
    <stop offset="0%" stop-color="#7C4DFF" stop-opacity="0.35"/>
    <stop offset="100%" stop-color="#7C4DFF" stop-opacity="0"/>
  </radialGradient>
  <filter id="soft" x="-40%" y="-40%" width="180%" height="180%">
    <feGaussianBlur stdDeviation="26"/>
  </filter>
  <filter id="grain">
    <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.02 0"/>
  </filter>
</defs>
<rect width="800" height="600" fill="url(#g)"/>
<rect width="800" height="600" fill="url(#glow1)"/>
<rect width="800" height="600" fill="url(#glow2)"/>
"""

GRAIN = '<rect width="800" height="600" filter="url(#grain)"/>'

MARK = """
<g opacity="0.55" transform="translate(736,548)">
  <rect x="0" y="0" width="20" height="20" rx="6" fill="#FFFFFF" fill-opacity="0.16"/>
  <circle cx="10" cy="10" r="4.4" fill="#FFFFFF"/>
</g>
"""

def wrap(shapes, name):
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" role="img" aria-hidden="true">'
           + DEFS + shapes + GRAIN + MARK + '</svg>')
    with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", name + ".svg")

# ---- hero: arched doorway + warm glow (home / welcome) ----
wrap('<circle cx="600" cy="150" r="150" fill="#FFFFFF" fill-opacity="0.10" filter="url(#soft)"/>'
     '<path d="M300 560 V330 a140 140 0 0 1 280 0 V560 Z" fill="#FFFFFF" fill-opacity="0.14"/>'
     '<path d="M300 560 V330 a140 140 0 0 1 280 0 V560" fill="none" stroke="#FFFFFF" stroke-opacity="0.35" stroke-width="3"/>',
     "hero")

# ---- about: single soft organic figure form ----
wrap('<ellipse cx="400" cy="230" rx="95" ry="105" fill="#FFFFFF" fill-opacity="0.16" filter="url(#soft)"/>'
     '<path d="M250 560 C250 420 320 360 400 360 C480 360 550 420 550 560 Z" fill="#FFFFFF" fill-opacity="0.14"/>',
     "about")

# ---- live-in care: doorway motif (reuse hero language, smaller) ----
wrap('<path d="M320 560 V360 a80 80 0 0 1 160 0 V560 Z" fill="#FFFFFF" fill-opacity="0.16"/>'
     '<path d="M320 560 V360 a80 80 0 0 1 160 0 V560" fill="none" stroke="#FFFFFF" stroke-opacity="0.4" stroke-width="3"/>'
     '<circle cx="600" cy="140" r="120" fill="#FFFFFF" fill-opacity="0.10" filter="url(#soft)"/>',
     "live-in-care")

# ---- domiciliary care: visiting route / path with a stop point ----
wrap('<path d="M120 500 C260 380 340 480 480 360 C560 290 620 320 690 220" fill="none" '
     'stroke="#FFFFFF" stroke-opacity="0.35" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 22"/>'
     '<circle cx="690" cy="220" r="14" fill="#FFFFFF" fill-opacity="0.65"/>'
     '<circle cx="120" cy="500" r="10" fill="#FFFFFF" fill-opacity="0.5"/>',
     "domiciliary-care")

# ---- companionship: two close overlapping soft forms ----
wrap('<circle cx="360" cy="300" r="130" fill="#FFFFFF" fill-opacity="0.14" filter="url(#soft)"/>'
     '<circle cx="470" cy="300" r="130" fill="#7C4DFF" fill-opacity="0.22" filter="url(#soft)"/>',
     "companionship")

# ---- specialist support: calm flowing infinity ribbon (neurodiversity-respectful, not a puzzle piece) ----
wrap('<path d="M260 300 a70 70 0 1 0 140 0 c30-70 90-70 140 0 a70 70 0 1 1-140 0 c-30 70-90 70-140 0Z" '
     'fill="none" stroke="#FFFFFF" stroke-opacity="0.5" stroke-width="10" stroke-linecap="round"/>',
     "specialist-support")

# ---- organisations / staffing: abstract network grid ----
wrap('<g fill="#FFFFFF" fill-opacity="0.16">'
     '<rect x="230" y="230" width="120" height="90" rx="14"/>'
     '<rect x="380" y="180" width="120" height="90" rx="14"/>'
     '<rect x="380" y="300" width="120" height="90" rx="14"/>'
     '<rect x="530" y="230" width="120" height="90" rx="14"/></g>'
     '<g stroke="#FFFFFF" stroke-opacity="0.3" stroke-width="2">'
     '<line x1="350" y1="275" x2="380" y2="225"/><line x1="350" y1="275" x2="380" y2="345"/>'
     '<line x1="500" y1="225" x2="530" y2="275"/><line x1="500" y1="345" x2="530" y2="275"/></g>',
     "organisations")

# ---- careers: ascending cluster of forms (growth / team) ----
wrap('<circle cx="290" cy="400" r="60" fill="#FFFFFF" fill-opacity="0.16"/>'
     '<circle cx="420" cy="330" r="72" fill="#FFFFFF" fill-opacity="0.18"/>'
     '<circle cx="560" cy="250" r="86" fill="#7C4DFF" fill-opacity="0.24"/>',
     "careers")

# ---- stories / resources: open page-fold abstraction ----
wrap('<path d="M180 240 L400 200 L400 460 L180 500 Z" fill="#FFFFFF" fill-opacity="0.14"/>'
     '<path d="M620 240 L400 200 L400 460 L620 500 Z" fill="#FFFFFF" fill-opacity="0.1"/>',
     "stories")

# ---- areas we support: radiating coverage from a pin ----
wrap('<circle cx="400" cy="320" r="60" fill="none" stroke="#FFFFFF" stroke-opacity="0.28" stroke-width="2"/>'
     '<circle cx="400" cy="320" r="110" fill="none" stroke="#FFFFFF" stroke-opacity="0.2" stroke-width="2"/>'
     '<circle cx="400" cy="320" r="160" fill="none" stroke="#FFFFFF" stroke-opacity="0.13" stroke-width="2"/>'
     '<circle cx="400" cy="320" r="12" fill="#FFFFFF" fill-opacity="0.7"/>',
     "areas")

# ---- contact: rounded speech bubble ----
wrap('<path d="M260 250 h280 a40 40 0 0 1 40 40 v120 a40 40 0 0 1-40 40 H360 l-60 60 v-60 h-40 '
     'a40 40 0 0 1-40-40 V290 a40 40 0 0 1 40-40Z" fill="#FFFFFF" fill-opacity="0.15"/>',
     "contact")

# ---- team: row of soft grouped forms ----
wrap('<circle cx="300" cy="330" r="70" fill="#FFFFFF" fill-opacity="0.15"/>'
     '<circle cx="420" cy="300" r="80" fill="#FFFFFF" fill-opacity="0.18"/>'
     '<circle cx="540" cy="330" r="70" fill="#7C4DFF" fill-opacity="0.22"/>',
     "team")

print("Done — 12 placeholder SVGs generated in", OUT)
