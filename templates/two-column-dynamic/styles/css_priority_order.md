# 📚 CSS Priority Order: From Weakest to Strongest

In CSS, when multiple styles target the same element, the final applied style depends on the **priority (specificity)** and **source** of the rule. Here's the order from weakest to strongest:

| Order | Source                                      | Priority     |
|-------|---------------------------------------------|--------------|
| 1️⃣    | Browser default styles (User Agent)         | ❌ Weakest   |
| 2️⃣    | External CSS file (e.g., base.css)          | ✅           |
| 3️⃣    | Later external files (e.g., main.css)       | ✅✅         |
| 4️⃣    | <style> tag in the HTML head                | ✅✅✅       |
| 5️⃣    | Inline style (style attribute on elements)  | ✅✅✅✅     |
| 6️⃣    | Rules with `!important`                     | 🔥 Strongest |

---

## 🧪 Example:

```html
<p id="text">Hello!</p>
```

### Styles from different sources:

**base.css:**
```css
#text {
  color: black;
}
```

**main.css:**
```css
#text {
  color: blue;
}
```

**In-page <style>:**
```html
<style>
  #text {
    color: red;
  }
</style>
```

**Inline Style:**
```html
<p id="text" style="color: green;">Hello!</p>
```

**With !important:**
```css
#text {
  color: purple !important;
}
```

### ✅ Final Result: `color: purple`

Because `!important` overrides all other declarations.

---

## 🔍 Debugging Tip:

Use browser DevTools (F12) → Elements → Styles to see which rules apply and which are overridden (crossed out).