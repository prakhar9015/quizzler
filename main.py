from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html  # html.unescape   -> to remove special characters from the API response.
from ui import QuizInterface

question_bank = []  # -> an empty list , that will play a huge rule in passing the data to QuizBrain

for i in question_data:
    q_object = Question(html.unescape(i["question"]), i["correct_answer"])
    question_bank.append(q_object)

quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():  # loop through until there is questions left
#     quiz.next_question()
