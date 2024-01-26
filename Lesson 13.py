class Person:
    __name: str = "no name"
    __surname: str = "no name"
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    def show_info(self):
        pass
        # print(f"Name: {self.name}\nSurname: {self.surname}")

class Student(Person):
    __age: int = 0

    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.__age = age

    def show_student(self):
        super().show_info()
        print(f"Student is {self.name} {self.surname}. Age is {self.__age}")


class Teacher(Person):
    __age: int = 0
    __specialization: str = "none"
    def __init__(self, name, surname, age, specialization):
        super().__init__(name, surname)
        self.__age = age
        self.__specialization = specialization

    def show_teacher(self):
        super().show_info()
        print(f"Teacher is {self.name} {self.surname}. Age is {self.__age}. Specialization is {self.__specialization}.")



class Academy:
    __AcademyName: str = "none"
    __subjects: str = "none"
    __grade: int = 0
    def __init__(self, AcademyName, subjects, grade):
        self.__AcademyName = AcademyName
        self.__subjects = subjects
        self.__grade = grade

    @property
    def AcademyName(self):
        return self.__AcademyName

    @property
    def subjects(self):
        return self.__subjects


    def show_academy(self):
        print(f"Academy is {self.AcademyName},subjects taught: {self.subjects}, there are {self.__grade} grades")

test_academy = Academy ("hihg tech",'maths', 5)
test_academy.show_academy()
test_student= Student ("Lesi","Loo", 45)
test_student.show_student()
test_teacher = Teacher ("Vasyl","Loiko", 22, "mathematics")
test_teacher.show_teacher()