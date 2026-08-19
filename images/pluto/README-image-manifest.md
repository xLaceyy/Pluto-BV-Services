# Pluto BV Services — image manifest

All photography on the homepage lives in `/images/pluto/` and is referenced by
these exact filenames. **To replace a placeholder with real Pluto photography,
drop a same-name file into this folder** — no HTML/CSS edits needed.

| Filename | Used for | Used in `index.html` |
|---|---|---|
| `pluto-caregiver-supporting-client-at-home.jpg` | Hero background | `.hero-bg` (line ~1600) |
| `pluto-family-in-living-room.jpg` | "Care & Support" audience card | `.people-card` (Families) |
| `pluto-care-home-manager-and-staff.jpg` | "Staffing Solutions" audience card | `.people-card` (Organisations) |
| `pluto-healthcare-professional-portrait.jpg` | "Careers" audience card | `.people-card` (Professionals) |
| `pluto-live-in-care-companion.jpg` | Live-in Care service icon | `.service-icon-img` |
| `pluto-domiciliary-care-visit.jpg` | Domiciliary Care service icon | `.service-icon-img` |
| `pluto-companionship-care-conversation.jpg` | Companionship Care service icon | `.service-icon-img` |
| `pluto-autism-specialist-support.jpg` | Autism & Specialist Support icon | `.service-icon-img` |
| `pluto-staffing-office-consultation.jpg` | Staffing Solutions section background | `.trust` section CSS `background` |
| `pluto-contact-northampton-office.jpg` | Contact / final CTA section background | `.contact`/CTA section CSS `background` |

## Status
All ten files are currently **generated placeholders** (gradient art, labelled
in the corner) — not stock photography and not real Pluto staff or clients.
Replace them with genuine, consented photography as soon as it's available;
until then nothing here should be captioned or implied as a real person.

## Notes for real photography
- Recommended minimum: 1800×1200 for the hero, 900×700 for people cards,
  480×480 for service icons (displayed at 240×240, 2x for retina).
- Keep faces roughly centred — cards crop with `object-fit: cover` and will
  clip the edges on narrow viewports.
- Compress before adding (target &lt;300KB per photo) — nothing here should
  ship multi-MB images to mobile.
