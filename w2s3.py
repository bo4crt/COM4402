#Excercise 3

#score = int(input("Please enter your score:"))

# if score >= 70:
#     print("Distinction")
# elif 42 < score < 69:
#     print("Clear pass")
# elif 38 >= score <= 42:
#     print("Borderline pass, consider review.")
# else:
#     print("fail")
#
#
#
# #Excercise 1
#
# age = int(input("What is your age?"))
# # if age >= 65:
# #     print("Senior ticket")
# # elif age > 17:
# #     print("Adult ticket")
# # elif age >= 5:
# #     print("Child ticket")
# # else:
# #     print("Free entry")
#
# if 0 < age <= 5:
#     print("Free entry")
# elif 5 < age <= 17:
#     print("Child ticket")
# elif 17 < age <= 65:
#     print("Adult ticket")
# else:
#     print("Senior ticket")
#
#
#
#
#
# #Excercise 2
# #
# days_late = int(input("How many days late?"))
# if days_late > 10:
#     print("Fine = £10 and membership review")
# elif 5 < days_late <= 10:
#     print("Fine = £5")
# elif 10 < days_late <= 5:
#     print("Fine = £1")
# elif days_late == 0:
#     print("No fine")


#Excercise 4

# is_student = str(input("Are you a student?"))
#
# if is_student == 'yes':
#     print("Discount applied")
#
# else:
#     print("How old are you?")
#
# age = int(input())
# if age < 18:
#     print("Discount applied")
# else: print("No discount.")


#Excercise 5

# print("What colour?")
#
# colour = str(input())
# if colour == 'red':
#     print("Stop")
# elif colour == 'amber':
#     print("Get ready")
# elif colour == 'green':
#         print("Go")
# else: print("Invalid colour")
#
# match colour:
#     case "red":
#         print("Stop")
#     case "amber":
#         print("Slow down")
#     case "Green":
#         print("Go")
#
#     case _:
#         print("Stop")

#Excercise 6

# number = float(input("Enter number"))
#
# if number == 3:
    # do A



#W2S4


# choice = int(input("Enter your choice:"))
# # if choice == 1:
# #     print("Hello")
# # if choice == 1:
# #     print("Goodbye")
# # if choice == 3:
# #     print("My name is python")
# # else: print("Invalid")
#
# match choice:
#     case 1:
#         print("Hello")
#     case 2:
#         print("Goodbye")
#     case 3:
#         print("My name is Python")
#     case _:
#         print("Invalid")







num = int(input("Enter number"))


if num%3==0 and num%5 == 0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print("No match\n Try again")

# div3 = False
# div5 = False
#
# result = "Invalid number"
#
# if num % 3 == 0:
#     div3 = True
#     result = "Fizz"
# if num % 5 == 0:
#     div5 = True
#     result = "Buzz"
#
# if div3 & div5:
#     result = "FizzBuzz"
#
# print(result)





























