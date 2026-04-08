import os
import sys
from openai import OpenAI

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from env import AIWorkplaceEnv, Action

def run_baseline():
    api_key = os.environ.get("HF_TOKEN")
    if not api_key:
        print("Error: HF_TOKEN environment variable not set.")
        sys.exit(1)

    client = OpenAI(api_key=api_key)
    environment = AIWorkplaceEnv()
    obs = environment.reset()
    
    while not environment.done:
        print(f"Task: {obs.task_name}")
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": f"{obs.instruction}\n{obs.payload}"}]
        )
        action = Action(task_name=obs.task_name, output=response.choices[0].message.content)
        obs, reward, done, _ = environment.step(action)
        print(f"Score: {reward.score} - Feedback: {reward.feedback}\n")

if __name__ == "__main__":
    run_baseline()
