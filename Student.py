
class Students:

    def __init__(self, lname, fname, major, gpa=0.0):
        names = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not(names.issuperset(lname) and names.issuperset(fname): #If the Last Name does not have any of the values above, we raise an Error
            raise ValueError
        if not(names.issuperset(major)): #If the Major does not have any of the values in the set, we do the same thing
            raise ValueError
        if not isinstance(gpa, float):  #If the GPA is not a float, we raise error
            raise ValueError
        elif gpa not in range(0,4):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

stud = Students('Lehmann','Ben','Math', 3.0)
print(stud.__str__())
