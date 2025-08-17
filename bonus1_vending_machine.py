# Bonus: Rabbit vender V.2 (เครื่องกดเครื่องดื่ม)
# แนวคิด:
# 1. กำหนดข้อมูลสินค้า (ชื่อ ราคา จำนวนคงเหลือ) ในตัวแปรแยก ๆ แบบพื้นฐาน
# 2. แสดงรายการสินค้า
# 3. รับหมายเลขสินค้า และจำนวนที่ต้องการซื้อ
# 4. ตรวจสอบว่าสินค้ามีพอหรือไม่ / หรือจำนวนคงเหลือเป็น 0 -> แสดงข้อความหมดสต็อก
# 5. ถ้าพอ: คำนวณราคารวม = จำนวน * ราคา แล้วแสดงผล
# หมายเหตุ: ใช้วิธีง่าย ไม่ใช้ list หรือ dict เพื่อให้เห็นโครงสร้างพื้นฐาน

# กำหนดข้อมูลสินค้า
coffee_price = 2.5
coffee_qty = 10
tea_price = 1.5
tea_qty = 0
juice_price = 3.0
juice_qty = 2

print("Beverage List:")
print(f"1. Coffee - $%s - Quantity: %s" % (coffee_price, coffee_qty))
print(f"2. Tea - $%s - Quantity: %s" % (tea_price, tea_qty))
print(f"3. Juice - $%s - Quantity: %s" % (juice_price, juice_qty))

choice = int(input("Enter the number of the beverage you want to purchase: "))
qty = int(input("Enter the quantity you want to purchase: "))

# ตรวจสอบตามหมายเลข
if choice == 1:
    if coffee_qty == 0 or qty > coffee_qty:
        print("Sorry, Coffee is out of stock")
    else:
        total = qty * coffee_price
        print(f"You purchased {qty} Coffee for ${total}")
        print("Enjoy your drink!")
elif choice == 2:
    if tea_qty == 0 or qty > tea_qty:
        print("Sorry, Tea is out of stock")
    else:
        total = qty * tea_price
        print(f"You purchased {qty} Tea for ${total}")
        print("Enjoy your drink!")
elif choice == 3:
    if juice_qty == 0 or qty > juice_qty:
        print("Sorry, Juice is out of stock")
    else:
        total = qty * juice_price
        print(f"You purchased {qty} Juice for ${total}")
        print("Enjoy your drink!")
else:
    print("Invalid selection")
