document.addEventListener("DOMContentLoaded", async () => {
  const API_BASE = "http://127.0.0.1:8000/api";

  const leftColumn = document.querySelector(".left-column");
  const rightColumn = document.querySelector(".right-column");

  // 🧩 تحميل الأقسام
  const sections = await fetch(`${API_BASE}/sections`).then(res => res.json());

  // 🧩 تحميل المشاريع والعناصر
  const projects = await fetch(`${API_BASE}/projects`).then(res => res.json());
  const items = await fetch(`${API_BASE}/items`).then(res => res.json());

  for (const section of sections) {
    const sectionBox = document.createElement("div");
    sectionBox.className = "section-box";

    // ✅ اسم القسم
    const title = document.createElement("h2");
    title.textContent = section.name;
    sectionBox.appendChild(title);

    // 🎯 مشاريع القسم
    const sectionProjects = projects.filter(p => p.section_id === section.id);
    const sectionItems = items.filter(i => i.section_id === section.id);

    if (sectionProjects.length) {
      for (const project of sectionProjects) {
        const div = document.createElement("div");
        div.className = "project-item";
        div.innerHTML = `
          <h3>${project.title}</h3>
          <p><strong>Company:</strong> ${project.company}</p>
          <p><strong>From:</strong> ${project.from_date} → <strong>To:</strong> ${project.to_date}</p>
          <p>${project.description}</p>
          <a href="${project.link}" target="_blank">${project.link}</a>
        `;
        sectionBox.appendChild(div);
      }
    }

    if (sectionItems.length) {
      const ul = document.createElement("ul");
      for (const item of sectionItems) {
        const li = document.createElement("li");
        li.innerHTML = `<strong>${item.label}:</strong> ${item.value}`;
        ul.appendChild(li);
      }
      sectionBox.appendChild(ul);
    }

    // 📌 عرض حسب نوع القسم
    if (section.name.toLowerCase().includes("project")) {
      rightColumn.appendChild(sectionBox);
    } else {
      leftColumn.appendChild(sectionBox);
    }
  }
});
