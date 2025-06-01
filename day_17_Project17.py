# Project-17 = Quiz Game Project
from questionmodel17 import Question
from data17 import question_data
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False)? ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.strip().lower() == correct_answer.lower():
            print("✅ Correct!")
            self.score += 1
        else:
            print("❌ Wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your score: {self.score}/{self.question_number}\n")

# Create list of Question objects
question_bank = [Question(q["text"], q["answer"]) for q in question_data]

# Initialize and run the quiz
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Final Score: {quiz.score}/{len(question_bank)}")
