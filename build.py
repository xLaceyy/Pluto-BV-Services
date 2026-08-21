import os

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV_ITEMS = [
    ("about",    "About",     "/about.html"),
    ("care",     "Care",      "/care.html"),
    ("staffing", "Staffing",  "/staffing.html"),
    ("expect",   "What You Can Expect", "/what-we-expect.html"),
    ("stories",  "Stories",   "/stories.html"),
    ("portal",   "Staff Portal", "/staff-portal.html"),
    ("contact",  "Contact",   "/contact.html"),
]

CARE_DROPDOWN = [
    ("Live-in Care", "/services/live-in-care.html"),
    ("Domiciliary Care", "/services/domiciliary-care.html"),
    ("Companionship Care", "/services/companionship-care.html"),
    ("Autism & Specialist Support", "/services/autism-support.html"),
]


def nav_html(active_key):
    links = []
    for key, label, href in NAV_ITEMS:
        cls = "magnetic active-link" if key == active_key else "magnetic"
        links.append('<li><a href="%s" class="%s">%s <span class="nav-indicator"></span></a></li>' % (href, cls, label))
    nav_links = "".join(links)

    mnav_links = []
    for key, label, href in NAV_ITEMS:
        cls = ' class="active-link"' if key == active_key else ""
        mnav_links.append('<li><a href="%s"%s>%s</a></li>' % (href, cls, label))
    mnav_html = "".join(mnav_links)

    return """
  <nav class="nav" id="nav">
    <a href="/index.html" class="nav-brand">
      <span class="logo-main">PLUTO</span>
      <span class="logo-sub">BVLTD</span>
      <span class="logo-tagline">CARE.PURPOSE.TRUST.</span>
    </a>
    <ul class="nav-links">%s</ul>
    <div class="nav-cta">
      <a href="tel:01604630916" class="nav-icon-btn magnetic" aria-label="Call Pluto" title="01604 630 916">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
      </a>
      <button class="nav-toggle" id="mnavOpen" aria-label="Open menu"><span></span></button>
    </div>
  </nav>

  <div class="mnav" id="mnav">
    <button class="mnav-close" id="mnavClose" aria-label="Close menu">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M18 6 6 18M6 6l12 12"/></svg>
    </button>
    <ul>%s</ul>
    <div class="mnav-foot">
      <span>01604 630 916</span>
      <span>admin@plutobvservices.co.uk</span>
      <span>3 Spencer Parade, Northampton, NN1 5AA</span>
    </div>
  </div>
""" % (nav_links, mnav_html)


def footer_html():
    return """
  <footer>
    <div class="wrap">
      <div class="foot-top">
        <div>
          <div class="foot-brand">
            <span class="logo-main">PLUTO</span>
            <span class="logo-sub">BVLTD</span>
            <span class="logo-tagline">CARE.PURPOSE.TRUST.</span>
          </div>
          <p class="foot-desc">Recruitment of temporary and permanent social care professionals for local authorities, the NHS and private residential homes — and direct care support for individuals and families.</p>
        </div>
        <div class="foot-col">
          <h5>Care Services</h5>
          <ul>
            <li><a href="/services/live-in-care.html">Live-in Care</a></li>
            <li><a href="/services/domiciliary-care.html">Domiciliary Care</a></li>
            <li><a href="/services/companionship-care.html">Companionship Care</a></li>
            <li><a href="/services/autism-support.html">Autism &amp; Specialist Support</a></li>
          </ul>
        </div>
        <div class="foot-col">
          <h5>Company</h5>
          <ul>
            <li><a href="/about.html">About</a></li>
            <li><a href="/staffing.html">Staffing</a></li>
            <li><a href="/what-we-expect.html">What You Can Expect</a></li>
            <li><a href="/staff-portal.html">Careers</a></li>
            <li><a href="/stories.html">Stories</a></li>
          </ul>
        </div>
        <div class="foot-col">
          <h5>Contact</h5>
          <ul>
            <li><a href="tel:01604630916">01604 630 916</a></li>
            <li><a href="mailto:admin@plutobvservices.co.uk">admin@plutobvservices.co.uk</a></li>
            <li>3 Spencer Parade, Northampton, NN1 5AA</li>
          </ul>
        </div>
      </div>
      <div class="foot-bottom">
        <p>&copy; 2026 Pluto BV Ltd. All rights reserved.</p>
        <div class="foot-legal">
          <a href="/contact.html#legal-privacy">Privacy Policy</a>
          <a href="/contact.html#legal-terms">Terms</a>
          <a href="/contact.html#legal-cookies">Cookies</a>
        </div>
      </div>
    </div>
  </footer>
"""


SVG_DEFS = """
  <a class="skip-link" href="#main">Skip to main content</a>
  <div class="grid-lines"></div>
  <div class="grain"></div>
  <div class="cursor" id="cursor"><span class="label" id="cursorLabel">Explore</span></div>
  <div class="scroll-progress" id="scrollProgress"></div>

  <div class="orb orb-1"></div>
  <div class="orb orb-2"></div>
  <div class="orb orb-3"></div>

  <svg class="svg-defs" style="position:absolute;width:0;height:0;overflow:hidden;" aria-hidden="true">
    <defs>
      <linearGradient id="pGradPrimary" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#E7DBFF" />
        <stop offset="45%" stop-color="#B088D4" />
        <stop offset="100%" stop-color="#6B3F8A" />
      </linearGradient>
      <linearGradient id="pGradGhost" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#ffffff" stop-opacity="0.8" />
        <stop offset="100%" stop-color="#B088D4" stop-opacity="0.15" />
      </linearGradient>
      <mask id="pMask" maskUnits="objectBoundingBox" maskContentUnits="userSpaceOnUse">
        <rect x="0" y="0" width="200" height="260" fill="black" />
        <rect x="34" y="18" width="46" height="224" rx="15" fill="white" />
        <rect x="34" y="18" width="142" height="114" rx="40" fill="white" />
        <rect x="77" y="51" width="65" height="48" rx="21" fill="black" />
      </mask>
      <symbol id="plutoP" viewBox="0 0 200 260">
        <rect x="0" y="0" width="200" height="260" fill="url(#pGradPrimary)" mask="url(#pMask)" />
        <rect x="0" y="0" width="90" height="260" fill="#fff" opacity="0.08" mask="url(#pMask)" />
      </symbol>
      <symbol id="plutoPGhost" viewBox="0 0 200 260">
        <rect x="0" y="0" width="200" height="260" fill="url(#pGradGhost)" mask="url(#pMask)" />
      </symbol>
      <filter id="softGlow" x="-60%" y="-60%" width="220%" height="220%">
        <feGaussianBlur stdDeviation="16" result="blur" />
        <feMerge>
          <feMergeNode in="blur" />
          <feMergeNode in="SourceGraphic" />
        </feMerge>
      </filter>
    </defs>
  </svg>
"""

PAGE_TEMPLATE = """<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <title>%(title)s</title>
  <meta name="description" content="%(description)s" />
  <link rel="canonical" href="https://plutobvltd.com%(canonical)s" />
  <meta property="og:title" content="%(title)s" />
  <meta property="og:description" content="%(description)s" />
  <meta property="og:type" content="website" />
  <meta name="theme-color" content="#6A4694" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300..700&family=Syne:wght@400..800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="%(css_path)sassets/css/styles.css" />

  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>
</head>
<body>
%(svg_defs)s
%(nav)s
  <main id="main">
%(content)s
  </main>
%(footer)s
  <script src="%(css_path)sassets/js/main.js"></script>
  <script src="%(css_path)sassets/js/navigation.js"></script>
  <script src="%(css_path)sassets/js/animations.js"></script>
%(extra_js)s
</body>
</html>
"""


def page(path, title, description, content, active_key, extra_js=""):
    depth = path.count("/") - 1
    css_path = "../" * depth if depth > 0 else ""
    html = PAGE_TEMPLATE % {
        "title": title,
        "description": description,
        "canonical": path,
        "css_path": css_path,
        "svg_defs": SVG_DEFS,
        "nav": nav_html(active_key),
        "content": content,
        "footer": footer_html(),
        "extra_js": extra_js,
    }
    full_path = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)


IMG = {
    "hero": "/assets/images/carer-helping-stand.jpg",
    "about": "/assets/images/team-purple-uniforms.jpg",
    "about2": "/assets/images/about-team.jpg",
    "livein": "/assets/images/live-in-care.jpg",
    "domiciliary": "/assets/images/domiciliary-care.jpg",
    "companionship": "/assets/images/companionship-care.jpg",
    "autism": "/assets/images/team-bench.jpg",
    "staffing": "/assets/images/staffing-office.jpg",
    "staffing2": "/assets/images/staffing-consult.jpg",
    "careers": "/assets/images/team-walking.jpg",
    "companions": "/assets/images/companions-laundry.jpg",
    "nurse_table": "/assets/images/nurse-elderly-table.jpg",
    "news": "/assets/images/news-family.jpg",
}
print("build.py loaded")