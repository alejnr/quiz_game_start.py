from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    q_text = q["question"]
    q_answer = q["correct_answer"]
    new_q = Questions(q_text, q_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
else:
    print("Thanks for playing! You've completed the quiz!")
    print(f"Your final score is {quiz.score}/{len(question_bank)}.")