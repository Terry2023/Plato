# 🏛 Plato: Collective Cognition Simulation Engine

Plato is a multi-agent environment designed to simulate collective cognition through competing, MBTI-driven persona nodes. Unlike standard sequential LLM frameworks, Plato fosters emergent systemic coherence by allowing autonomous agents to negotiate, audit, and refine information in a non-linear, resource-competitive environment.

---

## 🧠 Systemic Philosophy

Traditional AI frameworks treat agents as static, linear contributors. Plato treats them as a living ecosystem. 

By utilizing persistent agent identities (e.g., Elias, Luna, Rhea) and a recursive Logic Editor that performs automated audits on the system's output, the engine creates a self-correcting loop that discourages "homogenous agreement" and encourages deep, systemic reasoning.

## 🏗️ Architectural Resilience

- **Recursive Feedback Loops**: The Logic Editor acts as an automated auditor, identifying "drift" and structural inconsistencies in the generated narrative state.
- **Agentic Persistence**: Agents maintain unique identities and self-defined nomenclatures, preventing "robotic" output through sustained personality memory.
- **Stateful Memory**: Session state is managed via `.canvas` files, allowing for historical audits and mid-simulation mutation of personality nodes.
- **Hardware Optimized**: Designed to operate on local silicon (AMD 7950X / RTX 4070 / 64GB RAM), ensuring low-latency execution for complex cognitive simulations.

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/Terry2023/Plato.git
cd Plato
```

### 2. Launch the cognitive hive
```bash
# Utilizing Docker for isolated agent simulation
docker-compose up --build
```

### 3. Initiate a simulation session
```bash
python src/main.py --session [SESSION_ID]
```

### 4. Audit systemic consensus
- Open the generated `.canvas` files in the `vault/` directory to visualize node interactions
- Review the `hive_session_*.md` files to analyze collective logic evolution

> **Note:** Each session functions as an isolated collective cognition test. The system relies on MBTI-driven persona injection to diversify model output. Modify `src/config/personas.json` to alter the "hive" composition.

---

## 📁 Repository Structure
```
Plato/
├── src/
│   ├── main.py
│   └── config/
│       └── personas.json
├── vault/
│   └── *.canvas
├── docker-compose.yml
└── README.md
```

## 🧩 Core Concepts

**Collective Cognition**: Not voting, not averaging — negotiation under resource constraints.

**MBTI-Driven Personas**: 16 cognitive archetypes provide inherent diversity, preventing model collapse.

**Logic Editor**: Automated auditor, not a moderator. It flags drift, it doesn't enforce consensus.

## 📜 License

Open research — see LICENSE file for details.

---

**Author**: Terry Schermerhorn  
**GitHub**: [Terry2023/Plato](https://github.com/Terry2023/Plato)  
**Kosmos**: https://terry2023.github.io/Kosmos/

