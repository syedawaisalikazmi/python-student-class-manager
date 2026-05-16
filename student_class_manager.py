class Myclass:
    print("This is my class")
    def __init__(self,myname,rollno,marks):
        self.rollno=rollno
        self.name = myname
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.rollno)
        print("Marks:",self.marks)
    def grade(self):
        if self.marks>=90:
            print("Grade: A")
        elif self.marks>=80:
            print("Grade: B")
        elif self.marks>=70:
            print("Grade: C")
        else:
            print("Grade: F")
s1=Myclass("Awais",1,90)
s1.display()
s1.grade()
s2=Myclass("Ali",2,80)
s2.display()
s2.grade()
