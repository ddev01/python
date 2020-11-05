class Student:
    def __init__(self, fn, ln, dob, n):
        self.firstname = fn
        self.lastname = ln
        self.dateofbirth = dob
        self.adminnumber = n
    def __repr__(self):
        return "{} {} {} {}".format(self.firstname, self.lastname, self.dateofbirth, self.adminnumber)
class Cursus:
    def __init__(self, c1, c2, c3, c4, c5):
        self.cursus1 = c1
        self.cursus2 = c2
        self.cursus3 = c3
        self.cursus4 = c4
        self.cursus5 = c5



s = Student("Eric", "Bankschroef", "21/01/2001", 2424)
c = Cursus("Economie", "Nederlands", "Rekenen")
print(c.cursus1)
print(s)