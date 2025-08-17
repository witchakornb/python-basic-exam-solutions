# Bonus: ตำนานพีระมิดแห่งตึกวิทยวิภาส
# แนวคิดพื้นฐาน:
# 1. รับค่า N (จำนวนแถวของพีระมิด) (1-50)
# 2. จำนวนกล่องทั้งหมด = 1 + 2 + ... + N = N*(N+1)/2 (ใช้สูตรเพื่อความเร็ว หรือบวกทีละชั้นก็ได้)
# 3. ตรวจว่าเป็นเลขคู่หรือคี่ด้วยการใช้ total % 2
# 4. ถ้าเป็นเลขคู่: แสดงพีระมิดจาก 1 ถึง N
#    ถ้าเป็นเลขคี่: แสดงพีระมิดกลับหัวจาก N ถึง 1
# 5. พิมพ์แต่ละแถวด้วยตัวเลขซ้ำตามหมายเลขแถวนั้น เช่น แถวที่ 3 => 3 3 3
# ใช้วิธีพื้นฐาน for loop ไม่ใช้ list ซับซ้อน เพื่อให้ผู้เริ่มต้นเข้าใจง่าย

N = int(input("Enter the number of rows for the pyramid: "))

# คำนวณจำนวนกล่องทั้งหมดแบบบวกทีละชั้น (ให้เห็นแนวคิด)
total = 0
for i in range(1, N + 1):
    total += i

print(f"The total number of boxes: {total}")

if total % 2 == 0:
    print("The total number of boxes is even")
    # พิมพ์จาก 1 -> N
    for row in range(1, N + 1):
        # สร้างสตริงตัวเลขซ้ำ row ครั้ง คั่นด้วยช่องว่าง
        line = ""
        for c in range(row):
            if c == 0:
                line += str(row)
            else:
                line += " " + str(row)
        print(line)
else:
    print("The total number of boxes is odd")
    # พิมพ์จาก N -> 1
    for row in range(N, 0, -1):
        line = ""
        for c in range(row):
            if c == 0:
                line += str(row)
            else:
                line += " " + str(row)
        print(line)
