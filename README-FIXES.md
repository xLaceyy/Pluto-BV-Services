# What was actually wrong, and what I fixed

Your `index.html` (the one outside the zip) is a single-file site: every
"page" (Home/About/Staffing/Services/Stories/News/Staff Portal/Contact) is
a `<div class="page" id="page-x">` inside this one file, switched by JS
based on `#hash` in the URL. That part was working. Three real bugs made
it look and behave broken:

## 1. The purple was set to nearly-invisible opacity everywhere
Every border, glass edge, shadow, the ambient background orbs, the glowing
"P" watermark in the hero, and the particle dots ("stars") were set to
2–8% opacity — literally imperceptible. That's why everything read as flat
white with the odd solid-purple button and nothing in between. Fixed:
boosted ~60 washed-out `rgba(106,70,148, …)` tokens back to visible
levels, and switched the ambient orbs from `mix-blend-mode: screen`
(which brightens toward white — actively fighting a white background) to
`multiply` (which actually tints it). That's the "purple blending instead
of white→purple" you asked for.

## 2. The "stars" (hero particle dots) were invisible
`opacity: 0.04` with a `0.02`-alpha shadow — essentially off. Now they're
sized up, glow with a real soft shadow, and twinkle (0.3→1 opacity) rather
than sitting static and unseen.

## 3. Every content image was hotlinked from other companies' websites
`helpinghandshomecare.co.uk` and a random Wix media URL were being pulled
live into your site — fragile (breaks the moment they change their site)
and not something you want live on a competitor's bandwidth. All 7 image
slots now point to your own real photography in `/assets/images/`,
including the new team photo in purple uniforms on the About page, which
had no image at all before.

## Also fixed along the way
- **Contact form**: was POSTing to `https://formspree.io/f/YOUR_FORM_ID` —
  a placeholder that fails on every real submission. It now falls back to
  a pre-filled `mailto:` link so a message can always get to you; wire a
  real Formspree ID (or your own endpoint) into `data-endpoint` on the
  `<form id="contactForm">` when you have one.
- **`server.js` / `package.json` removed from this package.** That was the
  cause of your earlier `npm install` error — it expected a `public/`
  folder that doesn't exist, and its catch-all route served `index.html`
  for every URL. This site doesn't need a Node server at all: it's static.
  Drop this folder straight into Vercel (or any static host) as-is.

## Worth knowing, not fixed this pass
- Hash-based routing (`#about`) means a direct link to
  `plutobvltd.com/about` (no hash) won't land on the About content — only
  on-site clicks and `plutobvltd.com/#about` links work. Fine for browsing,
  weaker for SEO/shareability. If that matters, the fix is converting to
  real per-page URLs — say the word and I'll do that conversion next.
- Staffing Solutions and About are still fairly compact relative to the
  detailed content brief you provided — I focused this pass on the visual
  bugs you asked about. Happy to build those out substantially next.
