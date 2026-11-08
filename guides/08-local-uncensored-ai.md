# 🧠 Local Uncensored AI & Autonomous Coding Agent Blueprint

> A comprehensive reference guide for running, abliterating, and fine-tuning private, zero-refusal AI models on your own GPU to rival Claude Code, GPT-4, and cloud coding agents.

---

## 🧭 Executive Summary: How to Rival Cloud AI for $0

You do **not** need $50M+ to pre-train an AI from scratch. Instead, the modern open-source playbook is:
1. **Leverage Frontier Open Weights:** Open-source teams (Alibaba's Qwen Coder, DeepSeek, Meta's Llama) spend hundreds of millions training world-class base models and release the raw weights for free.
2. **Abliterate (Remove Refusals):** Mathematically isolate and neutralize the model's refusal vectors using open tools (like *Heretic*). This creates a 100% uncensored model without degrading intelligence.
3. **Agentic Harness & Tool Integration:** Run the model locally through **Ollama** or **vLLM** and connect it directly to terminal developer agents like **Claude Code**, **Aider**, or **Continue.dev**.

---

## 🖥️ Hardware Blueprint: What to Buy When You're Ready

To run models that match or exceed GPT-4/Claude 3.5 Sonnet on coding tasks, you need enough **VRAM (Video Memory)** to fit 32B to 70B parameter models:

| Tier | Hardware Setup | Total VRAM / Memory | Estimated Price | Model Capabilities |
| :--- | :--- | :--- | :--- | :--- |
| **Sweet Spot (Best Value)** | **1x Nvidia RTX 3090** (Used) | **24 GB GDDR6X** | ~$650 – $750 | Runs **14B–32B** coding models (e.g., `Qwen-2.5-Coder-32B`) at 40–50 tokens/sec. QLoRA fine-tuning enabled. |
| **High-End Enthusiast** | **1x Nvidia RTX 4090 / 5090** | **24 GB GDDR6X** | ~$1,600 – $1,900 | Maximum inference speed and fastest LoRA fine-tuning training times. |
| **The 70B Powerhouse** | **2x Nvidia RTX 3090** (Dual GPU) | **48 GB Combined** | ~$1,300 – $1,500 | Runs full **70B** models (e.g., `Llama-3.3-70B`, `DeepSeek-Coder-33B`) uncompressed with large context. |
| **Silent Mac Setup** | **Apple Mac Studio** (M2/M3/M4 Max/Ultra) | **64 GB – 128 GB Unified** | ~$2,000 – $3,500 | Runs massive 70B+ models completely in unified memory with low power draw and silent cooling. |

*(Note: Your current GTX 1050 with 2GB–4GB VRAM is great for small 3B–4B models like Qwen-3-4B, but the tiers above are what unlock Claude-rivaling intelligence).*

---

## ⚡ The 4-Step Execution Guide

### Step 1: Install & Configure Ollama
Ollama serves local models through an OpenAI / Anthropic compatible REST API:
```bash
# Linux / WSL2
curl -fsSL https://ollama.com/install.sh | sh
```
* **Critical Setting — Expand Context Length:**
  Ollama defaults to 4k tokens. Agentic coding tools (like Claude Code) send system prompts larger than that. Always launch Ollama with expanded context:
  ```bash
  export OLLAMA_CONTEXT_LENGTH=32768
  ollama serve
  ```

---

### Step 2: Choose & Pull Your Model

Avoid random community tags that don't publish benchmark scores. Stick to tested abliterations:

#### 1. Coding & Logic Specialist (Top Recommendation):
* **Model:** `Qwen/Qwen2.5-Coder-32B-Instruct` (or its abliterated variant)
* **Why:** The reigning open-source king of coding, scoring on par with GPT-4o on SWE-bench and HumanEval.

#### 2. Hybrid Reasoning / Uncensored Generalist:
* **Model:** `igorls/gemma-4-12B-it-heretic-GGUF`
* **Why:** Abliterated with *Heretic*, reducing refusals from 99/100 to 0/100 while keeping base reasoning intact.

To pull via Ollama:
```bash
ollama pull igorls/gemma-4-12B-it-heretic-GGUF
```

---

### Step 3: Turn Off Chain-of-Thought "Thinking" (For Gemma/Hybrid Models)
Hybrid reasoning models spend tokens generating internal monologue blocks (`<thought>...</thought>`). When using coding agents, this can exhaust your context budget:
```bash
# In Ollama interactive CLI:
ollama run igorls/gemma-4-12B-it-heretic-GGUF
/set nothink

# Or in API calls, pass:
# {"think": false}
```

---

### Step 4: Hook into Claude Code (Zero API Cost)

Because recent Ollama versions emulate Anthropic's API endpoint, you can drop your local model into Anthropic's **Claude Code** CLI:

```bash
# Point Claude Code to your local Ollama port
export ANTHROPIC_BASE_URL=http://localhost:11434
export ANTHROPIC_AUTH_TOKEN=ollama

# Launch Claude Code powered by your own GPU
claude --model igorls/gemma-4-12B-it-heretic-GGUF
```

Alternatively, use other top-tier open-source coding harnesses:
* **Aider (`pip install aider-chat`):** Best-in-class Git-integrated terminal coding agent. Run with:
  ```bash
  aider --model ollama/qwen2.5-coder:32b
  ```
* **Continue.dev:** VS Code / JetBrains extension for inline autocompletion and side-panel refactoring powered by your local Ollama instance.

---

## 🛠️ How to Abliterate Any Model Yourself (Heretic Method)

If a new, smarter model comes out and you want to remove its censorship guardrails yourself:

1. **Clone the Heretic Repository:**
   ```bash
   git clone https://github.com/p-e-w/heretic.git
   cd heretic
   pip install -r requirements.txt
   ```
2. **Calculate Refusal Directions:**
   Heretic runs paired contrastive prompts (e.g., harmless requests vs. sensitive requests) and finds the exact mathematical direction where the model decides to say *"I cannot assist with that"*.
3. **Neutralize the Weights:**
   The script projects out the refusal vectors from the attention/MLP layers and saves a clean, refusal-free GGUF file.

---

## 🎯 Golden Rules to Remember
1. **Uncensored ≠ Smarter:** Abliteration removes refusals; it does not add intelligence. Always start with a model that already has top-tier benchmark scores (like Qwen 2.5 Coder or DeepSeek).
2. **VRAM is King:** Model speed is governed by memory bandwidth, not raw compute. A GPU with 24GB VRAM will run circles around a 16GB GPU trying to swap to system RAM.
3. **Total Privacy:** The ultimate win of this architecture is complete data ownership. Your proprietary code, financial logs, and prompts never touch third-party servers.

---
*Created: 2026-11-07 • Stored in `Dartdark/homelab` (`guides/08-local-uncensored-ai.md`)*
