from question_model import Question
from data import question_data as questions
from quiz_brain import QuizBrain

# Array of all question in data.py as Question Object
question_bank = []

# Looping through the dicts in questions from data.py and inserting each question as a Question Object
# in question_bank list
for question in questions['results']:
    quest = Question(question['question'], question['correct_answer'])
    question_bank.append(quest)

# Initializing a new quiz Object and passing it our question bank as Questions Object
quiz = QuizBrain(question_bank)

# Starting the quiz: If there're still question, display the next question to the user
while quiz.still_has_questions():

    # Display the next question to the user
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is ({quiz.score}/{quiz.question_num})")
