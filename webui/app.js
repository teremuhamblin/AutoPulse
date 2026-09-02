// ===============================
// AutoPulse WebUI v1.2.0
// ===============================

async function api(endpoint, method = "POST") {
  try {
    const r = await fetch(endpoint, { method });
    return await r.json().catch(() => ({}));
  } catch (e) {
    console.log("API error:", e);
    return { error: "connection_failed" };
  }
}

// ===============================
// ACTION BUTTONS
// ===============================

async function actionStart() {
  await api("/start");
}

async function actionStop() {
  await api("/stop");
}

async function actionTick() {
  await api("/tick");
}

async function actionSequence(name) {
  await api(`/sequence/${name}`);
}

// ===============================
// UI UPDATE
// ===============================

function updateState(data) {
  const el = document.getElementById("state");

  if (data.state === "RUNNING") {
    el.innerText = "RUNNING";
    el.className = "status-indicator running";
  } else {
    el.innerText = "STOPPED";
    el.className = "status-indicator stopped";
  }
}

function updatePanel(id, value) {
  document.getElementById(id).innerText =
    JSON.stringify(value || {}, null, 2);
}

function updateTimeline(data) {
  document.getElementById("timeline").innerText =
    JSON.stringify(data || [], null, 2);
}

// ===============================
// REFRESH LOOP
// ===============================

async function refresh() {
  const data = await api("/status", "GET");

  // Raw JSON
  updatePanel("raw", data);

  // State
  updateState(data);

  // IO
  updatePanel("io", data.io);

  // Events
  updatePanel("events", data.events);

  // Scheduler
  updatePanel("scheduler", data.scheduler);

  // Alarms
  updatePanel("alarms", data.alarms);

  // Timeline
  updateTimeline(data.timeline);
}

// Refresh every second
setInterval(refresh, 1000);
refresh();
