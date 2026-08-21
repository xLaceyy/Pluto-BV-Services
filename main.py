from build import page
import pages_home, pages_about, pages_biz, pages_portal, pages_contact, pages_services

page("/index.html", "Pluto BV Ltd — Care, elevated.",
     "Pluto BV Ltd recruits and supplies social care professionals to the NHS, local authorities and residential homes, and provides live-in, domiciliary, companionship and specialist care support.",
     pages_home.home(), active_key=None)

page("/about.html", "About Pluto BV Ltd | Care & Staffing",
     "Pluto BV Ltd is a specialist social-care recruitment and staffing organisation providing temporary and permanent professionals across public and private sectors.",
     pages_about.about(), active_key="about")

page("/care.html", "Care Services | Pluto BV Ltd",
     "Live-in care, domiciliary care, companionship care and autism & specialist support from Pluto BV Ltd.",
     pages_biz.care(), active_key="care")

page("/staffing.html", "Staffing Solutions | Pluto BV Ltd",
     "Vetted, compliant social care staffing for the NHS, local authorities and residential care homes, with 24/7 account management.",
     pages_biz.staffing(), active_key="staffing")

page("/what-we-expect.html", "What You Can Expect | Pluto BV Ltd",
     "Vetting, screening, compliance, account management and performance standards at Pluto BV Ltd, explained in plain terms.",
     pages_biz.what_we_expect(), active_key="expect")

page("/stories.html", "Stories | Pluto BV Ltd",
     "Genuine testimonials from the organisations and people Pluto BV Ltd has worked with.",
     pages_biz.stories(), active_key="stories")

page("/staff-portal.html", "Staff Portal | Pluto BV Ltd",
     "Apply for a care role or submit a timesheet with Pluto BV Ltd.",
     pages_portal.staff_portal(), active_key="portal",
     extra_js='  <script src="../assets/js/forms.js"></script>\n  <script src="../assets/js/portal.js"></script>')

page("/contact.html", "Contact Pluto BV Ltd | Care & Staffing",
     "Contact Pluto BV Ltd for care support, staffing solutions or careers enquiries. Call 01604 630 916 or email admin@plutobvservices.co.uk.",
     pages_contact.contact(), active_key="contact",
     extra_js='  <script src="../assets/js/forms.js"></script>')

page("/services/live-in-care.html", "Live-in Care | Pluto BV Ltd",
     "Round-the-clock live-in care support that lets you stay independent in the comfort of your own home.",
     pages_services.live_in_care(), active_key="care")

page("/services/domiciliary-care.html", "Domiciliary Care | Pluto BV Ltd",
     "Domiciliary care for people who live in their own homes and need support with daily activities, household tasks and personal care.",
     pages_services.domiciliary_care(), active_key="care")

page("/services/companionship-care.html", "Companionship Care | Pluto BV Ltd",
     "Companionship care from Pluto BV Ltd — conversation, social interaction and consistent human connection.",
     pages_services.companionship_care(), active_key="care")

page("/services/autism-support.html", "Autism & Specialist Support | Pluto BV Ltd",
     "Person-centred support for individuals with a diagnosis of Autism Spectrum Disorder, complex needs and behaviours that challenge others.",
     pages_services.autism_support(), active_key="care")

print("\nAll pages generated.")