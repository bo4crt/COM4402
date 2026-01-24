import random

quiz = [{"question": "What colour is the sky?",
         "options": ["Blue", "Green", "Red", "Yellow"],
         "answer": "Blue"},

        {"question": "What colour is the sun?",
         "options": ["Blue", "Green", "Red", "Yellow"],
         "answer": "Yellow"},

        {"question": "What colour is blood?",
         "options": ["Red", "Blue", "Green", "Purple"],
         "answer": "Red"},

        {"question": "What colour is an orange?",
         "options": ["Orange", "Red", "Green", "White"],
         "answer": "Orange"},

        {"question": "Is grass green",
         "options": ["True", "False"],
         "answer": "True"},

        {"question": "When a negative number is divided by 0, what is the result?",
         "options": ["Positive number", "Zero", "Negative number"],
         "answer": "Zero"}
        ]


def check_answer(question, user_input):
    return question["answer"] == user_input


def get_answer_from_user(question):
    print("\n" + question["question"])

    random.shuffle(question["options"])
    total_options = len(question["options"])
    for i in range(total_options):
        print(i + 1, question["options"][i])


    while True:
        try:
            user_choice_index = int(input(f"\nEnter your choice (1-{total_options}): ")) - 1
            if 0 <= user_choice_index < len(question["options"]):
                break
            else:
                print(f"Please enter a number between 1 and {total_options}.")
        except ValueError:
            print("Please enter a valid number.")

    return question["options"][user_choice_index]


def run_quiz():

    print("Holton College Quiz")
    print("Please answer questions by entering the number of your choice:")

    score = 0
    total_questions = len(quiz)

    random.shuffle(quiz)

    for question in quiz:
        chosen_answer = get_answer_from_user(question)

        if check_answer(question, chosen_answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The answer was", question["answer"])

    print("\nEnd of quiz.")
    print(f"Your score is {score}/{total_questions}.")
    print(f"You have scored {round(score / total_questions * 100, 2)}% on this quiz.")


run_quiz()