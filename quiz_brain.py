# All the functionality of this game is controlled by this module like, asking questions,
# adding scores by checking answers and showing final results

user_answer = ""


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.current_question = None

    def still_has_questions(self):
        """ Checks for remaining questions, as long as it returns True"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """ It adds +1 each time this function is called and hence retrieving that exact item from list"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f" \n Q.{self.question_number}: {self.current_question.text}"
        # self.check_answer(user_answer, current_question.answer)  # passing the arguments to the check_answer

    def check_answer(self, user_chosen_answer):
        """ checks the answer received from user, compares it and add scores"""
        correct_answer = self.current_question.answer

        if correct_answer.lower() == user_chosen_answer.lower():
            self.score += 1
            print(" \n You got it right ✅")
            return True
        else:
            print("\n That's wrong ❌")
            return False

