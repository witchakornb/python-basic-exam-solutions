# Problem 1: Fruit Basket (ตะกร้าผลไม้)
# แนวคิด (Idea):
# 1. รับชื่อผลไม้และน้ำหนัก 4 ครั้ง (ใช้ input ทีละบรรทัด)
# 2. เก็บชื่อและน้ำหนักไว้ใน list (หรือจะใช้ตัวแปรแยกก็ได้ สำหรับผู้เริ่มต้น)
# 3. คำนวณผลรวมของน้ำหนักทั้งหมด
# 4. แสดงผลออกมาแบบจัดให้ช่องว่างพอดูตรง อ่านง่าย
# 5. ใช้การ format ตัวเลขทศนิยม 2 ตำแหน่งด้วย format หรือ f-string
# หมายเหตุ: ใช้วิธีง่าย ไม่ใช้ loop ซ้ำซ้อนเพื่อให้คนเริ่มเรียนเข้าใจ

# รับข้อมูล 4 รายการ
item1 = input("Enter item 1 : ")
weight1 = float(input("Enter weight 1 : "))
item2 = input("Enter item 2 : ")
weight2 = float(input("Enter weight 2 : "))
item3 = input("Enter item 3 : ")
weight3 = float(input("Enter weight 3 : "))
item4 = input("Enter item 4 : ")
weight4 = float(input("Enter weight 4 : "))

# คำนวณผลรวม
total = weight1 + weight2 + weight3 + weight4

# แสดงผล (ใช้ Tab คั่นระหว่างชื่อกับน้ำหนัก)
print(f"{item1}\t{weight1:.2f}")
print(f"{item2}\t{weight2:.2f}")
print(f"{item3}\t{weight3:.2f}")
print(f"{item4}\t{weight4:.2f}")
print("---------------------------")  # ตามที่ระบุให้ copy เลย
print(f"total\t{total:.2f}")
