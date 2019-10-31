results = {
    "Jane": (75, 80, 85),
    "John": (60, 68, 74),
    "Jerome": (81, 63, 77),
    "Jason": (55, 76, 67),
    "Jessica": (62, 45, 68),
    "Joanne": (52, 47, 51)
}
name = input("Enter student name: ")
if name not in results:
    print("Student does not exist")
else:
    print("Results of", name)
    print("="*30)
    result = results.get(name)
    print("Results for English =", result[0])
    print("Results for Math =", result[1])
    print("Results for Science =", result[2])
    print("\n")
for name in results:
    ave = (sum(results[name])) / 3
    print("Average marks of %s = %.1f" %(name, ave))
En = 0
Math = 0
Sci = 0
for name in results:
    En += results[name][0]
    Math += results[name][1]
    Sci += results[name][2]
print("\n")
print("Average results for English = %.1f" %(En/len(results)))
print("Average results for Math = %.1f" %(Math/len(results)))
print("Average results for Science = %.1f" %(Sci/len(results)))

