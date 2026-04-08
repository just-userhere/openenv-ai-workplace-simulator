# 🚀 AI Workplace Simulator (OpenEnv)

> A production-ready **OpenEnv environment** that simulates real-world workplace tasks to evaluate AI agents beyond toy benchmarks.

---

## 🌟 Overview

The **AI Workplace Simulator** is designed to test how well AI agents perform **practical, human-like tasks** such as:

* 📧 Email triage
* 💻 Code review & debugging
* 🧹 Data cleaning & normalization

Unlike traditional benchmarks, this environment focuses on **real-world productivity scenarios**.

---

## 🎯 Motivation

Most AI evaluations rely on synthetic or narrow tasks.

This project aims to:

* Bridge the gap between **theory and real-world AI usage**
* Evaluate **decision-making, reasoning, and execution**
* Provide a **standardized OpenEnv-compatible benchmark**

> 💡 *Learning matters, but applying it makes the difference.*

---

## 🧠 Tasks (Easy → Hard)

### 🟢 1. Email Triage (Easy)

* Classify emails into:

  * `spam`
  * `important`
  * `normal`
* Evaluates: **classification + prioritization**

---

### 🟡 2. Code Review & Fixing (Medium)

* Fix buggy Python/JavaScript code
* Handles:

  * Logical errors
  * Syntax errors
* Evaluates: **debugging + reasoning**

---

### 🔴 3. Data Cleaning (Hard)

* Clean messy datasets (JSON/CSV-like)
* Tasks include:

  * Normalizing text
  * Fixing types
  * Structuring data
* Evaluates: **data preprocessing + consistency**

---

## 🧩 OpenEnv Compliance

This project strictly follows the **OpenEnv specification**:

* ✅ Typed `Observation`, `Action`, `Reward` (Pydantic)
* ✅ Standard API:

  * `reset()`
  * `step(action)`
  * `state()`
* ✅ `openenv.yaml` configuration
* ✅ Deterministic graders per task

---

## 🔍 Observation Space

```json
{
  "task_type": "string",
  "input_data": "any",
  "step_count": "integer"
}
```

---

## 🎮 Action Space

```json
{
  "response": "any"
}
```

---

## 🏆 Reward System

* Score range: **0.0 → 1.0**
* Based on:

  * ✔ Correctness
  * ✔ Completeness
  * ✔ Format

### ⚖ Reward Shaping

* Incremental rewards for partial correctness
* Penalties for:

  * ❌ Invalid outputs
  * ❌ Incorrect logic
  * ❌ Multiple failed steps

---

## ⚙️ Project Structure

```
openenv-ai-workplace/
│
├── env/
│   ├── environment.py
│   ├── tasks/
│   ├── graders/
│
├── scripts/
│   ├── run_inference.py
│
├── openenv.yaml
├── Dockerfile
├── requirements.txt
├── README.md
```

---

## 🛠️ Setup Instructions

### 🔹 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-workplace-simulator-openenv.git
cd ai-workplace-simulator-openenv
```

### 🔹 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 3. Set API Key

```bash
export HF_TOKEN=your_openai_api_key
```

---

## ▶️ Run the Environment

```bash
python scripts/run_inference.py
```

---

## 🐳 Run with Docker

### Build

```bash
docker build -t openenv-app .
```

### Run

```bash
docker run -e HF_TOKEN=your_openai_api_key openenv-app
```

---

## 📊 Baseline Results

| Task          | Score |
| ------------- | ----- |
| Email Triage  | ~0.9  |
| Code Review   | ~0.8  |
| Data Cleaning | ~0.7  |

**Final Average:** ~0.8

---

## 🚀 Key Features

* 🔹 Real-world task simulation
* 🔹 Deterministic evaluation system
* 🔹 Reward shaping mechanism
* 🔹 Fully Dockerized
* 🔹 OpenEnv compliant

---

## 🔮 Future Improvements

* 🧠 Multi-step reasoning tasks
* 🤖 Multi-agent evaluation
* 📊 Leaderboard system
* 🌐 Web dashboard (React + Firebase)
* 📦 Larger and more complex datasets

---

## 🏷️ Tags

`openenv` `ai-agents` `evaluation` `benchmark` `machine-learning` `hackathon`

---

## 👨‍💻 Author

Built with ❤️ for the **Meta OpenEnv Hackathon**

---

## ⭐ Support

If you like this project:

👉 Star the repo
👉 Share with others
👉 Contribute improvements

---

> 🚀 *From learning to real-world impact — this is where AI meets work.*
