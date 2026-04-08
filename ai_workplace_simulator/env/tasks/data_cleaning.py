import io
import pandas as pd

class DataCleaningTask:
    def __init__(self):
        self.name = "data_cleaning"
        self.messy_csv = "user_id,Name,Spend\n1,john doe,100.50\n2,bob,NaN\n"
        self.instructions = "Capitalize names and fill missing Spend with 0.0. Return ONLY CSV text."

    def get_input(self) -> str:
        return f"{self.instructions}\n\n{self.messy_csv}"

    def evaluate(self, action_output: str) -> tuple[float, str]:
        clean_csv_str = action_output.replace("```csv", "").replace("```", "").strip()
        try:
            df = pd.read_csv(io.StringIO(clean_csv_str))
            if df.iloc[0]['Name'] == 'John Doe' and df.iloc[1]['Spend'] == 0.0:
                return 1.0, "Cleaned perfectly."
            return 0.5, "Format rules not fully met."
        except Exception as e:
            return 0.0, f"Invalid CSV: {str(e)}"
