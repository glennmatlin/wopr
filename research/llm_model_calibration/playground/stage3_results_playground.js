const state = { filter: "all", sort: "cost", selected: "openai/gpt-oss-20b" };
const tierLabels = {
  all: "All lanes",
  A: "Tier A primary",
  B: "Tier B comparison",
  C: "Tier C baselines",
  D: "Tier D partial",
  E: "Tier E hold",
};

function main() {
  renderSummary();
  renderTimeline();
  renderFailures();
  bindControls();
  render();
}

function bindControls() {
  document.querySelectorAll("[data-filter]").forEach((button) => {
    button.addEventListener("click", handleFilterClick);
  });
  document.querySelector("#sort-models").addEventListener("change", handleSortChange);
}

function handleFilterClick(event) {
  state.filter = event.currentTarget.dataset.filter;
  render();
}

function handleSortChange(event) {
  state.sort = event.currentTarget.value;
  render();
}

function handleModelClick(event) {
  state.selected = event.currentTarget.dataset.model;
  render();
}

function render() {
  renderFilters();
  renderModelRows();
  renderDetail();
  renderSamples();
}

function renderSummary() {
  const values = [
    ["Attempted runs", STAGE3_TOTALS.attempted],
    ["Completed runs", STAGE3_TOTALS.completed],
    ["Press messages", STAGE3_TOTALS.press],
    ["Spoken messages", STAGE3_TOTALS.spoken],
    ["Invalid actions", STAGE3_TOTALS.invalid],
    ["Catalog cost", formatMoney(STAGE3_TOTALS.cost)],
  ];
  document.querySelector("#summary-grid").innerHTML = values.map(renderMetric).join("");
}

function renderTimeline() {
  const steps = [
    ["Stage 1", "Surveyed the official serverless chat catalog and built the full candidate list."],
    ["Stage 2", "Ran low-cost calibration and found parser, timeout, and provider-shape issues."],
    ["Repair", "Recovered fenced JSON, empty-content handling, stale snapshots, and GPT-OSS low reasoning."],
    ["Stage 3", "Ran 23 model lanes across 3 seeds each under the same press-light controls."],
    ["Policy", "Promoted every functioning lane so later LLM games can test variety, not only price."],
  ];
  document.querySelector("#timeline").innerHTML = steps.map(renderStep).join("");
}

function renderFailures() {
  const total = STAGE3_FAILURES.reduce((sum, item) => sum + item.count, 0);
  document.querySelector("#failure-list").innerHTML = STAGE3_FAILURES.map((item) => {
    const width = total ? (item.count / total) * 100 : 0;
    return `<article class="failure"><div><strong>${item.count}</strong><span>${escapeHtml(item.name)}</span></div><p>${escapeHtml(item.detail)}</p><meter min="0" max="100" value="${width}"></meter></article>`;
  }).join("");
}

function renderFilters() {
  document.querySelectorAll("[data-filter]").forEach((button) => {
    button.classList.toggle("active", button.dataset.filter === state.filter);
  });
  document.querySelector("#active-filter").textContent = tierLabels[state.filter];
}

function renderModelRows() {
  const models = filteredModels().sort(compareModels);
  document.querySelector("#model-count").textContent = `${models.length} shown`;
  document.querySelector("#model-list").innerHTML = models.map(renderModelRow).join("");
  document.querySelectorAll(".model-row").forEach((row) => {
    row.addEventListener("click", handleModelClick);
  });
}

function renderModelRow(model) {
  const totalPress = model.spoken + model.declined;
  const spokenRate = totalPress ? Math.round((model.spoken / totalPress) * 100) : 0;
  const completeRate = Math.round((model.done / model.tries) * 100);
  const active = model.model === state.selected ? " active" : "";
  return `<button class="model-row${active}" data-model="${escapeHtml(model.model)}">
    <span class="tier tier-${model.tier}">${model.tier}</span>
    <span class="model-name">${escapeHtml(model.model)}</span>
    <span>${model.done}/${model.tries}</span>
    <span>${model.spoken}/${model.declined}</span>
    <span>${formatMoney(model.cost)}</span>
    <meter class="bar" min="0" max="100" value="${completeRate}"></meter>
    <meter class="bar speech" min="0" max="100" value="${spokenRate}"></meter>
  </button>`;
}

function renderDetail() {
  const model = selectedModel();
  const press = model.spoken + model.declined;
  const speechRate = press ? `${Math.round((model.spoken / press) * 100)}%` : "n/a";
  document.querySelector("#detail").innerHTML = `
    <h3>${escapeHtml(model.model)}</h3>
    <dl>
      <div><dt>Tier</dt><dd>${model.tier}</dd></div>
      <div><dt>Run status</dt><dd>${model.done}/${model.tries}</dd></div>
      <div><dt>Speech rate</dt><dd>${speechRate}</dd></div>
      <div><dt>Cost</dt><dd>${formatMoney(model.cost)}</dd></div>
    </dl>
    <p><strong>${escapeHtml(model.role)}</strong></p>
    <p>${escapeHtml(model.fit)}</p>`;
}

function renderSamples() {
  const samples = STAGE3_SAMPLES.filter((sample) => {
    return state.filter === "all" || selectedTier(sample.model) === state.filter;
  });
  const sampleHtml = samples.length
    ? samples.map(renderSample).join("")
    : `<p class="empty">No sampled spoken output for this filter.</p>`;
  document.querySelector("#samples").innerHTML = sampleHtml;
}

document.addEventListener("DOMContentLoaded", main);
