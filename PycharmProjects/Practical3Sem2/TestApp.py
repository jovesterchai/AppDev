import Student as s
import Lecturer as l

lname = input('Enter Lecturer Name: ')
lnric = input('Enter Lecturer NRIC: ')

# staffid = input('Enter Staff Id: ')
while True:
    staffid = input('Enter Staff Id: ')
    if staffid == lnric:
        break

hour = float(input('Enter Total Teaching Hours: '))

lecturer = l.Lecturer(lname, lnric, staffid)
lecturer.set_total_TeachingHour(hour)

sname = input('Enter Student Name: ')
snric = input('Enter Student NRIC: ')
adminno = input('Enter Student Admin Number: ')

testmark = -1
while testmark < 0 or testmark > 100:
    testmark = float(input('Enter Test mark: '))

exammark = -1
while exammark < 0 or exammark > 100:
    exammark = float(input('Enter Exam mark: '))

# testmark = float(input('Enter Test mark: '))
# exammark = float(input('Enter Exam mark: '))

student = s.Student(sname, snric, adminno)
student.set_test_Mark(testmark)
student.set_exam_Mark(exammark)

# print(lecturer.get_name() + ', ' + 'Staff Id:', lecturer.get_staff_id(), 'earns $%.2f' % (lecturer.computeSalary()))
# print(student.get_name() + ', ' + 'Admin No:', student.get_admin_no(), 'final mark is ' + str(student.computeFinalMark()))

print(lecturer)
print(student)
