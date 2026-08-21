/* Pluto BV Ltd — portal.js
   Timesheet upload widget */
(function () {
  "use strict";
  var drop = document.getElementById("ts-drop");
  var input = document.getElementById("ts-file");
  var filename = document.getElementById("ts-filename");
  var submit = document.getElementById("ts-submit");
  var status = document.getElementById("ts-status");
  if (!drop || !input) return;

  var maxBytes = 10 * 1024 * 1024;
  var chosen = null;

  function handleFile(file) {
    status.className = "form-status";
    if (!file) return;
    var okType = file.type === "application/pdf" || file.type.indexOf("image/") === 0;
    if (!okType) {
      filename.textContent = "";
      status.textContent = file.name + " isn't a PDF or image — please choose a different file.";
      status.classList.add("show", "error");
      submit.disabled = true;
      chosen = null;
      return;
    }
    if (file.size > maxBytes) {
      filename.textContent = "";
      status.textContent = file.name + " is over 10MB — please choose a smaller file.";
      status.classList.add("show", "error");
      submit.disabled = true;
      chosen = null;
      return;
    }
    chosen = file;
    filename.textContent = file.name + " (" + Math.round(file.size / 1024) + " KB) — ready to send.";
    submit.disabled = false;
  }

  input.addEventListener("change", function () { handleFile(input.files[0]); });
  drop.addEventListener("dragover", function (e) { e.preventDefault(); drop.classList.add("dragover"); });
  drop.addEventListener("dragleave", function () { drop.classList.remove("dragover"); });
  drop.addEventListener("drop", function (e) {
    e.preventDefault();
    drop.classList.remove("dragover");
    if (e.dataTransfer.files[0]) { input.files = e.dataTransfer.files; handleFile(e.dataTransfer.files[0]); }
  });

  submit.addEventListener("click", function () {
    if (!chosen) return;
    status.className = "form-status";
    status.textContent = 'There\'s no live upload endpoint connected yet — please attach "' + chosen.name + '" to an email and send it to admin@plutobvservices.co.uk directly.';
    status.classList.add("show", "error");
  });
})();
