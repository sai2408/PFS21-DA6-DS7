colleges = []
class person:
    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name
class student(person):
    def __init__(self,rollno,name,branch):
        super().__init__(rollno,name)
        self.branch = branch
class teacher(person):
    def __init__(self,rollno,name,subject):
        super().__init__(rollno,name)
        self.subject = subject
class college:
    def __init__(self,clg_id,clg_name):
        self.clg_id = clg_id
        self.clg_name = clg_name
        self.students = []
        self.teachers = []
    def add_student(self,student):
        self.students.append(student)
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
    def display_students(self):
        pass
    def dipslay_teachers(self):
        pass
print("Welcome !")
print()
while True:
    print("1. Add college")
    print("2. Add Student")
    print("3. Add Teacher")
    print("4. Display Student Details")
    print("5. Display Teachers Details")
    print("6. Exit")
    x = int(input("Ente Your Choise: "))
    if x == 1:
        clgid = int(input("Enter College Id: "))
        k = True
        for obj in colleges:
            if obj.clg_id == clgid:
                k = False
                break
        if k == True:
            cname = input("Enter COllege Name: ")
            clg = college(clgid,cname)
            colleges.append(clg)
        else:
            print("College Already Exists !")
    elif x == 2:
        clgid = int(input("Enter College Id: "))
        k = True
        for obj in colleges:
            if obj.clg_id == clgid:
                k = False
                res = obj
                break
        if k == True:
            print("College Does not Exists !")
        else:
            sroll = int(input("Enter Student Roll no: "))
            sname = input("Enter Student Name: ")
            sbranch = input("Enter Branch: ")
            s = student(sroll,sname,sbranch)
            res.add_student(s)
            print("Student Added Sucessfully !")
    elif x == 3:
        clgid = int(input("Enter College Id: "))
        k = True
        for obj in colleges:
            if obj.clg_id == clgid:
                k = False
                res = obj
                break
        if k == True:
            print("Colleges Does not Exists !")
        else:
            troll = int(input("Enter Roll no: "))
            tname = input("Enter Name: ")
            tsubject = input("Enter Subject: ")
            t = teacher(troll,tname,tsubject)
            res.add_teacher(t)
            print("Teacher Added Sucessfully !")
    elif x == 4:
        clgid = int(input("Enter College Id: "))
        k = True
        for obj in colleges:
            if obj.clg_id == clgid:
                res = obj
                k = False
                break
        if k == True:
            print("college Does not Exits !")
        else:
            details = res.students
            for data in details:
                print()
                print(f"Roll No: {data.rollno}")
                print(f"Name: {data.name}")
                print(f"Branch: {data.branch}")     
    elif x == 5:
        clgid = int(input("Enter College Id: "))
        k = True
        for obj in colleges:
            if obj.clg_id == clgid:
                res = obj
                k = False
                break
        if k == True:
            print("college Does not Exits !")
        else:
            details = res.teachers
            for data in details:
                print()
                print(f"Roll no: {data.rollno}")
                print(f"Name: {data.name}")
                print(f"Subject : {data.subject}")
    else:
        print()
        print("Thank You, Visit Again !")
        break





    






        
