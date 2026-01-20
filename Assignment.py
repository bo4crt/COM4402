question_bank = ["What colour is the sky?",
                 "What colour is grass?",
                 "What colour is the sun?",
                 "What colour is blood?",
                 "What colour is an orange?"]

correct_answer = ["Blue", "Green", "Yellow", "Red", "Orange"]

options = [["Blue", "Green", "Red", "Yellow", "Orange"],
           ["Blue", "Green", "Red", "Yellow", "Orange"],
           ["Blue", "Green", "Red", "Yellow", "Purple"],
           ["Red", "Blue", "Green", "Purple", "White"],
           ["Orange", "Red", "Green", "White", "Gold"]]

def check_answer(correct_answer, user_input):
    if user_input == correct_answer:
        return True
    else: return False

def run_quiz():
    question_counter = 0
    score = 0
    total_questions = len(question_bank)


    while question_counter < total_questions:
        print(question_bank[question_counter])

        for i in range(len(options[question_counter])):
            print(i + 1, options[question_counter][i])


        user_input = int(input("\nEnter your choice from the options:\n"))
        user_answer = correct_answer[question_counter]


        if check_answer(user_answer, correct_answer):
            print("Correct!")
            score += 1
        else: print("Incorrect!")

        question_counter += 1

    print("End of quiz.")
    print(f"Your score is {score}/{total_questions}")
    print("You have scored", score/total_questions * 100,"% on this quiz.")

run_quiz()