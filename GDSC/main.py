from question import Question
from quiz import Quiz
from question_data_2 import question_data_2  # Import the additional question data

# Create Question instances for the additional question data
additional_questions = [Question(item["text"], item["answer"]) for item in question_data_2]

# Create Quiz instance for the additional questions
additional_quiz = Quiz(additional_questions)

while additional_quiz.do_questions_remain():
    current_question = additional_quiz.next_question()
    print(f"Question: {current_question.text}")
    user_answer = input("Your answer (True/False): ")
    additional_quiz.check_answer(user_answer)

# Displays the final score for the additional quiz
print(f"Your score for the additional quiz: {additional_quiz.get_score()}")
