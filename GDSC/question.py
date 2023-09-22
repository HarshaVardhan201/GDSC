class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def is_correct(self, user_answer):
        return user_answer.lower() == self.answer.lower()
