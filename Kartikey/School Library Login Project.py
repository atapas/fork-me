A = [7376,'Ansh Walia - XI C','Last Book Issued: A Fine Balance','Current Book Issued: The God Of Small Things','Issued on 1/09/2020','To be submitted on 01/10/2020']
K = [9619,'Kartikey Prajapati - XI C','Last Book Issued: The Palace Of Illusions','Current Book Issued: The White Tiger','Issued on 01/09/2020','To be submitted on 1/10/2020']
P = [5467,'Piyush Singh - XI C','Last Book Issued: The Shadow Lines','Current Book Issued: A Suitable Boy','Issued on 01/09/2020','To be submitted on 1/10/2020']
S = [8376,'Shivansh - XI C','Last Book Issued: Train To Pakistan','Current Book Issued: The Guide','Issued on 01/09/2020','To be submitted on 1/10/2020']

Students = ['Ansh',A,'Kartikey',K,'Piyush',P,'Shivansh',S]

ABooks = ['The Great Indian Novel','The Inheritance of Loss','Sea of Poppies','The Secret of Nagas','The Glass Palace']

Lipi = ['Last Book Issued: ','Current Book Issued: ']
Gurpreet = ['Last Book Issued: ','Current Book Issued: ']
Pooja = ['Last Book Issued: ','Current Book Issued: ']
Shikha = ['Last Book Issued: ','Current Book Issued: ']

Teachers = ['Lipi',Lipi,'Gurpreet',Gurpreet,'Pooja',Pooja,'Shikha',Shikha]

pw = ""

PW = ['PrincipalTIS','P@$$W0RD','LibTeacher','123456789']

print("Welcome to Tagore International School, East Of Kailash Online Library.")
def start():
    print("")
    n = int(input("1.Login\n2.Search and Display\nYOUR INPUT: "))
    print("")
    if n==1:
        n1 = int(input("LOGIN AS:\n1.Principal\n2.Library Teacher\nYOUR INPUT: "))
        if n1==1:
            principal_login()
        elif n1==2:
            lib_teacher_login()
        else:
            print("Wrong Input")
            start()
    elif n==2:
          st_search()
    else:
        print("Wrong Input")
        start()

def principal_login():
    print("")
    print("PRINCIPAL LOGIN")
    un = input("Enter Username: ")
    pw = input("Enter Password: ")
    if un == PW[0] and pw == PW[1]:
        principal()
    else:
        print("Invalid Username or Password")
        principal_login()

def principal():
    print("")
    n = int(input("1.View Teacher's Info\n2.Add a Teacher\n3.Delete a Teacher\n4.Update Teacher\n5.Change Username or Password\n6.Log Out\nYOUR INPUT: "))
    if n==1:
        teacher_info()
    elif n==2:
        teacher_insert()
    elif n==3:
        teacher_delete()
    elif n==4:
        teacher_update()
    elif n==5:
        principal_change_pw()
    elif n==6:
        breaks()
    else:
        print("Wrong Input")
        principal()

def principal_change_pw():
    print("")
    n = int(input("1.Change Username\n2.Change Password\n3.Log Out\nYOUR INPUT: "))
    if n==1:
        un = str(input("Enter New Username: "))
        PW[0] = un
        pri_cont()
    elif n==2:
        opw = input("Enter Old Password: ")
        npw = input("Enter New Password: ")
        if opw == PW[1]:
            PW[1] = npw
            pri_cont()
        else:
            print("Incorrect Old Password")
            principal_change_pw()
    elif n==3:
        breaks()
    else:
        print("Wrong Input")
        principal_change_pw()

def lib_teacher_login():
    print("")
    print("TEACHER LOGIN")
    un = input("Enter Username: ")
    pw = input("Enter Password: ")
    if un == PW[2] and pw == PW[3]:
        lib_teacher()
    else:
        print("Invalid Username or Password")
        lib_teacher_login()

def lib_teacher():
    print("")
    n = int(input("1.See Available Books\n2.Teachers\n3.Students\n4.Change Username or Password\n5.Log Out\nYOUR INPUT: "))
    if n==1:
        books()
    elif n==2:
        teacher()
    elif n==3:
        student()
    elif n==4:
        teacher_change_pw()
    elif n==5:
        breaks()
    else:
        print("Wrong Input")
        lib_teacher()

def teacher():
    print("")
    n = int(input("1.View Teachers Info\n2.Add a New Teacher\n3.Remove a teacher\n4.Update a teacher\n5.Log Out\nYOUR INPUT: "))
    if n==1:
        teacher_info()
    elif n==2:
        teacher_insert()
    elif n==3:
        teacher_remove()
    elif n==4:
        teacher_update()
    elif n==5:
        breaks()
    else:
        print('Wrong Input')
        teacher()

def teacher_change_pw():
    print("")
    n = int(input("1.Change Username\n2.Change Password\n3.Log Out\nYOUR INPUT: "))
    if n==1:
        un = str(input("Enter New Username: "))
        PW[2] = un
        te_cont()
    elif n==2:
        opw = input("Enter Old Password: ")
        npw = input("Enter New Password: ")
        if opw == PW[3]:
            PW[3] = npw
            te_cont()
        else:
            print("Incorrect Old Password")
            teacher_change_pw()
    elif n==3:
        breaks()
    else:
        print("Wrong Input")
        teacher_change_pw()

def teacher_info():
    for i in range(0,len(Teachers),2):
            print(Teachers[i])
            k = Teachers[i+1]
            for j in range(0,len(k)):
                print("    ",k[j])

def teacher_insert():
    print("")
    n = str(input("Enter Name of Teacher: "))
    if n not in Teachers:
        Teachers.append(n)
        n1 = []
        Teachers.append(n1)
        lastbook = str(input("Enter Last Book Issued: "))
        n1.append('Last Book Issued: '+lastbook)
        currentbook = str(input("Enter Current Book Issued: "))
        n1.append('Current Book Issued: '+currentbook)
    te_cont()

def teacher_delete():
    print("")
    n = str(input("Enter Name of Teacher: "))
    for i in range(0,len(Teachers)):
        if n==Teachers[i]:
            Teachers.pop(i+1)
            Teachers.pop(i)
    te_cont()

def teacher_update():
    print("")
    n = str(input("Enter Name of Teacher: "))
    for i in range(0,len(Teachers),2):
        if n==Teachers[i]:
            k = Teachers[i+1]
            n1 = int(input("1.Change Last Book Issued\n2.Current Book Issued\nYOUR INPUT: "))
            if n1==1:
                s = input("Enter Last Book Issued: ")
                k[1]=['Last Book Issued :',s]
            elif n1==2:
                s = input("Enter Current Book Issued: ")
                k[2]=['Current Book Issued :',s]
                print(k)
    te_cont()

def books():
    print("")
    print("Available Books:")
    for i in range(0,len(ABooks)):
        print("    ",ABooks[i])
    print("")
    te_cont()

def student():
    print("")
    n = int(input("1.View Students Info\n2.Add a New Student\n3.Remove a Student\n4.Update a Student\n5.Log Out\nYOUR INPUT: "))
    if n==1:
        student_info()
    elif n==2:
        student_insert()
    elif n==3:
        student_delete()
    elif n==4:
        student_update()
    elif n==5:
        breaks()
    else:
        print('Wrong Input')
        student()

def student_info():
    a = []
        for i in range(1,len(Students)+1,2):
            a = Students[i]
            print(a[1])
            for k in range(2,len(a)):
                print("    ",a[k])
                k += 1
        te_cont()


def student_insert():
    print("")
    n = str(input("Enter Name of Student: "))
    if n not in Students:
        Students.append(n)
        n1 = []
        Students.append(n1)
        lastbook = str(input("Enter Last Book Issued: "))
        n1.append('Last Book Issued: '+lastbook)
        currentbook = str(input("Enter Current Book Issued: "))
        n1.append('Current Book Issued: '+currentbook)
        issue = str(input("Enter The Date Of Issuing: "))
        n1.append('Issued on '+issue)
        due = str(input("Enter The Date Of Submission(DD/MM/YYYY): "))
        n1.append('To be Submitted on '+due)
    te_cont()

def student_delete():
    print("")
    n = str(input("Enter Name of Student: "))
    for i in range(0,len(n)):
        if n==Students[i]:
            Students.pop(i+1)
            Students.pop(i)
    lib_teacher()

def student_update():
    print("")
    n = str(input("Enter Name of Student: "))
    for i in range(0,len(Students),2):
        if n==Students[i]:
            n1 = int(input("1.Change Last Book Issued\n2.Current Book Issued\n3.Issued Date\n4.Submission Date\n5.Log Out\nYOUR INPUT: "))
            if n1==1:
                s = input("Enter Last Book Issued: ")
                Students[i+1][2]=['Last Book Issued :',s]
            elif n1==2:
                s = input("Enter Current Book Issued: ")
                Students[i+1][3]=['Current Book Issued :',s]
            elif n1==3:
                s = input("Enter Date Of Issuing(DD/MM/YY): ")
                Students[i+1][4]=['Issued on',s]
            elif n1==4:
                s = input("Enter Date Of Submission(DD/MM/YY): ")
                Students[i+1][4]=['To be Submitted on',s]
            elif n1==5:
                breaks()
            else:
                student_update()
    lib_teacher()

def st_search():
    print("")
    c = 0
    a = []
    name = str(input("Enter Student's first name: "))
    an = int(input("Enter your admission no: "))
    for i in range(0,len(Students),2):
        if name == Students[i]:
            a = Students[i+1]
            if an == a[0]:
                c += 1
                print("")
                print(a[1])
                for i in range(2,len(a)):
                    print("    ",a[i])
                start()
    if c == 0:
            print("Wrong Input")
            st_search()

def pri_cont():
    print("")
    n = int(input("Do You Want To Continue:\n1.Yes\n2.No\n"))
    if n==1:
        principal()
    elif n==2:
        breaks()

def te_cont():
    print("")
    n = int(input("Do You Want To Continue:\n1.Yes\n2.No\n"))
    if n==1:
        lib_teacher()
    elif n==2:
        breaks()

def st_cont():
    n = int(input("Do You Want To Continue:\n1.Yes\n2.No\n"))
    if n==1:
        start()
    elif n==2:
        breaks()

def breaks():
    print("")
    print("Thanks for visiting TOI Library.\nHave A Good Day")

start()
