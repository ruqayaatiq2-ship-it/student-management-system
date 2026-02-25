class StudentManager:

    def __init__(self):
        self.file = "students.txt"

    def add_student(self):

        name = input("Enter student name: ")
        age = input("Enter age: ")

        with open(self.file, "a") as f:
            f.write(name + "," + age + "\n")

        print("Student added successfully")


    def view_students(self):

        try:

            with open(self.file, "r") as f:

                print("\nStudent Records:\n")

                for line in f:
                    name, age = line.strip().split(",")

                    print("Name:", name)
                    print("Age:", age)
                    print("--------")

        except:

            print("No records found")


manager = StudentManager()

while True:

    print("\n1 Add Student")
    print("2 View Students")
    print("3 Exit")

    choice = input("Choice: ")

    if choice == "1":

        manager.add_student()

    elif choice == "2":

        manager.view_students()

    elif choice == "3":

        break
