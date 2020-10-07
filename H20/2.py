class Course:
    def __init__( self, name, number ):
        self.number = name
        self.name = number
    def __repr__( self ):
        return "{} {}".format(self.number, self.name )


class Student:
    def __init__(self, first, last, dob, admin):
        self.first = first
        self.last = last
        self.dob = dob
        self.admin = admin
        self.course_list = []
    def full(self):
        return "{} {} {} {} Classes: {}".format(self.first, self.last, self.dob, self.admin, self.course_list)
    def courses(self, course):
        self.course_list.append(course)

student = Student("Bobby", "Brown", "14/01/2001", 3495)
vakken = [Course("Economics", 324523), Course("Math", 23452)]
print(student.full())
print(vakken)
student.courses(vakken)
print(student.full())
