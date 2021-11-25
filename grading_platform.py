global student_marks
student_marks = {
    "Mariya Turetska" : {
        "Math": 99,
        "Photogrpahy": 100,
        "French": 95,
        "CS": 97
    }
}


def add_new(student_name):

    for i in range (1,4):
        text1 = "Code of the course " + str(i) + ": "
        text2 = "Grade for coure " + str(i) + ": "
        subject = input(text1)
        mark = int(input(text2))

        new_info = { subject : mark }
        new_dic = {student_name : new_dic.update(new_info)}
        # new_dic.update(new_info)
        student_marks.update(new_dic)

    print("The student and their grades have been successfully added to the database!")
    print(student_marks)

# Searching student grades
def action_1():
    user_request = input("Search up a person: ")
    if user_request in student_marks:
        print("Here is all the grades we have from", user_request)
        print(student_marks[user_request])
    else:
        user_answer = input("We don't have such student. Would you like to add them? (Y/N) ")
        if user_answer == "Y":
            add_new(user_request)
        elif user_answer == "N":
            menu()

def action_2():
    a = 2


# Calculating student average
def action_3():
    user_request = input("Search up a person: ")
    if user_request in student_marks:
        course_average(user_request)
    else:
        print("We couldn't find this student in our database. Try adding this student to the database first, or search up a different student.")

# Conducting the actual calculations of the average mark
def course_average(student_name):
    grades = student_marks[student_name]
    grades_val = list(grades.values())
    max_mark = max(grades_val)
    min_mark = min(grades_val)
    average_mark = sum(grades_val) / len(grades_val)
    print(student_name, "has an average grade in her courses of", average_mark, ".\nHeighest Mark: ", max_mark, "\nLowest Mark: ", min_mark)

# Getting values of nested dictionaries
def get_values(dictionary):
    if isinstance(dictionary, dict):
        for value in dictionary.values():
            yield from get_values(value)
    elif isinstance(dictionary, list):
        for value in dictionary:
            yield from get_values(value)
    else:
        yield dictionary

def action_4():
    a = 4
def action_5(): 
    a = 5

# Menu
while True:
    def menu():
        print("\nWelcome to the student performance portal. Use the menu to navigate:")
        print("Press 1 to search up a student and their performance in their courses.")
        print("Press 2 to add a new student and their grades to the system.")
        print("Press 3 to search up a student's current average, lowest and highest grades.")
        print("Press 4 to save this file as a text file.")
        print("Press 5 to exit the program.")

        try:
            user_input = input("\nYour Selection: ")
            if user_input == '1':
                action_1()
            elif user_input == '2':
                action_2()
            elif user_input == '3':
                action_3()
            elif user_input == '4':
                action_4()
            elif user_input == '5':
                action_5()
        except:
            print("Please input a propoer number to navigate this menu.")

    menu()
