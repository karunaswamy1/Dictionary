{
    'sonu':85,
    'Kartik':90,
    'Deepak':96,
    'Aman':76,
    'Somesh':60,
    'Umesh':85,
    'Amarpal':70,
    'Roshan':57,
    'Riyaz':98,
    'Shabid':56
} 
num=(input("enter the student name"))
student={}
for i in range (num):
    key=input("enter the student name")
    values=int(input("enter the student marks"))
    student[key]=values
print(student)