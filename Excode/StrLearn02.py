
#ตรวจสอบคำขึ้นต้น 
'''
name=input("ป้อนชื่อของคุณ")
if name.startswith("นาย"):
    print("เป็นเพศชาย")
elif name.startswith("นางสาว"):
    print("เป็นเพศหญิง")
elif name.startswith("นาง"):
    print("เป็นผู้หญิง")
'''

#---------------------------

#ตรวจสอบคำลงท้าย
'''
mouth=input("ป้อนเดือน: ")
if mouth.endswith("คม"):
    print("เดือนนี้มี 31 วัน")
elif mouth.endswith("ยน"):
    print("เดือนนี้มี 30 วัน")
'''

#---------------------------

#ตรวจสอบว่ามีคำนั้นมั้ย
'''
text = "kuyChonnaHee"
print(text.find("Hee"))
'''
#---------------------------

#ตรวจสอบว่ามีตัวอักษรนั้นกี่ตัว
'''
text = "" \
"sdfjksjkfkaeklhahefkjaklgblrehgfiaehkjhfkjsahfksahkfhksafksahfi4ukjbsbfjskfhkjashkkasfkafkhs" \
""
print(text.count("ka"))
'''
#---------------------------

#แทนที่ข้อมูลเดิมด้วยข้อมูลใหม่
'''
sunya="สัญญาจ้างงานประจำปี 2567 มีผลตั้งแต่ 1 มกราคม 2567 ถึง 31 ธันวาคม 2567"
update =sunya.replace("2567","2568")
print(update)
'''
#---------------------------

#ลบช่องว่างซ้ายขวา

text=" javascrips ".strip()
print(len(text))

#---------------------------

#จัดรูปแบบข้อมูล

#info="ฉันชื่อ {0} อายุ {1} ปี".format("สายชล", 16)
#print(info)