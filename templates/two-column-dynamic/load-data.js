document.addEventListener("DOMContentLoaded", async () => {
  const API_BASE = "http://127.0.0.1:8000/api";

  const leftColumn = document.querySelector(".left-column");
  const rightColumn = document.querySelector(".right-column");

  // 🧩 تحميل الأقسام والمشاريع والعناصر
  const [sections, projects, items] = await Promise.all([
    fetch(`${API_BASE}/sections`).then(res => res.json()),
    fetch(`${API_BASE}/projects`).then(res => res.json()),
    fetch(`${API_BASE}/items`).then(res => res.json())
  ]);

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
        div.className = "project";
        div.dataset.projectId = project.id;
        div.innerHTML = `
          <div class="project-header">
            <h3>${project.title}</h3>
            <div class="project-controls no-print"></div>
          </div>
          <p>${project.description}</p>
          <p><strong>${project.company}</strong></p>
          ${project.link ? `<a href="${project.link}" target="_blank">🔗 ${project.link}</a>` : ""}
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

  // ✅ زرع أزرار التحكم لكل مشروع
  setTimeout(() => {
    document.querySelectorAll(".project").forEach(projectEl => {
      if (typeof createControlButtons === "function") {
        createControlButtons(projectEl);
      }
    });
  }, 100);
});
