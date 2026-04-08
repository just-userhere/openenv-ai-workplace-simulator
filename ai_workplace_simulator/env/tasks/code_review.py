class CodeReviewTask:
    def __init__(self):
        self.name = "code_review"
        self.buggy_code = (
            "def calculate_discount(price, discount_percent):\n"
            "    if discount_percent > 100\n"
            "        return price\n"
            "    return price + (price * (discount_percent / 100))\n"
        )

    def get_input(self) -> str:
        return self.buggy_code

    def evaluate(self, action_output: str) -> tuple[float, str]:
        code = action_output.replace("```python", "").replace("```", "").strip()
        try:
            compiled = compile(code, '<string>', 'exec')
            test_namespace = {}
            exec(compiled, test_namespace)
            func = test_namespace['calculate_discount']
            
            if func(100, 20) == 80 and func(50, 100) == 0:
                return 1.0, "All tests passed!"
            return 0.5, "Syntax valid, but logic tests failed."
        except Exception as e:
             return 0.0, f"Error: {str(e)}"
