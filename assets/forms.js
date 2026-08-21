/* Pluto BV Ltd — forms.js
   Contact form + staff application form. */
(function () {
  "use strict";
  var isEmail = function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v); };

  // ---- Contact form ----
  (function () {
    var contactForm = document.getElementById("contactForm");
    if (!contactForm) return;
    var status = document.getElementById("contact-status");
    var btn = document.getElementById("contact-submit");

    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();
      status.className = "form-status";
      var fd = new FormData(contactForm);
      var name = (fd.get("fullName") || "").trim();
      var phone = (fd.get("phone") || "").trim();
      var email = (fd.get("email") || "").trim();
      var type = fd.get("enquiryType") || "";
      var message = (fd.get("message") || "").trim();

      contactForm.querySelectorAll(".invalid").forEach(function (el) { el.classList.remove("invalid"); });

      var problems = [];
      if (!name) problems.push(contactForm.querySelector('[name="fullName"]'));
      if (!phone) problems.push(contactForm.querySelector('[name="phone"]'));
      if (!email || !isEmail(email)) problems.push(contactForm.querySelector('[name="email"]'));
      if (!type) problems.push(contactForm.querySelector('[name="enquiryType"]'));
      if (!message) problems.push(contactForm.querySelector('[name="message"]'));

      if (problems.length) {
        problems.forEach(function (el) { if (el) el.classList.add("invalid"); });
        status.textContent = "Please fill in every field with a valid value before sending.";
        status.classList.add("show", "error");
        return;
      }

      btn.disabled = true;
      btn.textContent = "Opening your email…";

      var subject = "Website enquiry — " + type;
      var body = "Name: " + name + "\nPhone: " + phone + "\nEmail: " + email + "\nEnquiry type: " + type + "\n\n" + message;
      window.location.href = "mailto:admin@plutobvservices.co.uk?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);

      status.textContent = "Your email app should now be open with this enquiry pre-filled to admin@plutobvservices.co.uk — hit send there to reach us. Nothing was sent automatically from this page.";
      status.classList.add("show", "success");
      btn.disabled = false;
      btn.innerHTML = 'Send Enquiry <span class="arrow">→</span>';
    });
  })();

  // ---- Staff Portal: application form ----
  (function () {
    var form = document.getElementById("applyForm");
    if (!form) return;
    var status = document.getElementById("ap-status");
    var btn = document.getElementById("ap-submit");
    var fields = ["name", "phone", "email", "role"];

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      status.className = "form-status";
      var name = document.getElementById("ap-name");
      var phone = document.getElementById("ap-phone");
      var email = document.getElementById("ap-email");
      var role = document.getElementById("ap-role");
      [name, phone, email, role].forEach(function (el) { el.classList.remove("invalid"); });
      fields.forEach(function (f) { document.getElementById("ap-" + f + "-err").classList.remove("show"); });

      var ok = true;
      if (!name.value.trim()) { name.classList.add("invalid"); document.getElementById("ap-name-err").classList.add("show"); ok = false; }
      if (!phone.value.trim()) { phone.classList.add("invalid"); document.getElementById("ap-phone-err").classList.add("show"); ok = false; }
      if (!isEmail(email.value.trim())) { email.classList.add("invalid"); document.getElementById("ap-email-err").classList.add("show"); ok = false; }
      if (!role.value) { role.classList.add("invalid"); document.getElementById("ap-role-err").classList.add("show"); ok = false; }
      if (!ok) return;

      btn.disabled = true;
      btn.textContent = "Opening your email…";
      var subject = "Job application — " + role.options[role.selectedIndex].text;
      var body = "Name: " + name.value.trim() + "\nPhone: " + phone.value.trim() + "\nEmail: " + email.value.trim() + "\nRole: " + role.options[role.selectedIndex].text;
      window.location.href = "mailto:admin@plutobvservices.co.uk?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);

      status.textContent = "Your email app should now be open with this application pre-filled to admin@plutobvservices.co.uk — hit send there to apply. There is no live application database behind this form yet.";
      status.classList.add("show", "success");
      btn.disabled = false;
      btn.innerHTML = 'Send application <span class="arrow">→</span>';
    });
  })();
})();