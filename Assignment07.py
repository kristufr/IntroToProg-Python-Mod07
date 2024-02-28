# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   C.Cipolla, 2/28/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str = ""  # Hold the choice made by the user.


# TODO Create a Person Class
class Person:
    '''
    A class representing a person with 1st and last names

    Properties - first (str) and last name (str)

    Changelog:
    C.Cipolla 2/28/2024, Created Class
    '''

    # TODO Add first_name and last_name properties to the constructor (Done)
    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    # TODO Create a getter and setter for the first_name property (Done)
    @property  # getter or accessor returns first name
    def first_name(self) -> str:
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str) -> None:
        if value.isalpha() or value == "":
            self.__first_name = value.title()
        else:
            raise ValueError("The first name should only contain letters.")

    # TODO Create a getter and setter for the last_name property (Done)
    @property  # getter returns last name
    def last_name(self) -> str:
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str) -> None:
        if value.isalpha() or value == "":
            self.__last_name = value.title()
        else:
            raise ValueError("The last name should only contain letters.")

    # TODO Override the __str__() method to return Person data (Done)
    def __str__(self):
        return f"{self.first_name},{self.last_name}"


# TODO Create a Student class the inherits from the Person class (Done)
class Student(Person):
    '''
    Creates a Student Class that inherits Person class attributes

    Properties: first (str) and last names (str) from Person Class plus
                Course name (str)

    Changelog:
    C.Cipolla 2/28/2024, Created Class
    '''

    # TODO call to the Person constructor and pass it the first_name and last_name data (Done)
    def __init__(self, first_name: str ="", last_name: str ="", course_name: str =""):
        super().__init__(first_name=first_name, last_name=last_name)

        # TODO add an assignment to the course_name property using the course_name parameter (Done)
        self.course_name = course_name

    # TODO add the getter for course_name (Done)
    @property
    def course_name(self):
        return self.__course_name

    # TODO add the setter for course_name (Done)
    @course_name.setter
    def course_name(self, value: str):
        self.__course_name = value.upper()

    # TODO Override the __str__() method to return the Student data (Done)
    def __str__(self):
        return f"{Person(self)},{self.course_name}"


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        C. Cipolla, 2/28/2024, updated to use the Student Class

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """

        try:
            file = open(file_name, "r")
            this_dictionary = json.load(file)
            for each_row in this_dictionary:
                # Create a variable "student" of class Student and use the constructor to
                # convert from the dictionary
                student: Student = Student(first_name=each_row["FirstName"],
                                           last_name=each_row["LastName"],
                                           course_name=each_row["CourseName"])
                student_data.append(student)

            file.close()

        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)

        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        else:  # If try is successful
            if file.closed is False:
                file.close()

        finally:
            return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        C. Cipolla, 2/28/2024, updated to use the Student Class

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """

        try:
            # Convert the object into a list
            student_rolodex: list = []
            for each_row in student_data:
                student: dict = {"FirstName": each_row.first_name, "LastName": each_row.last_name,
                                 "CourseName": each_row.course_name}
                student_rolodex.append(student)

            file = open(file_name, "w")
            json.dump(student_rolodex, file)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)

        finally:
            if not file.closed:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        C. Cipolla, 2/28/2024, updated to use the Student Class

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student.first_name} '
                  f'{student.last_name} is enrolled in {student.course_name}')
        print("-" * 50)
        print()

    @staticmethod
    def input_student_data(student_data: list) -> list:
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        C. Cipolla, 2/28/2024, updated to use the Student Class

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:  # Error handling is done in the getter of the data classes
            # Create a student object of Student class and init its properties
            student = Student()
            student.first_name = input("Enter the student's first name: ")
            student.last_name = input("Enter the student's last name: ")
            student.course_name = input("Please enter the name of the course: ")
            # add the new student to the list of students
            student_data.append(student)

            print()
            print(f"You have registered {student.first_name} {student.last_name} for {student.course_name}.")
            print()

        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
