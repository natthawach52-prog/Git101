#List โดย ก้องรักสยาม

print('----List---- \n----List----')
product=list(("กาวเกง",235.56,True))#หรือ[]
print(type(product))
print(len(product))

#เข้าถึงสมาชิก
print(product[0])#หรือ -3
print(product[1])#หริอ -2
print("================")

product[0]="เสื้อ"#เปลี่ยนแปลงข้อมูล
for element in product:
    print(element)
print("================")
color1=["สีดำ","สีแดง","สีดำ"]
color2=["สีแดง","สีส้ม","สีขาว"]

Allcolor = color1 + color2
print(Allcolor)

#การเช้าถึงข้อมูลแบบกำหนดช่วง
print(Allcolor[2:5])
print("================")

Allcolor.append("สีน้ำตาล")#เพิ่มข้อมูลต่อท้าย 1 จำนวน 
Allcolor.extend(["สีขาว","สีดำ"])#เพิ่มข้อมูลต่อท้ายหลายจำนวน
Allcolor.insert(2,"สีเทา")#สำหรับแทรกข้อมูลลงไป
print(Allcolor)
Allcolor.remove("สีดำ")#สำหรับลบข้อความบางส่วน
print(Allcolor.count("สีแดง"))#สำหรับนับจำนวนที่ซ้ำกัน
print(Allcolor)
Allcolor.clear()#สำหรับลบข้อมูลทั้งหมด
print(Allcolor)

print("================")
color3=["แดง","ส้ม","เหลือง","ขาว","เทา","เขียว"]
color3.sort()#จัดเรียงข้อมูลโดย_พยัญชนะขึ้นก่อนตามด้วยสระ
print(color3)
color3.reverse()#กลับคำจากหลังไปหน้า
print(color3)
print("================")
numbers=["23","67","6","39","1"]
numbers.sort()#จัดเรียงข้อมูลโดย_พยัญชนะขึ้นก่อนตามด้วยสระ
print(numbers)



