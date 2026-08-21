from build import IMG

ALL_SERVICES = [
    ("Live-in Care", "/services/live-in-care.html", IMG["livein"]),
    ("Domiciliary Care", "/services/domiciliary-care.html", IMG["domiciliary"]),
    ("Companionship Care", "/services/companionship-care.html", IMG["companionship"]),
    ("Autism &amp; Specialist Support", "/services/autism-support.html", IMG["autism"]),
]

def service_page(*, path, name, headline, intro, hero_img, features, cta_label, related_exclude, who_benefits, faqs):
    header = """
    <section class="page-header">
      <div class="wrap">
        <div class="breadcrumbs"><a href="/index.html">Home</a> / <a href="/care.html">Care</a> / <span>%s</span></div>
        <div class="eyebrow">Care services</div>
        <h1 style="margin-top:10px;">%s</h1>
        <p class="lede">%s</p>
        <div class="hero-ctas" style="margin-top:26px;"><a href="/contact.html" class="btn btn-primary magnetic">%s <span class="arrow">→</span></a></div>
      </div>
    </section>
""" % (name, headline, intro, cta_label)

    media = """
    <section class="pad-lg" style="background:#fff;">
      <div class="wrap">
        <div class="image-wrap reveal" style="aspect-ratio:21/9;"><img src="%s" alt="%s" loading="lazy" /></div>
      </div>
    </section>
""" % (hero_img, name.replace("&amp;", "and"))

    rows = "".join("""
          <div class="feature-row reveal"><div><span class="fnum">%02d</span></div><div><h3>%s</h3><p>%s</p></div></div>""" % (i, t, d) for i, (t, d) in enumerate(features, start=1))
    feature_section = """
    <section class="pad-xl" style="background:var(--bg-body);">
      <div class="wrap">
        <div class="section-head reveal" style="max-width:640px;"><div class="eyebrow">What support can include</div><h2 style="margin-top:10px;">Here's what to expect.</h2></div>
        <div class="feature-rows" style="max-width:900px;">%s</div>
      </div>
    </section>
""" % rows

    who_html = """
    <section class="pad-lg" style="background:#fff;">
      <div class="wrap" style="max-width:760px;">
        <div class="eyebrow reveal">Who might benefit</div>
        <p class="reveal" style="margin-top:12px;color:var(--text-secondary);line-height:1.8;font-size:15px;">%s</p>
      </div>
    </section>
""" % who_benefits

    faq_html = "".join("""
        <details class="faq-item reveal"><summary>%s <span class="plus">+</span></summary><div class="faq-body">%s</div></details>""" % (q, a) for q, a in faqs)
    faq_section = """
    <section class="pad-lg" style="background:var(--bg-body);">
      <div class="wrap" style="max-width:760px;">
        <div class="eyebrow reveal">FAQs</div>
        <div style="margin-top:16px;">%s</div>
      </div>
    </section>
""" % faq_html

    related = [s for s in ALL_SERVICES if s[0] != name]
    related_html = "".join("""
          <a href="%s" class="people-card reveal-scale" style="background-image:url('%s');min-height:220px;">
            <div class="card-overlay"></div>
            <div class="card-inner people-card-content"><h3 style="font-size:18px;">%s</h3><span class="service-cta" style="color:#fff;">Explore →</span></div>
          </a>""" % (href, img, title) for title, href, img in related)
    related_section = """
    <section class="people pad-xl">
      <div class="wrap">
        <div class="people-head"><div class="eyebrow reveal">Related</div><h2 class="reveal">Other ways we support people</h2></div>
        <div class="people-grid" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr));">%s</div>
      </div>
    </section>
""" % related_html

    cta = """
    <section class="final-cta" id="contact">
      <div class="final-p"><svg viewBox="0 0 200 260" style="filter:url(#softGlow)"><use href="#plutoP" /></svg></div>
      <div class="wrap" style="position:relative;z-index:1;">
        <div class="eyebrow reveal">Let's talk about %s</div>
        <h2 class="reveal">Speak with our team.</h2>
        <div class="hero-ctas reveal" style="justify-content:center;margin-top:28px;">
          <a href="/contact.html" class="btn btn-primary magnetic">%s <span class="arrow">→</span></a>
        </div>
      </div>
    </section>
""" % (name.replace("&amp;", "and").lower(), cta_label)

    return header + media + feature_section + who_html + faq_section + related_section + cta


def live_in_care():
    return service_page(
        path="/services/live-in-care.html",
        name="Live-in Care",
        headline="Care that lets you stay where you belong.",
        intro="Security and peace of mind to continue living the life you choose, in the comfort of your own home, with someone on hand to help whenever you need it.",
        hero_img=IMG["livein"],
        features=[
            ("Comprehensive support", "A dedicated caregiver based in your home, offering round-the-clock support and assistance."),
            ("Assistance with daily activities", "Support with personal care tasks, mobility, medication reminders and meal preparation."),
            ("Promoting independence", "Caregivers encourage and assist with tasks you're able to manage yourself."),
            ("Companionship", "Conversation, shared activities and emotional support."),
            ("Peace of mind for family", "Family members can be reassured knowing a trained professional is present."),
            ("A routine that's yours", "Live-in care adapts to your existing routine and preferences."),
            ("Experienced caregivers", "Caregivers are vetted and trained to handle a range of needs."),
        ],
        cta_label="Discuss Live-in Care",
        related_exclude="Live-in Care",
        who_benefits="People who need consistent, round-the-clock support but want to remain in their own home rather than move into residential care.",
        faqs=[
            ("How is a live-in carer matched to me?", "We consider the support required, personal preferences, and the caregiver's experience before proposing a match."),
            ("Can the arrangement change over time?", "Yes — needs change, and the level of support can be reviewed and adjusted."),
        ],
    )


def domiciliary_care():
    return service_page(
        path="/services/domiciliary-care.html",
        name="Domiciliary Care",
        headline="Professional support, in the comfort of home.",
        intro="For people who live in their own home but need additional support with daily activities, household tasks and personal care.",
        hero_img=IMG["domiciliary"],
        features=[
            ("Daily activities support", "Assistance with personal care tasks like bathing, dressing and grooming."),
            ("Household tasks", "Support with cleaning, cooking, shopping and other everyday tasks."),
            ("Medication support", "Caregivers can assist with medication reminders where agreed."),
            ("Companionship", "Conversation, activities and interaction that provide emotional support."),
            ("Promoting independence", "We focus on supporting people to do what they can for themselves."),
            ("Flexible visits", "Visits are arranged around your routine, where availability allows."),
            ("Family peace of mind", "Reassurance for family members that a loved one is cared for safely."),
        ],
        cta_label="Talk About Your Care Needs",
        related_exclude="Domiciliary Care",
        who_benefits="People who are largely independent but need scheduled support — a daily or weekly visit for personal care, household tasks, or company.",
        faqs=[
            ("How often can visits happen?", "Visit frequency is arranged around what's needed — from a single weekly visit to multiple visits a day."),
            ("Is this different from live-in care?", "Yes — domiciliary care is scheduled visits, while live-in care means a caregiver is based in the home."),
        ],
    )


def companionship_care():
    return service_page(
        path="/services/companionship-care.html",
        name="Companionship Care",
        headline="Because nobody should feel alone.",
        intro="Loneliness and social isolation can significantly affect older people's wellbeing. Companionship care is about consistent, genuine human connection.",
        hero_img=IMG["companionship"],
        features=[
            ("Meaningful social interaction", "Conversations and activities that foster real connection."),
            ("Emotional support", "A listening ear and genuine attention — comfort as well as company."),
            ("Alleviating loneliness", "Regular companionship for people who can experience isolation."),
            ("Personalised activities", "Companionship built around personal interests."),
            ("Accompaniment & outings", "Caregivers can accompany people on outings, walks or appointments."),
            ("Respite for family carers", "Valuable respite for family caregivers."),
            ("A consistent, familiar presence", "We aim to build lasting familiarity rather than rotate through unfamiliar faces."),
        ],
        cta_label="Arrange Companionship Care",
        related_exclude="Companionship Care",
        who_benefits="People who are managing well physically but experiencing loneliness or reduced social contact.",
        faqs=[
            ("Is companionship care just conversation?", "It's built around whatever genuine connection looks like for that person — conversation, shared activities, outings, or simply familiar company."),
            ("Can this be combined with other services?", "Yes — companionship is often arranged alongside domiciliary or live-in care."),
        ],
    )


def autism_support():
    return service_page(
        path="/services/autism-support.html",
        name="Autism &amp; Specialist Support",
        headline="Support that starts with the person.",
        intro="Specialised, person-centred support for individuals with a diagnosis of Autism Spectrum Disorder, complex needs, and behaviours that may challenge others.",
        hero_img=IMG["autism"],
        features=[
            ("Individualised support", "A tailored approach that accounts for individual strengths, preferences and needs."),
            ("Communication", "A supportive environment focused on communication styles that work for the individual."),
            ("Routines & consistency", "Support structured around routines and consistency."),
            ("Complex support needs", "Support for individuals with complex needs, delivered with patience and professionalism."),
            ("Family involvement", "Working alongside families, where appropriate, to keep support joined-up."),
            ("Professional matching", "Support workers matched to individual needs rather than assigned generically."),
        ],
        cta_label="Discuss Specialist Support",
        related_exclude="Autism &amp; Specialist Support",
        who_benefits="Autistic individuals and people with complex support needs who benefit from consistent, trained support that respects individual communication styles and routines.",
        faqs=[
            ("Are support workers specifically trained for this?", "Support workers for this service have relevant experience and training."),
            ("Can support be adjusted as needs change?", "Yes — we review and adjust support in consultation with the individual and their family or care team."),
        ],
    )


def care():
    header = """
    <section class="page-header">
      <div class="wrap">
        <div class="breadcrumbs"><a href="/index.html">Home</a> / <span>Care</span></div>
        <div class="eyebrow">Care services</div>
        <h1 style="margin-top:10px;">Support that meets people where they are.</h1>
        <p class="lede">Four ways we help people stay independent, connected and well supported — at home, or in the setting that suits them best.</p>
      </div>
    </section>
"""
    cards = [
        ("Live-in Care", "/services/live-in-care.html", IMG["livein"], "Round-the-clock support in the comfort of your own home."),
        ("Domiciliary Care", "/services/domiciliary-care.html", IMG["domiciliary"], "Support with daily activities and household tasks."),
        ("Companionship Care", "/services/companionship-care.html", IMG["companionship"], "Because nobody should feel alone — conversation, activities and consistent connection."),
        ("Autism &amp; Specialist Support", "/services/autism-support.html", IMG["autism"], "Person-centred support for individuals with autism and complex needs."),
    ]
    grid = "".join("""
          <a href="%s" class="people-card reveal-scale" style="background-image:url('%s');">
            <div class="card-overlay"></div>
            <div class="card-inner people-card-content">
              <h3>%s</h3>
              <p>%s</p>
              <span class="service-cta" style="color:#fff;">Explore service →</span>
            </div>
          </a>""" % (href, img, name, desc) for name, href, img, desc in cards)

    services_grid = """
    <section class="people pad-xl">
      <div class="wrap">
        <div class="people-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">%s</div>
      </div>
    </section>
""" % grid

    approach = """
    <section class="approach">
      <div class="wrap">
        <div class="approach-head"><div><div class="eyebrow reveal">How support begins</div><h2 class="reveal">A considered path to the right care.</h2></div></div>
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
    <section class="final-cta" id="contact">
      <div class="final-p"><svg viewBox="0 0 200 260" style="filter:url(#softGlow)"><use href="#plutoP" /></svg></div>
      <div class="wrap" style="position:relative;z-index:1;">
        <div class="eyebrow reveal">Not sure which service fits?</div>
        <h2 class="reveal">Tell us about the situation.</h2>
        <p class="sub reveal">We'll help you find the right kind of support.</p>
        <div class="hero-ctas reveal" style="justify-content:center;margin-top:28px;">
          <a href="/contact.html" class="btn btn-primary magnetic">Discuss Your Needs <span class="arrow">→</span></a>
        </div>
      </div>
    </section>
"""
    return header + services_grid + approach + cta


def staffing():
    header = """
    <section class="page-header">
      <div class="wrap">
        <div class="breadcrumbs"><a href="/index.html">Home</a> / <span>Staffing</span></div>
        <div class="eyebrow">For care organisations</div>
        <h1 style="margin-top:10px;">Reliable people, for the teams that need them.</h1>
        <p class="lede">Temporary and permanent social care professionals for local authorities, the NHS, residential homes and other organisations that need appropriately screened staff.</p>
        <div class="hero-ctas" style="margin-top:26px;">
          <a href="/contact.html" class="btn btn-primary magnetic">Request Staffing <span class="arrow">→</span></a>
          <a href="tel:01604630916" class="btn btn-ghost magnetic">Speak to Pluto</a>
        </div>
      </div>
    </section>
"""
    trust = """
    <section class="trust">
      <div class="wrap">
        <div class="trust-head"><div class="eyebrow reveal" style="justify-content:center;">Who we support</div><h2 class="reveal">Sectors we work with.</h2></div>
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
      </div>
    </section>
"""
    capabilities = [
        ("Vetting &amp; Screening", "Every professional we supply undergoes vetting and screening, including DBS-related checks, before placement."),
        ("Diverse Care Specialisations", "A roster of social care professionals spanning elderly care, learning disabilities support, and complex needs."),
        ("Coverage Across Disciplines", "An integrated approach across social care disciplines — residential homes, healthcare settings and other relevant environments."),
        ("Care Standards", "We operate with reference to established care standards."),
        ("TUPE Expertise", "Experience supporting the transfer of staff from outgoing suppliers under TUPE."),
        ("Responsive Account Management", "A dedicated account manager available 24/7 to respond to staffing issues."),
        ("Performance Measurement", "Ongoing performance measurement with client management information."),
        ("Flexibility in Administration", "Adaptable invoicing and review documentation."),
    ]
    cap_html = "".join('<div class="capability-card reveal"><h4>%s</h4><p>%s</p></div>' % (t, d) for t, d in capabilities)
    cap_section = """
    <section class="pad-xl" style="background:#fff;">
      <div class="wrap">
        <div class="section-head reveal" style="max-width:640px;"><div class="eyebrow">What we provide</div><h2 style="margin-top:10px;">A detailed look at our staffing service.</h2></div>
        <div class="capability-grid" style="margin-top:36px;">%s</div>
      </div>
    </section>
""" % cap_html

    matching = """
    <section class="pad-xl" style="background:var(--bg-body);">
      <div class="wrap split-grid reverse">
        <div>
          <div class="image-wrap"><img src="%s" alt="Account manager discussing staffing requirements" loading="lazy" /></div>
        </div>
        <div>
          <div class="eyebrow reveal">Matching</div>
          <h2 class="reveal" style="margin-top:10px;">Filling a shift isn't the goal. The right fit is.</h2>
          <p class="reveal" style="margin-top:14px;color:var(--text-secondary);line-height:1.8;font-size:15px;">An organisation's requirements go beyond a job title — the setting, the role, the shift pattern, the professional skills needed, and the needs of the people being cared for all matter. We consider these together when identifying a suitable professional.</p>
        </div>
      </div>
    </section>
""" % IMG["staffing2"]

    process = """
    <section class="approach">
      <div class="wrap">
        <div class="approach-head"><div><div class="eyebrow reveal">How an organisation works with Pluto</div><h2 class="reveal">A clear process, start to finish.</h2></div></div>
        <div class="prof-steps" style="margin-top:20px;">
          <div class="p-step reveal"><div class="pnum">01</div><div><h4>Discuss</h4><span>Tell us about your staffing requirement.</span></div></div>
          <div class="p-step reveal"><div class="pnum">02</div><div><h4>Understand</h4><span>We understand the setting, roles and workforce considerations involved.</span></div></div>
          <div class="p-step reveal"><div class="pnum">03</div><div><h4>Source</h4><span>Appropriate professionals are identified.</span></div></div>
          <div class="p-step reveal"><div class="pnum">04</div><div><h4>Screen</h4><span>Required checks and verification are completed.</span></div></div>
          <div class="p-step reveal"><div class="pnum">05</div><div><h4>Match</h4><span>Suitable professionals are considered against your requirements.</span></div></div>
          <div class="p-step reveal"><div class="pnum">06</div><div><h4>Place</h4><span>Staffing arrangements are confirmed.</span></div></div>
          <div class="p-step reveal"><div class="pnum">07</div><div><h4>Support</h4><span>The relationship continues through communication and account management.</span></div></div>
        </div>
      </div>
    </section>
"""

    faqs = [
        ("What types of organisations does Pluto support?", "Local authorities, the NHS and other healthcare organisations, and private residential homes."),
        ("Can Pluto provide temporary staffing?", "Yes — for organisations that need additional capacity, short-term cover, or flexible staffing."),
        ("Can Pluto support permanent recruitment?", "Yes, for organisations recruiting for longer-term positions."),
        ("What screening do professionals undergo?", "Vetting and screening including DBS-related checks and UK Right to Work verification."),
        ("Can Pluto support organisations changing staffing providers?", "We have experience supporting TUPE and staff-transfer processes."),
        ("How do I request staffing?", "Get in touch through our contact page or call 01604 630 916."),
    ]
    faq_html = "".join("""
        <details class="faq-item reveal"><summary>%s <span class="plus">+</span></summary><div class="faq-body">%s</div></details>""" % (q, a) for q, a in faqs)
    faq_section = """
    <section class="pad-xl" style="background:#fff;">
      <div class="wrap" style="max-width:820px;">
        <div class="section-head reveal" style="max-width:640px;"><div class="eyebrow">FAQs</div><h2 style="margin-top:10px;">Common questions from organisations.</h2></div>
        <div style="margin-top:20px;">%s</div>
      </div>
    </section>
""" % faq_html

    cta = """
    <section class="final-cta" id="contact">
      <div class="final-p"><svg viewBox="0 0 200 260" style="filter:url(#softGlow)"><use href="#plutoP" /></svg></div>
      <div class="wrap" style="position:relative;z-index:1;">
        <div class="eyebrow reveal">Need additional care professionals?</div>
        <h2 class="reveal">Tell Pluto what your organisation needs.</h2>
        <div class="hero-ctas reveal" style="justify-content:center;margin-top:28px;">
          <a href="/contact.html" class="btn btn-primary magnetic">Request Staffing <span class="arrow">→</span></a>
          <a href="tel:01604630916" class="btn btn-ghost magnetic">Speak to our team</a>
        </div>
      </div>
    </section>
"""
    return header + trust + cap_section + matching + process + faq_section + cta


def what_we_expect():
    header = """
    <section class="page-header">
      <div class="wrap">
        <div class="breadcrumbs"><a href="/index.html">Home</a> / <span>What You Can Expect</span></div>
        <div class="eyebrow">Standards &amp; trust</div>
        <h1 style="margin-top:10px;">What you can expect from Pluto.</h1>
        <p class="lede">Screening, compliance, account management and performance — explained in plain terms.</p>
      </div>
    </section>
"""
    rows = [
        ("VETTING", "Vetting &amp; screening", "Every professional we place goes through vetting and screening before starting, including DBS-related checks and identity verification."),
        ("RTW", "Right to Work", "UK Right to Work is verified as part of onboarding."),
        ("STANDARDS", "Care standards", "We operate with reference to relevant care standards for the settings we supply into."),
        ("TUPE", "TUPE &amp; transfer management", "We have experience supporting TUPE and transfer processes to help transitions go smoothly."),
        ("ACCOUNT", "Account management", "Organisations get a dedicated account contact rather than a call centre queue."),
        ("PERFORMANCE", "Performance &amp; feedback", "We support clients with feedback, performance monitoring and review documentation where available."),
        ("ADMIN", "Administrative flexibility", "Invoicing, documentation and reviews handled with flexibility where the client needs it."),
    ]
    rows_html = "".join("""
          <div class="feature-row reveal"><div><span class="fnum">%s</span></div><div><h3>%s</h3><p>%s</p></div></div>""" % (tag, t, d) for tag, t, d in rows)
    body = """
    <section class="pad-xl" style="background:#fff;">
      <div class="wrap">
        <div class="feature-rows" style="max-width:900px;margin:0 auto;">%s</div>
      </div>
    </section>
""" % rows_html
    cta = """
    <section class="final-cta" id="contact">
      <div class="final-p"><svg viewBox="0 0 200 260" style="filter:url(#softGlow)"><use href="#plutoP" /></svg></div>
      <div class="wrap" style="position:relative;z-index:1;">
        <div class="eyebrow reveal">Questions about our standards?</div>
        <h2 class="reveal">Ask us directly.</h2>
        <div class="hero-ctas reveal" style="justify-content:center;margin-top:28px;">
          <a href="/contact.html" class="btn btn-primary magnetic">Contact Pluto BV Ltd <span class="arrow">→</span></a>
        </div>
      </div>
    </section>
"""
    return header + body + cta


def stories():
    header = """
    <section class="page-header">
      <div class="wrap">
        <div class="breadcrumbs"><a href="/index.html">Home</a> / <span>Stories</span></div>
        <div class="eyebrow">In their words</div>
        <h1 style="margin-top:10px;">Stories from the people we work with.</h1>
        <p class="lede">Two genuine testimonials from people we've worked with. We haven't padded this out with invented quotes, ratings or case studies.</p>
      </div>
    </section>
"""
    grid = """
    <section class="stories pad-xl">
      <div class="wrap">
        <div class="stories-grid">
          <div class="story-card reveal-scale">
            <div class="story-quote-mark">&ldquo;</div>
            <p class="q">Wow! What a great service.</p>
            <div class="story-meta"><span class="dot"></span><span>Service Manager</span></div>
          </div>
          <div class="story-card reveal-scale">
            <div class="story-quote-mark">&ldquo;</div>
            <p class="q">PlutoBV Services is the real deal.</p>
            <div class="story-meta"><span class="dot"></span><span>Home Manager</span></div>
          </div>
        </div>
        <div class="note-callout reveal" style="margin-top:44px;max-width:640px;">
          These are the only two testimonials we currently have on record with enough context to publish honestly. As more organisations, families and professionals share their experience with us, we'll add real stories here — with the person's role and, where they're happy for it, more detail about the situation and outcome. We won't fabricate volume in the meantime.
        </div>
      </div>
    </section>
"""
    cta = """
    <section class="final-cta" id="contact">
      <div class="final-p"><svg viewBox="0 0 200 260" style="filter:url(#softGlow)"><use href="#plutoP" /></svg></div>
      <div class="wrap" style="position:relative;z-index:1;">
        <div class="eyebrow reveal">Worked with Pluto?</div>
        <h2 class="reveal">We'd like to hear about it.</h2>
        <div class="hero-ctas reveal" style="justify-content:center;margin-top:28px;">
          <a href="/contact.html" class="btn btn-primary magnetic">Share your experience <span class="arrow">→</span></a>
        </div>
      </div>
    </section>
"""
    return header + grid + cta