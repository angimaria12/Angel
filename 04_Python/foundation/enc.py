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