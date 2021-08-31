num_of_students = int(input("Enter number of Students: "))

increment = 1

students_marks = []

while increment <= num_of_students:
    print(f"======= Student: {increment} =====")
    for i in range(1):
        nep = input("Enter nepali mark: ")
        eng = input("Enter eng mark: ")
        mat = input("Enter mat mark: ")
        sic = input("Enter sic mark: ")
        pop = input("Enter pop mark: ")
        mark = [nep, eng, mat, sic, pop]
        students_marks.append(mark)

    increment += 1


total_mark = []

for student in students_marks:
    total = 0
    for mark in student:
        total += int(mark)
    total_mark.append(total)

x = 1
for sm in total_mark:
    percentage = sm / 5
    division = ""

    if percentage > 35 and percentage < 45:
        division += "third"
    elif percentage > 45 and percentage < 60:
        division += "second"
    elif percentage > 60 and percentage < 75:
        division += "first"
    elif percentage > 75 and percentage < 100:
        division += "topper"
    else:
        division += "try again"

    print(f"========Student Result {x} ======")
    print(f"Total: {sm} Percentage: {percentage} Division: {division}")
    x += 1
