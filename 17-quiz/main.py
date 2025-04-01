from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import html

questions = []

for question in question_data:
    text = html.unescape(question["question"])
    answer = question["correct_answer"]
    new_question = Question(text, answer)
    questions.append(new_question)

quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.next_question()
