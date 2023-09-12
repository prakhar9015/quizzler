# Question model  -> This is basically structuring each of the items from data list, 
# making dictionary data to be used in a simple way by creating objects

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


new_q = Question("Where on Earth I am ?", "Iceland")

