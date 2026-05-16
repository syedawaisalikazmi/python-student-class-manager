class Myclass:
    print("This is my class")
    def __init__(self,myname,rollno,marks):
        self.rollno=rollno
        self.name = myname
        self.marks=marks
s1=Myclass("Awais",1,90)
print(s1.name)
print(s1.rollno)
print(s1.marks)
s2=Myclass("Ali",2,80)
print(s2.name)
print(s2.rollno)
print(s2.marks)
