# AI Workplace Simulator

## Project Overview
The AI Workplace Simulator is a production-ready OpenEnv environment designed to evaluate an AI agent's performance on real-world office tasks. It features a progressive difficulty curve and robust deterministic grading.

## Setup Instructions
1. `pip install -r requirements.txt`
2. Export your OpenAI API key: `export HF_TOKEN="your-api-key-here"`
3. Run: `python scripts/run_inference.py`

### Docker
1. `docker build -t openenv-app .`
2. `docker run -e HF_TOKEN="your-api-key-here" openenv-app`
