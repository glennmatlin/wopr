function filteredModels() {
  return STAGE3_MODELS.filter((model) => {
    return state.filter === "all" || model.tier === state.filter;
  });
}

function selectedModel() {
  return STAGE3_MODELS.find((model) => model.model === state.selected) || STAGE3_MODELS[0];
}

function selectedTier(modelName) {
  const model = STAGE3_MODELS.find((item) => item.model === modelName);
  return model ? model.tier : "all";
}

function compareModels(left, right) {
  if (state.sort === "tier") return left.tier.localeCompare(right.tier) || right.done - left.done;
  if (state.sort === "spoken") return right.spoken - left.spoken || left.cost - right.cost;
  if (state.sort === "completion") return right.done - left.done || left.cost - right.cost;
  return left.cost - right.cost || right.done - left.done;
}

function renderMetric([label, value]) {
  return `<article class="metric"><span>${escapeHtml(label)}</span><strong>${value}</strong></article>`;
}

function renderStep([label, text]) {
  return `<li><strong>${escapeHtml(label)}</strong><span>${escapeHtml(text)}</span></li>`;
}

function renderSample(sample) {
  return `<blockquote><p>${escapeHtml(sample.text)}</p><footer>${escapeHtml(sample.model)} - ${escapeHtml(sample.speaker)}</footer></blockquote>`;
}

function formatMoney(value) {
  return `$${value.toFixed(value < 0.1 ? 6 : 3)}`;
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (match) => {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" }[match];
  });
}
