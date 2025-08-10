def saveEnployee(*args):
    # args: (name, department, address [, salary])
    name = args[0]
    department = args[1]
    address = args[2]
    
    # ถ้าส่งเงินเดือนมา → ใช้ค่านั้น, ถ้าไม่ส่ง → ใช้ 25000
    if len(args) >= 4:
        salary = args[3]
    else:
        salary = 25000

    print(f"ชื่อ: {name} , ตำแหน่ง: {department}")
    print(f"เงินเดือน: {salary}")
    print(f"ที่อยู่: {address}")
    print("------------------------")

# เรียกใช้งาน
saveEnployee("สายชล", "ผู้พัฒนา", "เมืองศรีสะเกษ", 45000)  # ใส่เงินเดือนเอง
saveEnployee("นน", "ช่างไฟ", "ศรีรัตนะ")                     # ใช้ default 25000
saveEnployee("ปิง", "ช่างกลึง", "อุทุมพร")                   # ใช้ default 25000
