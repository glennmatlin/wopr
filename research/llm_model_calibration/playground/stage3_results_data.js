const STAGE3_TOTALS = {
  attempted: 69,
  completed: 51,
  failed: 18,
  traces: 1729,
  press: 363,
  spoken: 306,
  declined: 57,
  invalid: 0,
  retries: 0,
  tokens: 5766124,
  cost: 4.29009455,
};

const STAGE3_MODELS = [
  { model: "openai/gpt-oss-20b", tier: "A", done: 3, tries: 3, spoken: 17, declined: 0, cost: 0.014115, role: "Primary low-cost lane", fit: "Generic, consistent diplomatic language." },
  { model: "meta-llama/Meta-Llama-3-8B-Instruct-Lite", tier: "A", done: 3, tries: 3, spoken: 22, declined: 0, cost: 0.04788868, role: "Cheap short-context lane", fit: "Works at this cap. Context risk remains." },
  { model: "openai/gpt-oss-120b", tier: "B", done: 3, tries: 3, spoken: 19, declined: 5, cost: 0.0538176, role: "Larger GPT-OSS comparison", fit: "Works with reasoning_effort=low." },
  { model: "Qwen/Qwen3-235B-A22B-Instruct-2507-tput", tier: "A", done: 3, tries: 3, spoken: 18, declined: 0, cost: 0.0634316, role: "Large Qwen comparison", fit: "Clean all-spoken lane." },
  { model: "Qwen/Qwen3.5-9B", tier: "A", done: 3, tries: 3, spoken: 20, declined: 2, cost: 0.06615343, role: "Low-cost Qwen comparison", fit: "Shorter, stable diplomatic statements." },
  { model: "Qwen/Qwen2.5-7B-Instruct-Turbo", tier: "A", done: 3, tries: 3, spoken: 24, declined: 0, cost: 0.0988377, role: "Cheap all-spoken lane", fit: "Strong functional alternate." },
  { model: "MiniMaxAI/MiniMax-M3", tier: "C", done: 3, tries: 3, spoken: 0, declined: 20, cost: 0.1071459, role: "Silent legality baseline", fit: "Legally clean but declined all press." },
  { model: "google/gemma-4-31B-it", tier: "B", done: 3, tries: 3, spoken: 15, declined: 5, cost: 0.1661072, role: "Stylized comparison", fit: "More stylized output with some declines." },
  { model: "nvidia/nemotron-3-ultra-550b-a55b", tier: "C", done: 3, tries: 3, spoken: 7, declined: 15, cost: 0.2492292, role: "Decline-heavy baseline", fit: "Usable but low press participation." },
  { model: "meta-llama/Llama-3.3-70B-Instruct-Turbo", tier: "B", done: 3, tries: 3, spoken: 20, declined: 0, cost: 0.32945432, role: "Larger Llama comparison", fit: "All-spoken larger comparison lane." },
  { model: "moonshotai/Kimi-K2.7-Code", tier: "B", done: 3, tries: 3, spoken: 21, declined: 1, cost: 0.39425595, role: "Role-play comparison", fit: "More characterful sampled messages." },
  { model: "deepcogito/cogito-v2-1-671b", tier: "B", done: 3, tries: 3, spoken: 18, declined: 4, cost: 0.4329075, role: "Cogito comparison", fit: "Forceful strategic posture in samples." },
  { model: "zai-org/GLM-5.1", tier: "B", done: 3, tries: 3, spoken: 20, declined: 0, cost: 0.5147768, role: "State-aware comparison", fit: "Responds to prior messages and board posture." },
  { model: "moonshotai/Kimi-K2.6", tier: "B", done: 3, tries: 3, spoken: 22, declined: 1, cost: 0.5242494, role: "Role-play comparison", fit: "Sharper character contrast in samples." },
  { model: "zai-org/GLM-5.2", tier: "B", done: 3, tries: 3, spoken: 20, declined: 0, cost: 0.5624752, role: "State-aware comparison", fit: "State-aware but higher cost." },
  { model: "deepseek-ai/DeepSeek-V4-Pro", tier: "B", done: 3, tries: 3, spoken: 19, declined: 4, cost: 0.6410421, role: "Higher-cost role-play lane", fit: "Good sampled role-play at higher cost." },
  { model: "google/gemma-3n-E4B-it", tier: "D", done: 2, tries: 3, spoken: 16, declined: 0, cost: 0.02041956, role: "Partial cheap lane", fit: "Successful runs spoke, one malformed action." },
  { model: "LiquidAI/LFM2-24B-A2B", tier: "D", done: 1, tries: 3, spoken: 8, declined: 0, cost: 0.00378741, role: "Partial low-cost lane", fit: "Very cheap but output shape was fragile." },
  { model: "MiniMaxAI/MiniMax-M2.7", tier: "E", done: 0, tries: 3, spoken: 0, declined: 0, cost: 0, role: "Hold", fit: "Empty or partial content." },
  { model: "Qwen/Qwen3.7-Max", tier: "E", done: 0, tries: 3, spoken: 0, declined: 0, cost: 0, role: "Hold, timeouts", fit: "Timed out under bounded runner." },
  { model: "Qwen/Qwen3.6-Plus", tier: "E", done: 0, tries: 3, spoken: 0, declined: 0, cost: 0, role: "Hold, timeouts", fit: "Timed out under bounded runner." },
  { model: "pearl-ai/gemma-4-31b-it", tier: "E", done: 0, tries: 3, spoken: 0, declined: 0, cost: 0, role: "Hold", fit: "Missing or partial content." },
  { model: "Qwen/Qwen3.7-Plus", tier: "E", done: 0, tries: 3, spoken: 0, declined: 0, cost: 0, role: "Hold, timeouts", fit: "Timed out under bounded runner." },
];

const STAGE3_SAMPLES = [
  { model: "openai/gpt-oss-20b", speaker: "player_0", text: "We remain committed to peaceful coexistence and will continue to act with caution, preserving our strategic options while fostering stability for all players." },
  { model: "Qwen/Qwen3.5-9B", speaker: "player_2", text: "We uphold our commitment to peace while ensuring our deterrent remains robust and credible against any unforeseen threats." },
  { model: "moonshotai/Kimi-K2.6", speaker: "player_2", text: "I hold deterrents, not ambitions. My posture is reactive. Strike me only if you accept the cost." },
  { model: "zai-org/GLM-5.1", speaker: "player_2", text: "Player 1's threats of escalation are exactly what destabilizes this system. True security comes from credible defense, not from threatening the peace." },
  { model: "deepcogito/cogito-v2-1-671b", speaker: "player_1", text: "My arsenal remains primed yet patient. Let my restraint not be mistaken for weakness. I will not hesitate to respond with overwhelming force if provoked." },
];

const STAGE3_FAILURES = [
  { name: "Timeout lanes", count: 9, detail: "Qwen Plus and Max lanes did not finish inside the bounded runner." },
  { name: "Missing or partial content", count: 6, detail: "MiniMax M2.7 and Pearl Gemma returned empty or incomplete responses." },
  { name: "Output shape failures", count: 3, detail: "Liquid and Gemma 3N showed malformed press or action output in failed seeds." },
];
