# Problem 3: นปโปะการค้า (ระบบคำนวณส่วนลด)
# แนวคิด:
# 1. รับสถานะสมาชิก (y/n)
# 2. รับยอดซื้อ (จำนวนเต็มหรือทศนิยม)
# 3. ตรวจตามเงื่อนไขส่วนลด:
#    - สมาชิกและ >= 1000 -> 20%
#    - สมาชิกและ 500-999  -> 10%
#    - ไม่เป็นสมาชิกและ >= 1000 -> 5%
#    - อื่นๆ -> 0%
# 4. คำนวณส่วนลดและยอดสุทธิ
# 5. แสดงผลด้วยทศนิยม 2 ตำแหน่ง

member_input = input("Membership (y/n) : ")
amount = float(input("Total amount : "))

if member_input == 'y':
    if amount >= 1000:
        discount = amount * 0.20
    elif amount >= 500:  # 500 - 999
        discount = amount * 0.10
    else:
        discount = 0.0
else:  # ไม่เป็นสมาชิก
    if amount >= 1000:
        discount = amount * 0.05
    else:
        discount = 0.0

final_amount = amount - discount

print(f"Discount : {discount:.2f}")
print(f"Final Amount to Pay : {final_amount:.2f}")
