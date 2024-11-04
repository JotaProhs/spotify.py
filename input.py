class InputHandler:
    @staticmethod
    def get_choice(prompt, valid_choices):
        while True:
            choice = input(prompt).strip()
            if choice in valid_choices:
                return choice

            print(f"{choice} is not a valid option. Try again.")

    @staticmethod
    def get_text_input(prompt):
        while True:
            text = input(prompt).strip()
            if text:
                return text

            print("Input cannot be empty. Please enter a valid text.")
