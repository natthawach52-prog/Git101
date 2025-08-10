print('----Tuple---- \n----Tuple----')#เปลี่ยนแปลงค่าไม่ได้
#การเข้าถึงสมาชิก print(product[3])#หรือ-1
product=("เสื้อ", 239.0, 25)
(name,price,stock) = product #ใส่วงเล็บหรือไม่ใส่ก็ได้
print(name)
print(price)
print(stock)

#ตรวจสอบชนิดข้อมูล
print(type(product))
print("================")

#ตัวอย่างการใช้ For loop
for element in product:
    print(element)


#ฟังชั่นสำหรับนับจำนวนสมาชิกว่ามีค่าซ้ำกันกี่จุด Print(ตัวแปร.count())
#ฟังชั่นสำหรับค้นหาข้อมูล Print(ตัวแปร.index("ใส่ข้อมูลที่ต้องการค้นหา"))
#ใช้ len เพื่อตรวจสอบข้อมูล
#เชื่อม Tuple ตัวแปร3=ตัวแปร1+ตัวแปร2
#สามารถใช้ print(ตัวแปร*2) เพื่อทำให้มันปริ้นตัวแปร*2ได้