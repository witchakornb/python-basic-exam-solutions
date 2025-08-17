# Problem 4: วิชานี้เกรดออกยังนะ (โปรแกรมบันทึกและรายงานเกรด)
# แนวคิด:
# 1. ใช้ loop while เพื่อให้ถามข้อมูลซ้ำจนกว่าผู้ใช้จะพิมพ์ n (ไม่ทำต่อ)
# 2. เก็บรายชื่อนักศึกษาใน list names และเกรดใน list grades (ตำแหน่ง index ตรงกัน)
# 3. เมื่อจบการกรอกแล้ว:
#    - ค่าเฉลี่ย = ผลรวม / จำนวนคน (ตรวจกรณีไม่มีข้อมูล)
#    - หาค่า max ด้วยการไล่เทียบเองแบบพื้นฐาน (ไม่ใช้ฟังก์ชัน max เพื่อให้เข้าใจตรรกะ)
#    - หาค่า min เช่นเดียวกัน
# 4. แสดงรายงาน

print("===== Calculate Grade Program =====")

names = []
grades = []

count = 1
while True:
    name = input(f"Enter student name No.{count} : ")
    grade = float(input("Enter Grade : "))
    names.append(name)
    grades.append(grade)

    cont = input("Continue? (y/n) : ")
    if cont == 'n':
        break
    count += 1

print("\n===== Report =====")

if len(grades) == 0:
    print("No data.")
else:
    # คำนวณค่าเฉลี่ย
    total = 0.0
    for g in grades:
        total += g
    average = total / len(grades)

    # หาค่าสูงสุด
    max_grade = grades[0]
    max_name = names[0]
    i = 1
    while i < len(grades):
        if grades[i] > max_grade:
            max_grade = grades[i]
            max_name = names[i]
        i += 1

    # หาค่าต่ำสุด
    min_grade = grades[0]
    min_name = names[0]
    j = 1
    while j < len(grades):
        if grades[j] < min_grade:
            min_grade = grades[j]
            min_name = names[j]
        j += 1

    print(f"Average : {average:.2f}")
    print(f"Max : {max_name}")
    print(f"Min : {min_name}")
