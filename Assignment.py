import random
import array

quiz = [{"question": "What colour is the sky?",
        "options": ["Blue", "Green", "Red", "Yellow"],
        "answer": "Blue"},

    {"question": "What colour is grass?",
    "options": ["Blue", "Green", "Red", "Yellow"],
    "answer": "Green"},

    {"question": "What colour is the sun?",
            "options": ["Blue", "Green", "Red", "Yellow"],
            "answer": "Yellow"},

    {"question": "What colour is blood?",
            "options": ["Red", "Blue", "Green", "Purple"],
            "answer": "Red"},

    {"question": "What colour is an orange?",
            "options": ["Orange", "Red", "Green", "White"],
            "answer": "Orange"}]



def check_answer(correct_answer, user_input):
    if user_input == correct_answer:
        return True
    else:
        return False

import random

def run_quiz():
    question_counter = 0
    score = 0
    total_questions = len(quiz)

    while question_counter < total_questions:

        random.shuffle(quiz)

        for question in quiz:
            print("\n" + question["question"])

            for i in range(len("options"[question_counter])):
                print(i + 1, "options"[question_counter][i])

            user_choice = int(input("\nEnter your choice: ")) - 1
            user_answer = question["options"][user_choice]

            if check_answer(question["answer"], user_answer):
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")

        print("\nEnd of quiz.")
    print(f"Your score is {score}/{total_questions}")
    print("You have scored", score / total_questions * 100, "% on this quiz.")


# run_quiz()


q = {"question": "What colour is blood?",
            "options": ["Red", "Blue", "Green", "Purple"],
            "answer": "Red"}
print(q)
# shuffle options
random.shuffle(q["options"])
print(q["options"])
# find index position of answer after shuffle
# use this position to match user input to stored answer
answer = q["answer"]
print(q["options"].index(answer))