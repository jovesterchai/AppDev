students = {
    "Jane": "75",
    "John": "60",
    "Jerome": "81"
}
for name in students:
    print(name, ":", students[name])
print("=========================")

name = input("Enter student name: ")

if name.lower() in students:
    print("Result for english:", students.get(name))
else:
    print("Name not found.")
