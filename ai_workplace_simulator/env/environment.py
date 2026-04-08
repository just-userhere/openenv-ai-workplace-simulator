from pydantic import BaseModel
from typing import Any, Tuple, Dict
from .tasks import EmailTriageTask, CodeReviewTask, DataCleaningTask

class Observation(BaseModel):
    task_name: str
    instruction: str
    payload: str

class Action(BaseModel):
    task_name: str
    output: str

class Reward(BaseModel):
    score: float
    feedback: str
    is_done: bool

class AIWorkplaceEnv:
    def __init__(self):
        self.tasks = [EmailTriageTask(), CodeReviewTask(), DataCleaningTask()]
        self.current_task_idx = 0
        self.done = False

    def reset(self) -> Observation:
        self.current_task_idx = 0
        self.done = False
        return self.state()

    def state(self) -> Observation:
        if self.done:
            return Observation(task_name="finished", instruction="Done.", payload="")
        current_task = self.tasks[self.current_task_idx]
        return Observation(task_name=current_task.name, instruction="Process the payload.", payload=current_task.get_input())

    def step(self, action: Action) -> Tuple[Observation, Reward, bool, Dict[str, Any]]:
        current_task = self.tasks[self.current_task_idx]
        score, feedback = current_task.evaluate(action.output)
        
        self.current_task_idx += 1
        if self.current_task_idx >= len(self.tasks):
            self.done = True

        return self.state(), Reward(score=score, feedback=feedback, is_done=self.done), self.done, {}
