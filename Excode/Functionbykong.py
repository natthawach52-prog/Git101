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
#saveEnployee("สายชล", "ผู้พัฒนา", "เมืองศรีสะเกษ", 45000)  # ใส่เงินเดือนเอง
#saveEnployee("นน", "ช่างไฟ", "ศรีรัตนะ")                     # ใช้ default 25000
#aveEnployee("ปิง", "ช่างกลึง", "อุทุมพร")                   # ใช้ default 25000


#para + retrun fuction

def checkNumber(num):
    if num %2==0:
       return "เลขคู๋"
    else :
        return "เลขคี่"
    
#Number = int(input("ป้อนเลข"))
#result = checkNumber(Number)
#print(result)

def summation(*data):
    total=0
    for item in data :
        total+=item
    return total

#print(summation(10,39,40))

#lamda function 2^3
def power(base,n):
    return base**n

result= power(4,5)
print(result)