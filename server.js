require('dotenv').config();
const express = require('express');
const nodemailer = require('nodemailer');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

// Email transporter (optional)
let transporter = null;
if (process.env.EMAIL_USER && process.env.EMAIL_PASS) {
  transporter = nodemailer.createTransport({
    host: process.env.EMAIL_HOST || 'smtp.gmail.com',
    port: parseInt(process.env.EMAIL_PORT || '587'),
    secure: process.env.EMAIL_SECURE === 'true',
    auth: {
      user: process.env.EMAIL_USER,
      pass: process.env.EMAIL_PASS,
    },
  });
  console.log('✅ Email ready.');
} else {
  console.warn('⚠️ Email not configured – messages logged only.');
}

// Contact form endpoint
app.post('/api/contact', async (req, res) => {
  try {
    const { fullName, email, phone, enquiryType, message } = req.body;

    if (!fullName || !email || !message || !enquiryType) {
      return res.status(400).json({ success: false, message: 'Please fill in all required fields.' });
    }

    console.log(`📩 Enquiry from ${fullName} (${email}) – ${enquiryType}`);

    if (transporter) {
      const mailOptions = {
        from: process.env.EMAIL_USER,
        to: process.env.APPLICATION_RECIPIENT || 'admin@plutobvservices.co.uk',
        subject: `Pluto Enquiry: ${enquiryType} – ${fullName}`,
        text: `
New enquiry via Pluto website.

Name: ${fullName}
Email: ${email}
Phone: ${phone || 'Not provided'}
Type: ${enquiryType}
Message:
${message}

Sent: ${new Date().toLocaleString()}
        `
      };

      await transporter.sendMail(mailOptions);

      await transporter.sendMail({
        from: process.env.EMAIL_USER,
        to: email,
        subject: 'We’ve received your enquiry',
        text: `Dear ${fullName},\n\nThank you for contacting Pluto BV Services. We'll get back to you shortly.\n\nBest regards,\nPluto BV Services Team`
      }).catch(() => {});

      res.json({ success: true, message: 'Message sent successfully.' });
    } else {
      res.json({ success: true, message: 'Message received (email disabled for testing).' });
    }
  } catch (error) {
    console.error('Contact form error:', error);
    res.status(500).json({ success: false, message: 'Something went wrong. Please try again.' });
  }
});

// Serve the new Pluto 2.0 HTML for all routes
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html')); // since index.html is in the root
});

app.listen(PORT, () => {
  console.log(`🚀 Pluto 2.0 running at http://localhost:${PORT}`);
});