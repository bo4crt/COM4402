# nums = [3,6,9,12]
#
# print(nums[0])
# print(nums[3])
#
#
# colours = ["Red", "Blue", "Green",]
#
# colours.append("Black")
#
# for i in range(2):
#     print(colours)
#
# Fruits = ["apple", "banana", "cherry",]
#
# Fruits[1] = "orange"
#
# print(Fruits)
#
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30, 40, 50]
# list3 = []
#
# for item in list1:
#     list3.append(item)
#
# print(list3)
#
# for item in list2:
#     list3.append(item)
#
# print(list3)
#
# list1.remove(2)
# list1.remove(3)
# list1.remove(4)
# print(list1)
#
# list1.insert(1, 99)
# list1.insert(2, 100)
# print(list1)
#
# list3.pop()
# list3.pop()
# print(list3)
#
# for i in range(len(list3)):
#     list3[i] = list3[i] * 2
# print(list3)



#
# person = {"name": "Sam", "city": "London"}
#
# person["city"] = "Bolton"
#
# person["age"] = int(input("Enter your age: "))
#
# print(person)


courses = {
    "python": {
        "students": ["Ali", "Sara", "Tom", "Ali"],
        "max_size": 3
    },
    "datasci": {
        "students": ["Sara", "Imran"],
        "max_size": 2
    },
    "math": {
        "students": ["Sara", "Tom"],
        "max_size": 2
    }
}

# 1. For each course, print the set of unique student names (so each name appears once).
# 2. For each course, check if the number of unique students is greater than `max_size`
# and print `"FULL"` or `"OK"`.
# 3. Build a dictionary `student_counts` mapping each student name to
# how many different courses they are enrolled in (use a dict plus sets or lists).

# find all unique students
course_keys = courses.keys()
all_students_unique_set = set()

# make a set of students from all courses
for key in course_keys:
    students_list_set = set(courses[key]["students"])
    all_students_unique_set = all_students_unique_set.union(students_list_set)
    # print(all_students_unique_set)

# initialize a dict with 0 count for each student
student_counts = {}
for student in all_students_unique_set:
    student_counts[student] = 0
# print(student_counts)

# for each course
for key in course_keys:
    # make a set of students
    unique_students_in_course = set(courses[key]["students"])
    # for each unique student
    for student in unique_students_in_course:
        # increment count in set
        student_counts[student] = student_counts[student] + 1

print(student_counts)





#
# course_keys = courses.keys()
# # print(course_keys)
#
# # for each course print unique students
# for key in course_keys:
#     print(f"Unique students in {key}: ")
#     print(set(courses[key]["students"]))
# #
# # print(set(courses["python"]["students"]))
# # print(set(courses["datasci"]["students"]))
# #
# #
# #
#
#
#
# for key in courses.keys():
#     unique_students = set(courses[key]["students"])
#     print(f"Unique students in {key}: {unique_students}")
#
# print("\n \nStudent count and capacity")
#
# for key in courses.keys():
#     current_count = len(set(courses[key]["students"]))
#     max_size = courses[key]["max_size"]
#
#     if current_count >= max_size:
#         print(key,": Full (", current_count,"/", max_size,")" )
#     else:
#         print(f"{key}: OK ({current_count}/{max_size})")
#
# print(set(len(courses["python"]["students"])))
# print(set(len(courses["datasci"]["students"]))), "is enrolled in",course_keys.count )




# total_students = sum(len(course["python"]["students"]))
# for course in courses["python"]["students"])
#     print("Total students:", total_students)
#
# for courses in courses["python"]["max_size"]



# print(courses)
# print(courses["python"])
# print(courses["python"]["students"])
# print(courses["python"]["students"][0])
