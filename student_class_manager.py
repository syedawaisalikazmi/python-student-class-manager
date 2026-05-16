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
s1=Myclass("Awais",1,90)
s1.display()
s2=Myclass("Ali",2,80)
s2.display()
