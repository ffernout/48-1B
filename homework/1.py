class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Меня зовут {self.full_name}, Мой возраст {self.age}, Мое семейное положение: {self.is_married}")

class Teacher(Person):
    base_salary = 25000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        if self.experience > 3:
            bonus_years = self.experience - 3
            bonus = 0.05 * bonus_years * self.base_salary  # 5% за каждый год свыше 3-х
        else:
            bonus = 0
        total_salary = self.base_salary + bonus
        return total_salary

    def introduce_myself(self):
        super().introduce_myself()
        print(f"У меня опыта преподавателя: {self.experience}")
        print(f"Моя зарплата: {self.base_salary}")
        print(f"Моя зарплата с учетом опыта: {self.calculate_salary()}")

class Student(Person):
    def __init__(self, full_name, age, is_married, subject_grade):
        super().__init__(full_name, age, is_married)
        self.subject_grade = subject_grade

    def introduce_myself(self):
        super().introduce_myself()
        print(f"Моя оценка по предмету: {self.subject_grade}")

def create_students():
    students = []

    student1 = Student("Даня", 14, "не женат", "история 5")
    student2 = Student("Макс", 15, "не женат", "биология 3")
    student3 = Student("Глеб", 17, "не женат", "алгебра 4")

    students.extend([student1, student2, student3])

    return students

teacher = Teacher("Мис. Мария", 51, "за мужем", 7)
teacher.introduce_myself()

student_list = create_students()

for student in student_list:
    print("\n---")
    student.introduce_myself()