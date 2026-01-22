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
    return correct_answer == user_input


def run_quiz():
    score = 0
    total_questions = len(quiz)

    random.shuffle(quiz)

    for question in quiz:
        print("\n" + question["question"])

        random.shuffle(question["options"])

        for i in range(len(question["options"])):
            print(i + 1, question["options"][i])


        while True:
            try:
                user_choice = int(input("\nEnter your choice (1-4): ")) - 1
                if 0 <= user_choice < len(question["options"]):
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")

        user_answer = question["options"][user_choice]

        if check_answer(question["answer"], user_answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The answer was", question["answer"])

    print("\nEnd of quiz.")
    print(f"Your score is {score}/{total_questions}.")
    print("You have scored", score / total_questions * 100, "% on this quiz.")


run_quiz()


