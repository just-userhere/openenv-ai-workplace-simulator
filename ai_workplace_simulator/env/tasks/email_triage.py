import json

class EmailTriageTask:
    def __init__(self):
        self.name = "email_triage"
        self.emails = [
            {"id": "e1", "sender": "boss@company.com", "subject": "URGENT", "body": "Need this in 5 mins!"},
            {"id": "e2", "sender": "promo@buy-now.xyz", "subject": "Enlarge your audience", "body": "Click here for 50% off!"},
            {"id": "e3", "sender": "hr@company.com", "subject": "Lunch menu", "body": "Pizza today."}
        ]
        self.ground_truth = {"e1": "important", "e2": "spam", "e3": "normal"}

    def get_input(self) -> str:
        return json.dumps(self.emails, indent=2)

    def evaluate(self, action_output: str) -> tuple[float, str]:
        try:
            prediction = json.loads(action_output)
            correct = sum(1 for e_id, true_cat in self.ground_truth.items() if prediction.get(e_id) == true_cat)
            return correct / len(self.ground_truth), f"Categorized {correct}/{len(self.ground_truth)} correctly."
        except json.JSONDecodeError:
            return 0.0, "Invalid JSON format."
