def contact():
    return """
    <section class="page-header">
      <div class="wrap">
        <div class="breadcrumbs"><a href="/index.html">Home</a> / <span>Contact</span></div>
        <div class="eyebrow">Get in touch</div>
        <h1 style="margin-top:10px;">Let's talk.</h1>
        <p class="lede">Whether you're looking for care, staffing support, or your next role — we're a phone call away.</p>
      </div>
    </section>

    <section class="pad-xl" style="background:#fff;">
      <div class="wrap" style="max-width:640px;">
        <form id="contactForm" class="glass-form reveal" novalidate>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
            <input type="text" name="fullName" placeholder="Full Name" required />
            <input type="tel" name="phone" placeholder="Phone Number" required />
          </div>
          <input type="email" name="email" placeholder="Email Address" required />
          <select name="enquiryType" required>
            <option value="">How can we help?</option>
            <option value="care">I need care for myself / a family member</option>
            <option value="staffing">I need staffing for an organisation</option>
            <option value="job">I'm looking for a care role</option>
          </select>
          <textarea rows="4" name="message" placeholder="How can we assist you?" required></textarea>
          <button type="submit" class="btn btn-primary" id="contact-submit">Send Enquiry <span class="arrow">→</span></button>
          <div class="form-status" id="contact-status" role="status" aria-live="polite"></div>
        </form>
        <div class="final-phone reveal" style="margin-top:32px;text-align:center;">01604 630 916</div>
        <p class="reveal" style="text-align:center;margin-top:8px;color:var(--text-secondary);font-size:14px;">admin@plutobvservices.co.uk &middot; 3 Spencer Parade, Northampton, NN1 5AA</p>
      </div>
    </section>

    <section class="pad-xl" id="legal" style="background:var(--bg-body);">
      <div class="wrap" style="max-width:760px;">
        <h2 class="reveal">Legal</h2>
        <div id="legal-privacy" class="reveal" style="margin-top:32px;">
          <h3>Privacy Policy</h3>
          <p style="color:var(--text-secondary);margin-top:10px;line-height:1.7;">Pluto BV Ltd collects only the information you give us directly — such as through the contact or application forms on this site — in order to respond to your enquiry, process an application, or arrange care or staffing support. We don't sell or share your details with third parties for marketing. For any question about what we hold or to request its removal, contact <a href="mailto:admin@plutobvservices.co.uk">admin@plutobvservices.co.uk</a>.</p>
        </div>
        <div id="legal-terms" class="reveal" style="margin-top:32px;">
          <h3>Terms</h3>
          <p style="color:var(--text-secondary);margin-top:10px;line-height:1.7;">This website provides information about Pluto BV Ltd's care and staffing services. It doesn't form a contract for services — any placement or care arrangement is agreed separately in writing. Content here is kept accurate to the best of our knowledge; contact us if anything looks out of date.</p>
        </div>
        <div id="legal-cookies" class="reveal" style="margin-top:32px;">
          <h3>Cookies</h3>
          <p style="color:var(--text-secondary);margin-top:10px;line-height:1.7;">This site does not currently set analytics or marketing cookies. Fonts and animation libraries are loaded from third-party CDNs (Google Fonts, cdnjs, jsDelivr), which may set their own technical cookies as part of delivering those files.</p>
        </div>
      </div>
    </section>
"""