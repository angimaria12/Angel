# class Student:
#     universiy="Nova University"
#     def __init__(self,name,id,dept,Marks,Attendance):
#         self.name=name
#         self.id=id
#         self.dept=dept
#         self.Marks=Marks
#         self.Attendance=Attendance
#     def display(self):
#         return f"Name:{self.name} \n ID:{self.id} \n Department:{self.dept} \n Marks:{self.Marks} \n Attendance:{self.Attendance}"
    
# '''
# Name
# id
# dept 
# Marks
# Attendance'''

# std1=Student("James","CS101","CSE",[89,90,78],0)
# std2=Student("Michale","CS102","CSE",[82,90,98],0)
# std3=Student("Shawn","CS103","CSE",[74,80,68],0)
# std4=Student("Allwyn","CS104","CSE",[92,70,92],0)
# std5=Student("Monika","CS105","CSE",[81,80,98],0)


# print(std1.display())
# print(std2.display())
# print(std3.display())
# print(std4.display())
# print(std5.display())


# Average
# class Student:
#     university="Nova University"
#     def __init__(self,name,id,dept,marks,attendance):
#         self.name=name
#         self.id=id
#         self.dept=dept
#         self.marks=marks
#         self.attendance=attendance
#     def average_marks(self):
#         return round(sum(self.marks) / len(self.marks),2)

# '''
# Name
# id
# dept
# Marks
# Attendance
# '''

# std1=Student("Angel","CS101","CSE",[89,90,78],0)
# std2=Student("Althea","CS102","CSE",[99,88,95],0)
# std3=Student("Asin","CS103","CSE",[90,80,70],0)
# st4=Student("Harini","CS104","CSE",[80,70,60],0)
# st5=Student("Joylin","CS105","CSE",[70,60,50],0)

# print(std1.average_marks())
# print(std2.average_marks())
# print(std3.average_marks())
# print(st4.average_marks())
# print(st5.average_marks())


# encapsulation
class Student:
    university="Nova University"
    def __init__(self,name,id,dept,marks,attendance):
        self.name=name
        self.id=id
        self.dept=dept
        self._marks=marks
        self._attendance=attendance

    # Getter
    def get_marks(self):
        sum_=0
        for mark in self._marks:
            sum_=sum_+mark
        self.average=sum_/len(self._marks)
        cgpa = self.average / 10
        return round(cgpa, 2)

    # Setter
    def set_marks(self,marks):
        self._marks=marks

'''
Name
id
dept
Marks
Attendance
'''

std1=Student("Angel","CS101","CSE",[89,90,78],0)
std2=Student("Althea","CS102","CSE",[99,88,95],0)
std3=Student("Asin","CS103","CSE",[90,80,70],0)
st4=Student("Harini","CS104","CSE",[80,70,60],0)
st5=Student("Joylin","CS105","CSE",[70,60,50],0)



print(std1.get_marks())
print(std2.name, std2.id, std2.dept,"CGPA:",std2.get_marks())
print(std3.get_marks())
print(st4.name, st4.id, st4.dept,"CGPA:",st4.get_marks())
print(st5.get_marks())
