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