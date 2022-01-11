from question_model import Question


class QuizBrain:
    """The main quiz model"""

    def __init__(self, question_list):
        """Initialize the QuizBrain taking the list of questions as input"""
        self.question_bank = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_bank[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) ")
        if user_answer.lower() == current_question.answer.lower():
            self.score += 1
            print(f"Correct! Score: {self.score} / {self.question_number}")
        else:
            print(f"Incorrect. Score: {self.score} / {self.question_number}")
        print("\n")

    def still_has_questions(self):
        return self.question_number < len(self.question_bank)