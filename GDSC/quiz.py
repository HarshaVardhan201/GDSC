from question import Question

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_question_index = 0
        self.score = 0

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def check_answer(self, user_answer):
        question = self.questions[self.current_question_index - 1]
        if user_answer.lower() == "skip":
            pass  # User chose to skip, no effect on the score
        elif question.is_correct(user_answer):
            self.score += 2
        else:
            self.score -= 1

    def do_questions_remain(self):
        return self.current_question_index < len(self.questions)

    def get_score(self):
        return self.score
   
    

    

