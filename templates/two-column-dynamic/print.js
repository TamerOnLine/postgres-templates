function applyPrintSettings() {
  const fontFamily = document.getElementById("font-family").value;
  const fontSize = document.getElementById("font-size").value + "pt";
  const lineHeight = document.getElementById("line-height").value;
  const wordSpacing = document.getElementById("word-spacing").value + "pt";
  const blockSpacing = document.getElementById("block-spacing").value + "px";
  // إعدادات الهوامش
  const marginTop = document.getElementById("margin-top").value + "cm";
  const marginBottom = document.getElementById("margin-bottom").value + "cm";
  const marginLeft = document.getElementById("margin-left").value + "cm";
  const marginRight = document.getElementById("margin-right").value + "cm";

  // ✨ عرض الإعدادات مباشرة في الصفحة (قبل الطباعة)
  document.body.style.fontFamily = `"${fontFamily}", serif`;
  document.body.style.fontSize = fontSize;
  document.body.style.lineHeight = lineHeight;
  document.body.style.wordSpacing = wordSpacing;
  document.body.style.padding = blockSpacing;

  // إعدادات خاصة بالطباعة
  let style = document.getElementById("dynamic-print-style");
  if (!style) {
    style = document.createElement("style");
    style.id = "dynamic-print-style";
    document.head.appendChild(style);
  }

  style.innerHTML = `
    @media print {
      body {
        font-family: "${fontFamily}", serif;
        font-size: ${fontSize};
        line-height: ${lineHeight};
        word-spacing: ${wordSpacing};
        color: #000;
      }

      .edit-button, .no-print, #print-btn, #save-btn, #clear-btn {
        display: none !important;
      }

      .left-column, .project-box, .profile-pic {
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }

      h1, h2, h3, .project-box, .left-column > div {
        break-inside: avoid;
        page-break-inside: avoid;
      }

      @page {
        margin: ${marginTop} ${marginRight} ${marginBottom} ${marginLeft};
      }
    }
  `;
}
