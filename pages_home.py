from build import IMG

def home():
    hero = """
    <section class="hero" id="hero">
      <img class="hero-bg" src="%s" alt="A carer supporting an elderly client at home" loading="eager" />
      <div class="hero-overlay"></div>
      <div class="hero-field">
        <div class="hero-p" id="heroP">
          <svg viewBox="0 0 200 260" style="filter:url(#softGlow)"><use href="#plutoP" /></svg>
        </div>
        <div class="hero-particles" id="heroParticles"></div>
      </div>
      <div class="wrap hero-inner">
        <div class="eyebrow hero-eyebrow reveal">
          <span>Social care recruitment &amp; support — Northampton</span>
          <span class="status-badge"><span class="pulse-dot"></span>24/7 On-Call</span>
        </div>
        <h1 class="hero-title reveal">PLUTO <span class="highlight">Care, elevated.</span></h1>
        <div class="hero-tagline reveal">Care, elevated.</div>
        <p class="hero-copy reveal">Pluto BV Ltd recruits and supplies social care professionals to the NHS, local authorities and residential homes — and supports people to live independently, on their own terms, at home.</p>
        <div class="hero-ctas reveal">
          <a href="/care.html" class="btn btn-primary magnetic">Explore Care <span class="arrow"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span></a>
          <a href="/contact.html" class="btn btn-ghost magnetic">Start a conversation <span class="arrow"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span></a>
        </div>
        <div class="hero-audience-links reveal">
          <a href="/care.html" class="btn btn-primary" style="padding:10px 20px;font-size:11.5px;">👨‍👩‍👧‍👦 Family Care</a>
          <a href="/staffing.html" class="btn btn-ghost" style="padding:10px 20px;font-size:11.5px;">🏢 Staffing</a>
          <a href="/staff-portal.html" class="btn btn-ghost" style="padding:10px 20px;font-size:11.5px;">👩‍⚕️ Apply</a>
        </div>
      </div>
      <div class="hero-audience">
        <span class="tag">Individuals &amp; Families</span>
        <span class="tag">NHS &amp; Care Organisations</span>
        <span class="tag">Care Professionals</span>
      </div>
      <div class="hero-scroll"><span>Scroll</span><span class="line"></span></div>
    </section>
""" % IMG["hero"]

    intro = """
    <section class="statement" id="intro">
      <div class="statement-p-bg"><svg viewBox="0 0 200 260"><use href="#plutoPGhost" /></svg></div>
      <div class="wrap statement-grid">
        <h2 class="statement-word">
          <span class="reveal">Care isn't</span>
          <span class="reveal">a service.</span>
          <span class="reveal">It's <em>a standard.</em></span>
        </h2>
        <div>
          <p class="statement-copy reveal">Pluto BV Ltd recruits temporary and permanent social care professionals for local authorities, the NHS and private residential homes — and provides care support directly to individuals and families who want to stay independent at home.</p>
          <p class="statement-copy reveal">Every professional we place is vetted first, because the people relying on them are often vulnerable adults and children.</p>
          <a href="/about.html" class="btn btn-ghost magnetic reveal" style="margin-top:8px;">More about Pluto <span class="arrow">→</span></a>
        </div>
      </div>
    </section>
"""

    people = """
    <section class="people pad-xl" id="people">
      <div class="wrap">
        <div class="people-head">
          <div class="eyebrow reveal">Who we're built for</div>
          <h2 class="reveal">Care built around people.</h2>
        </div>
        <div class="people-grid">
          <a href="/care.html" class="people-card reveal-scale" style="background-image:url('%s');">
            <div class="card-overlay"></div>
            <svg class="pmark" viewBox="0 0 200 260"><use href="#plutoP" /></svg>
            <div class="card-inner people-card-content">
              <div class="num">01 — INDIVIDUALS &amp; FAMILIES</div>
              <h3>Staying independent, at home.</h3>
              <p>Compassionate, one-to-one support for people who want to keep living life on their own terms.</p>
            </div>
          </a>
          <a href="/staffing.html" class="people-card reveal-scale" style="background-image:url('%s');">
            <div class="card-overlay"></div>
            <svg class="pmark" viewBox="0 0 200 260"><use href="#plutoP" /></svg>
            <div class="card-inner people-card-content">
              <div class="num">02 — NHS &amp; CARE ORGANISATIONS</div>
              <h3>People they can trust.</h3>
              <p>Vetted, dependable social care professionals for local authorities, the NHS and private residential homes.</p>
            </div>
          </a>
          <a href="/staff-portal.html" class="people-card reveal-scale" style="background-image:url('%s');">
            <div class="card-overlay"></div>
            <svg class="pmark" viewBox="0 0 200 260"><use href="#plutoP" /></svg>
            <div class="card-inner people-card-content">
              <div class="num">03 — CARE PROFESSIONALS</div>
              <h3>A career that matters.</h3>
              <p>Temporary and permanent placements across the NHS, local authorities and residential homes.</p>
            </div>
          </a>
        </div>
      </div>
    </section>
""" % (IMG["companions"], IMG["staffing"], IMG["careers"])

    services = """
    <section class="services pad-xl" id="services">
      <div class="wrap">
        <div class="services-head">
          <h2 class="reveal">Support that meets people where they are.</h2>
          <p class="reveal">Four ways we help people stay independent, connected and well supported.</p>
        </div>
        <div class="services-list">
          <a href="/services/live-in-care.html" class="service-row reveal">
            <div class="row-bg"></div>
            <div class="service-num">01</div>
            <div class="service-name"><img class="service-icon-img" src="%s" alt="" loading="lazy" />Live-in Care</div>
            <div class="service-desc">Round-the-clock support in the comfort of your own home.</div>
            <span class="service-cta">Explore →</span>
          </a>
          <a href="/services/domiciliary-care.html" class="service-row reveal">
            <div class="row-bg"></div>
            <div class="service-num">02</div>
            <div class="service-name"><img class="service-icon-img" src="%s" alt="" loading="lazy" />Domiciliary Care</div>
            <div class="service-desc">Support with daily activities and household tasks for people who live independently.</div>
            <span class="service-cta">Explore →</span>
          </a>
          <a href="/services/companionship-care.html" class="service-row reveal">
            <div class="row-bg"></div>
            <div class="service-num">03</div>
            <div class="service-name"><img class="service-icon-img" src="%s" alt="" loading="lazy" />Companionship Care</div>
            <div class="service-desc">Because nobody should feel alone — conversation, activities and consistent connection.</div>
            <span class="service-cta">Explore →</span>
          </a>
          <a href="/services/autism-support.html" class="service-row reveal">
            <div class="row-bg"></div>
            <div class="service-num">04</div>
            <div class="service-name"><img class="service-icon-img" src="%s" alt="" loading="lazy" />Autism &amp; Specialist Support</div>
            <div class="service-desc">Person-centred support for individuals with autism and complex needs.</div>
            <span class="service-cta">Explore →</span>
          </a>
        </div>
      </div>
    </section>
""" % (IMG["livein"], IMG["domiciliary"], IMG["companionship"], IMG["autism"])

    staffing_teaser = """
    <section class="trust" id="staffing-teaser">
      <div class="wrap">
        <div class="trust-head">
          <div class="eyebrow reveal" style="justify-content:center;">For care organisations</div>
          <h2 class="reveal">Reliable people, for the teams that need them.</h2>
        </div>
        <div class="trust-orgs">
          <div class="org-chip reveal-scale">Local Authorities</div>
          <div class="org-chip reveal-scale">NHS &amp; Healthcare</div>
          <div class="org-chip reveal-scale">Residential Care Homes</div>
          <div class="org-chip reveal-scale">Private Organisations</div>
        </div>
        <div class="trust-stats">
          <div class="stat reveal"><div class="num" data-count="24">24</div><div class="lbl">/7 ACCOUNT SUPPORT</div></div>
          <div class="stat reveal"><div class="num">DBS</div><div class="lbl">VETTING &amp; SCREENING</div></div>
          <div class="stat reveal"><div class="num">RTW</div><div class="lbl">RIGHT TO WORK</div></div>
          <div class="stat reveal"><div class="num">TUPE</div><div class="lbl">TRANSFER EXPERTISE</div></div>
        </div>
        <div class="reveal" style="text-align:center;margin-top:36px;">
          <a href="/staffing.html" class="btn btn-primary magnetic">See our Staffing Solutions <span class="arrow">→</span></a>
        </div>
      </div>
    </section>
"""

    how = """
    <section class="approach" id="how-it-works">
      <div class="wrap">
        <div class="approach-head">
          <div><div class="eyebrow reveal">How support begins</div><h2 class="reveal">A considered path to the right care.</h2></div>
        </div>
        <div class="timeline">
          <div class="timeline-track"><div class="fill" id="timelineFill"></div></div>
          <div class="timeline-grid">
            <div class="t-step reveal"><div class="t-dot">01</div><h3>Understand</h3><p>We take time to understand the person's needs, routine and circumstances.</p></div>
            <div class="t-step reveal"><div class="t-dot">02</div><h3>Match</h3><p>We identify the right kind of support, and the right person to provide it.</p></div>
            <div class="t-step reveal"><div class="t-dot">03</div><h3>Support</h3><p>Compassionate, professional support begins — on the schedule that works.</p></div>
            <div class="t-step reveal"><div class="t-dot">04</div><h3>Continue</h3><p>We stay in touch, so support keeps pace as needs change.</p></div>
          </div>
        </div>
      </div>
    </section>
"""

    cta = """
    <section class="final-cta" id="cta">
      <div class="final-p"><svg viewBox="0 0 200 260" style="filter:url(#softGlow)"><use href="#plutoP" /></svg></div>
      <div class="wrap" style="position:relative;z-index:1;">
        <div class="eyebrow reveal">Not sure where to start?</div>
        <h2 class="reveal">Let's talk.</h2>
        <p class="sub reveal">Whether you're looking for care, staffing support, or your next role — we're a phone call away.</p>
        <div class="hero-ctas reveal" style="justify-content:center;margin-top:28px;">
          <a href="/contact.html" class="btn btn-primary magnetic">Contact Pluto BV Ltd <span class="arrow">→</span></a>
          <a href="tel:01604630916" class="btn btn-ghost magnetic">01604 630 916</a>
        </div>
      </div>
    </section>
"""

    return hero + intro + people + services + staffing_teaser + how + cta