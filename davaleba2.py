class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def display_info(self):
        print(f"სტუდენტის ID: {self.student_id}\nსახელი: {self.name}\nკურსების ჩამონათვალი:")
        if not self.courses:
            print(f"- თქვენ არ ხართ დარეგისტრირებული არცერთ კურსზე.")
        else:
            for course in self.courses:
                print(f"  - {course}")
               

    def start_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} დარეგისტრირდა შემდეგ კურსზე: {course}")
        else:
            print(f"{self.name} უკვე არის დარეგისტრირებული აღნიშნულ კურსზე: {course}")

    def leave_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"{self.name} დატოვა შემდეგი კურსი : {course}")
        else:
            print(f"{self.name} არ არის დარეგისტრირებული აღნიშნულ კურსზე: {course}")


student1 = Student("Mikheil Makasarashvili", "7777")
student2 = Student("Shota Rustaveli", "67890")

student1.display_info()
student1.start_course("Python")
student1.start_course("JavaScript")
student1.start_course("JavaScript")
student1.display_info()

student2.start_course("Philology")
student2.display_info()
student2.leave_course("Philology")
student2.leave_course("Python")
student2.display_info()
