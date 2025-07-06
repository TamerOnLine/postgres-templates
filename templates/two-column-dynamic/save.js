// save.js
const STORAGE_KEY = "tamer-resume-data";

function createControlButtons({ showMove = true, moveType = "default" } = {}) {
  const wrapper = document.createElement("span");
  wrapper.className = "edit-button";
  wrapper.innerHTML = `
    <button data-delete>🗑️</button>
    <button data-toggle-print>🙈 Hide from print</button>
    ${showMove ? `
      <button ${moveType === "project" ? "data-move-project-up" : "data-move-up"}>⬆️</button>
      <button ${moveType === "project" ? "data-move-project-down" : "data-move-down"}>⬇️</button>
    ` : ""}
  `;
  return wrapper;
}




function printPage() {
  window.print();
}

function saveToLocalStorage() {
  const container = document.querySelector(".container");
  localStorage.setItem(STORAGE_KEY, container.innerHTML);
  alert("✔️ Saved successfully!");
}

function clearStorage() {
  if (confirm("Are you sure you want to reset all changes?")) {
    localStorage.removeItem(STORAGE_KEY);
    location.reload();
  }
}

function editTextContent(el) {
  const currentValue = el.innerText;
  const newValue = prompt("Edit value:", currentValue);
  if (newValue !== null && newValue.trim() !== "") {
    el.innerText = newValue;
  }
}

function editLinkContent(container) {
  const a = container.querySelector("a");
  const newText = prompt("Enter link text:", a.innerText);
  const newHref = prompt("Enter URL:", a.href);
  if (newText && newHref) {
    a.innerText = newText;
    a.href = newHref;
    a.target = "_blank";
  }
}

function addMoveEffect(el) {
  el.style.transition = "background-color 0.3s ease";
  el.style.backgroundColor = "#ffffcc";
  setTimeout(() => (el.style.backgroundColor = ""), 300);
}



function deleteBlock(btn) {
  // أولاً: هل الزر داخل مشروع؟
  const projectBox = btn.closest(".project-box");

  if (projectBox) {
    const isProjectHeader = btn.closest(".project-box > .project-header-controls, .project-box > .edit-button");

    // ✅ إذا الزر في أول مستوى داخل المشروع => احذف المشروع كامل
    if (isProjectHeader && isProjectHeader.parentElement === projectBox) {
      if (confirm("Delete entire project?")) {
        projectBox.remove();
      }
      return;
    }

    // ✅ إذا الزر داخل عنصر داخل المشروع => احذف العنصر فقط
    const item = btn.closest(".project-box > div");
    if (item) {
      if (confirm("Delete this item?")) {
        item.remove();
      }
      return;
    }
  }

  // ✅ عناصر أخرى مثل li أو قسم كامل
  const otherBlock = btn.closest("li, .left-column > div, .project-section");
  if (otherBlock && confirm("Delete this block?")) {
    otherBlock.remove();
  }
}


function togglePrint(btn) {
  // حدد أقرب عنصر يمكن إخفاؤه بذكاء: مشروع، قسم، عنصر فرعي
  const block = btn.closest(".project-box, .project-section, .left-column > div, li, ul, p, h3, h2");

  if (!block) return;

  // تحديد ما إذا كان سيتم الإخفاء أو الإظهار
  const shouldHide = !block.classList.contains("no-print");

  // أضف أو أزل كلاس الإخفاء من العنصر المستهدف فقط
  block.classList.toggle("no-print", shouldHide);

  // غيّر نص الزر
  btn.textContent = shouldHide ? "👁️ Show in print" : "🙈 Hide from print";
}

function findMovableBlock(btn) {
  // إذا داخل المشروع وتحديدًا داخل أول .edit-button (أزرار المشروع نفسه)
  const projectBox = btn.closest(".project-box");
  if (projectBox) {
    const firstEditButton = projectBox.querySelector(".project-header-controls, .edit-button");
    if (firstEditButton && firstEditButton.contains(btn)) {
      return projectBox; // هذا زر خاص بالمشروع كاملًا
    }
  }

  // عنصر داخل المشروع (مثل العنوان أو التاريخ)
  const innerProjectItem = btn.closest(".project-box > div");
  if (innerProjectItem) return innerProjectItem;

  // عنصر في القسم اليسار
  const leftItem = btn.closest("li");
  if (leftItem) return leftItem;

  // قسم كامل
  const sectionBlock = btn.closest(".project-section, .left-column > div");
  if (sectionBlock) return sectionBlock;

  return null;
}

function findMovableBlock(btn) {
  // 🔍 إذا الزر داخل مشروع
  const projectBox = btn.closest(".project-box");
  if (projectBox) {
    const firstEditButton = projectBox.querySelector(".project-header-controls, .edit-button");
    
    // 🔍 إذا كان الزر ضمن أزرار تحكم المشروع وليس عنصر داخلي
    if (firstEditButton && firstEditButton.contains(btn)) {
      const section = btn.closest(".project-section");
      
      // ✅ فقط إذا كان المشروع ضمن نفس القسم
      if (section && section.contains(projectBox)) {
        return projectBox;
      }
    }
  }

  // 🔍 عنصر فرعي داخل المشروع
  const innerProjectItem = btn.closest(".project-box > div");
  if (innerProjectItem) return innerProjectItem;

  // 🔍 عنصر في قسم يسار
  const leftItem = btn.closest("li");
  if (leftItem) return leftItem;

  // 🔍 قسم كامل (يمين أو يسار)
  const sectionBlock = btn.closest(".project-section, .left-column > div");
  if (sectionBlock) return sectionBlock;

  return null;
}




function moveUp(btn) {
  const block = findMovableBlock(btn);
  const prev = block?.previousElementSibling;
  if (block && prev && block.parentNode === prev.parentNode) {
    block.parentNode.insertBefore(block, prev);
    addMoveEffect(block);
  }
}

function moveDown(btn) {
  const block = findMovableBlock(btn);
  const next = block?.nextElementSibling;
  if (block && next && block.parentNode === next.parentNode) {
    block.parentNode.insertBefore(next, block);
    addMoveEffect(block);
  }
}














function addLeftItem(targetUl) {
  const li = document.createElement("li");
  li.innerHTML = `
    <strong contenteditable>Label:</strong>
    <span contenteditable>Value</span>
  `;
  li.appendChild(createControlButtons({ showMove: true, moveType: "default" }));
  targetUl.appendChild(li);
}



function addProject(sectionId) {
  const container = document.querySelector(`#${sectionId}`);
  const box = document.createElement("div");
  box.className = "project-box";

  // ✅ إضافة أزرار التحكم للمشروع ككل
  const headerControls = document.createElement("div");
  headerControls.className = "project-header-controls edit-button";
  headerControls.style.textAlign = "right";
  headerControls.style.marginBottom = "6px";
  headerControls.appendChild(createControlButtons({ showMove: true, moveType: "project" }));
  box.appendChild(headerControls);

  // ✅ تعريف عناصر المشروع
  const fields = [
    { label: "Title:", content: "Project Title" },
    { label: "Date (from – to):", content: "Jan 2023 – Present" },
    { label: "Company:", content: "Company Name" },
    { label: "Description:", content: "Brief project description here..." },
    {
      label: "Link:",
      content: `<a href="https://example.com" target="_blank">https://example.com</a>`,
      isLink: true
    }
  ];

  fields.forEach(({ label, content, isLink }) => {
    const fieldDiv = document.createElement("div");
    fieldDiv.innerHTML = `
      <strong contenteditable>${label}</strong>
      <span contenteditable>${content}</span>
    `;
    fieldDiv.appendChild(createControlButtons({ showMove: true }));
    box.appendChild(fieldDiv);
  });

  container.appendChild(box);
}


function addLeftSection() {
  const leftColumn = document.querySelector(".left-column");
  const wrapper = document.createElement("div");
  const sectionId = `left-section-${Date.now()}`;

  // إنشاء عناصر HTML
  const h2 = document.createElement("h2");

  const titleSpan = document.createElement("span");
  titleSpan.contentEditable = true;
  titleSpan.textContent = "New Section";

  const controlSpan = createControlButtons();

  const ul = document.createElement("ul");
  ul.id = sectionId;

  const li = document.createElement("li");
  li.innerHTML = `
    <strong contenteditable>Label:</strong>
    <span contenteditable>Value</span>
  `;
  li.appendChild(createControlButtons());
  ul.appendChild(li);

  const addBtnWrapper = document.createElement("div");
  addBtnWrapper.className = "no-print";
  addBtnWrapper.style.textAlign = "right";
  addBtnWrapper.innerHTML = `<button class="add-left-item" data-target="${sectionId}">➕ Add Info</button>`;

  // تجميع المكونات
  h2.appendChild(titleSpan);
  h2.appendChild(controlSpan);
  wrapper.appendChild(h2);
  wrapper.appendChild(ul);
  wrapper.appendChild(addBtnWrapper);
  leftColumn.appendChild(wrapper);
}


function addProjectSection() {
  const rightSection = document.querySelector(".container > div:last-of-type");
  const sectionId = `projects-section-${Date.now()}`;
  const section = document.createElement("div");
  section.className = "project-section";
  section.id = sectionId;

  const h2 = document.createElement("h2");

  const titleSpan = document.createElement("span");
  titleSpan.contentEditable = true;
  titleSpan.textContent = "New Projects Section";

  const controlSpan = createControlButtons();

  const addBtnWrapper = document.createElement("div");
  addBtnWrapper.className = "no-print";
  addBtnWrapper.style.textAlign = "right";
  addBtnWrapper.style.marginBottom = "10px";
  addBtnWrapper.innerHTML = `<button class="add-project" data-section="${sectionId}">➕ New Project</button>`;

  // تجميع العناصر
  h2.appendChild(titleSpan);
  h2.appendChild(controlSpan);
  section.appendChild(h2);
  section.appendChild(addBtnWrapper);
  rightSection.appendChild(section);
}



function delegateEvents() {
  document.body.addEventListener("click", (e) => {
    const btn = e.target.closest("button");
    if (!btn) return;

    if (btn.matches("[data-edit]")) {
      editTextContent(document.getElementById(btn.dataset.edit));
    } else if (btn.matches("[data-edit-link]")) {
      editLinkContent(document.getElementById(btn.dataset.editLink));
    } else if (btn.matches("[data-delete]")) {
      deleteBlock(btn);
    } else if (btn.matches("[data-toggle-print]")) {
      togglePrint(btn);
    } else if (btn.matches("[data-move-up]")) {
      moveUp(btn);
    }else if (btn.matches("[data-move-down]")) {
      moveDown(btn);
    } else if (btn.matches("[data-move-project-up]")) {
      moveUp(btn);
    } else if (btn.matches("[data-move-project-down]")) {
      moveDown(btn);
    }
    else if (btn.id === "save-btn") {
          saveToLocalStorage();
    } else if (btn.id === "clear-btn") {
      clearStorage();
    } else if (btn.id === "edit-pic") {
      const newUrl = prompt("Enter image URL:");
      if (newUrl) {
        document.getElementById("profile-pic").src = newUrl;
      }
    } else if (btn.classList.contains("add-left-item")) {
      const ul = document.getElementById(btn.dataset.target);
      if (ul) addLeftItem(ul);
    } else if (btn.classList.contains("add-project")) {
      addProject(btn.dataset.section);
    } else if (btn.id === "add-left-section") {
      addLeftSection();
    } else if (btn.id === "add-project-section") {
      addProjectSection();
    }
  });
}

function restoreContent() {
  const saved = localStorage.getItem(STORAGE_KEY);
  if (saved) {
    document.querySelector(".container").innerHTML = saved;
  }
}

window.addEventListener("DOMContentLoaded", () => {
  restoreContent();
  delegateEvents();
});



