let allProjects = [];

function setButtonLoading(id, message) {
  const card = document.getElementById(`project-${id}`);
  if (!card) return;
  card.querySelector(".project-actions").innerHTML = `<span class="status-stopped">⏳ ${message}</span>`;
}

async function waitUntilProjectStatus(id, expectedKeyword, timeout = 10000, interval = 1000) {
  const start = Date.now();
  while (Date.now() - start < timeout) {
    const res = await fetch("/projects");
    const projects = await res.json();
    const project = projects.find(p => p.id === id);

    console.log(`🔍 Checking status of project ${id}:`, project?.status); // Debug log

    if (project?.status && project.status.includes(expectedKeyword)) return true;
    await new Promise(r => setTimeout(r, interval));
  }
  return false;
}

async function startProject(id) {
  setButtonLoading(id, "Starting...");
  await fetch(`/start/${id}`, { method: "POST" });
  await waitUntilProjectStatus(id, "Running");
  loadProjects();
}

async function stopProject(id) {
  setButtonLoading(id, "Stopping...");
  await fetch(`/stop/${id}`, { method: "POST" });
  await waitUntilProjectStatus(id, "Stopped");
  loadProjects();
}

async function restartProject(id) {
  setButtonLoading(id, "Restarting...");
  await fetch(`/restart/${id}`, { method: "POST" });
  await waitUntilProjectStatus(id, "Running");
  loadProjects();
}

async function deleteProject(id) {
  if (!confirm("⚠️ Are you sure you want to delete this project?")) return;
  const res = await fetch(`/delete/${id}`, { method: "POST" });
  const result = await res.json();
  alert(result.message);
  await loadProjects();
}


async function addProject(event) {
  event.preventDefault();
  const data = {
    name: document.getElementById("name").value,
    type: document.getElementById("type").value,
    path: document.getElementById("path").value,
    entry: document.getElementById("entry").value,
    port: parseInt(document.getElementById("port").value),
  };

  const res = await fetch("/add", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const result = await res.json();
  alert(result.message);
  await loadProjects();
  document.getElementById("add-form").reset();
}

async function loadProjects() {
  const res = await fetch("/projects");
  const projects = await res.json();
  allProjects = projects;
  const list = document.getElementById("project-list");
  list.innerHTML = "";
  projects.forEach(project => renderProjectCard(project));
}

function renderProjectCard(project) {
  const list = document.getElementById("project-list");

  const card = document.createElement("div");
  card.className = "project-card";
  card.id = `project-${project.id}`;

  card.innerHTML = `
    <h3>📄 ${project.name}</h3>
    <div class="project-details">
      <p><strong>Type:</strong> ${project.type}</p>
      <p><strong>Port:</strong> ${project.port}</p>
      <p><strong>Entry:</strong> ${project.entry || "undefined"}</p>
    </div>
    <div class="project-actions">
      ${project.status.includes("Running")
        ? `
        <button class="stop" onclick="stopProject(${project.id})">⏹️ Stop</button>
        <button class="restart" onclick="restartProject(${project.id})">🔄 Restart</button>`
        : `<button class="start" onclick="startProject(${project.id})">▶️ Start</button>`
      }
      <button class="delete" onclick="deleteProject(${project.id})">🗑️ Delete</button>
      <a class="open" href="http://localhost:${project.port}" target="_blank">🌐 Open</a>
      <span class="status-stopped ${project.status.includes("Running") ? "running" : ""}">
        ${project.status}
      </span>
    </div>
  `;

  list.appendChild(card);
}



window.addEventListener("DOMContentLoaded", loadProjects);
