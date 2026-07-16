import html
#Manages the quiz flow, score, and questions
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    #Check if there are more questions
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    #Get the next question
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return q_text

    #Check the answers, increase score and return a message
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower() and self.still_has_questions():
            self.score += 1
            return "You got it right!"
        else:
            return "That's wrong!"
