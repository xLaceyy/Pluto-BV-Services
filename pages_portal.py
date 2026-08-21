def staff_portal():
    return """
    <section class="page-header">
      <div class="wrap">
        <div class="breadcrumbs"><a href="/index.html">Home</a> / <span>Staff Portal</span></div>
        <div class="eyebrow">Current &amp; prospective staff</div>
        <h1 style="margin-top:10px;">Staff Portal</h1>
        <p class="lede">Apply for a role, or submit a timesheet if you're already placed with us.</p>
      </div>
    </section>

    <section class="staff-portal" id="staff-portal">
      <div class="wrap">
        <div class="portal-card reveal" style="margin-top:32px;">
          <h3 style="margin:0 0 6px;">Apply for a role</h3>
          <p style="color:var(--text-secondary,#68616F); font-size:13.5px; margin-bottom:20px;">Tell us a bit about yourself and we'll follow up by phone or email.</p>
          <form id="applyForm" class="glass-form" novalidate>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
              <div>
                <input type="text" name="fullName" id="ap-name" placeholder="Full name" required>
                <div class="field-error" id="ap-name-err">Please enter your name.</div>
              </div>
              <div>
                <input type="tel" name="phone" id="ap-phone" placeholder="Phone number" required>
                <div class="field-error" id="ap-phone-err">Please enter a contact number.</div>
              </div>
            </div>
            <div>
              <input type="email" name="email" id="ap-email" placeholder="Email address" required>
              <div class="field-error" id="ap-email-err">Please enter a valid email address.</div>
            </div>
            <div>
              <select name="role" id="ap-role" required>
                <option value="">Which role are you applying for?</option>
                <option value="live-in">Live-in Carer</option>
                <option value="domiciliary">Domiciliary Carer</option>
                <option value="companionship">Companionship Support Worker</option>
                <option value="autism">Autism / Specialist Support Worker</option>
                <option value="other">Other social care role</option>
              </select>
              <div class="field-error" id="ap-role-err">Please select a role.</div>
            </div>
            <button type="submit" class="btn btn-primary" id="ap-submit">Send application <span class="arrow">→</span></button>
            <div class="form-status" id="ap-status" role="status" aria-live="polite"></div>
          </form>
        </div>

        <div class="portal-card reveal">
          <h3 style="margin:0 0 6px;">Submit a timesheet</h3>
          <p style="color:var(--text-secondary,#68616F); font-size:13.5px; margin-bottom:20px;">PDF or photo of your completed timesheet, up to 10MB.</p>
          <label class="upload-drop" id="ts-drop" for="ts-file">
            <input type="file" id="ts-file" accept="application/pdf,image/*">
            <div>Click to choose a file, or drag one here</div>
            <div class="upload-filename" id="ts-filename"></div>
          </label>
          <button type="button" class="btn btn-primary" id="ts-submit" style="margin-top:16px;" disabled>Submit timesheet</button>
          <div class="form-status" id="ts-status" role="status" aria-live="polite"></div>
        </div>
      </div>
    </section>
"""