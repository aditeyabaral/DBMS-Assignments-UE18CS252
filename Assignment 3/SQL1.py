import pyodbc
connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-HOLIG319;'
                      'Database=DBMS;'
                      'Trusted_Connection=yes;')
cursor = connection.cursor()
name = input("ENTER STUDENT NAME TO PRINT GPA: ")
number =  list(cursor.execute("SELECT STUDENT_NUMBER FROM STUDENT WHERE NAME = \'"+name+"\'"))[0][0]
grades = cursor.execute("SELECT GRADE FROM GRADE_REPORT WHERE STUDENT_NUMBER = "+str(number))
gpa = 0.0
for i in grades:
    grade = i[0]
    if grade=='A':
        gpa+=4
    elif grade=='B':
        gpa+=3
    elif grade=='C':
        gpa+=2
    else:
        gpa+=1
print("GPA:", gpa/4)
