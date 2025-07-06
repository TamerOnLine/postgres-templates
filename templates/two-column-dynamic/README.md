# 📄 Template: Two Column Dynamic

This template provides a dynamic two-column resume layout with built-in editing, saving, and printing capabilities – all in the browser.

---

## ✨ Features

- ✏️ Edit text inline or via edit buttons.
- ➕ Add new sections or items dynamically.
- 🗑️ Delete any section or item.
- ⬆️⬇️ Move elements up or down in order.
- 🙈 Hide elements from the printed version.
- 💾 Save all changes using `localStorage`.
- 🧹 Reset everything to the default layout.
- 🖨️ Print your resume in a clean, print-optimized format.

---

## 📁 Files Overview

| File            | Description                          |
|-----------------|--------------------------------------|
| `index.html`    | Main resume layout                   |
| `style.css`     | Styling and print formatting         |
| `save.js`       | JavaScript logic for dynamic actions |
| `README.md`     | This documentation file              |

---

## 🧠 How It Works

- All edits are saved in `localStorage` under the key: `tamer-resume-data`.
- On page load, saved data is restored automatically.
- No backend is required – everything works client-side.

---

## 🖨️ Print Output

- Use the 🖨️ “Print Page” button to print.
- Elements marked with `.no-print` will not appear in the print view.
- Layout avoids breaking sections across pages using `break-inside: avoid`.

---

## 💡 Tips

- To reuse this template for another person, duplicate the folder and customize the contents.
- You can export the resume as PDF using the browser’s built-in print-to-PDF.
- Use 🧹 “Reset” to clear all edits and start fresh.

---

## 🧑‍💻 Developer Notes

- Editing is enabled via `contenteditable` and `prompt()` dialogs.
- Consider enhancing the editing UX with modal forms or rich text editors.
- Multilingual support can be added via `lang` attributes and i18n-compatible keys.

---

## 🧪 Quick Start

1. Open `index.html` in a modern browser.
2. Edit text sections, titles, or project descriptions.
3. Click 💾 “Save Changes”.
4. Refresh the page – your edits are preserved.
5. Click 🖨️ “Print Page” to generate a PDF or paper copy.

---

## 🔗 Live Demo

You can try the resume template live in your browser:

👉 [Open Template in Browser](https://tameronline.github.io/resume-templates/templates/two-column-dynamic/)

---

Made with ❤️ by [Tamer Hamad Faour](https://github.com/TamerOnLine)

