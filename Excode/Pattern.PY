print('\n------Literal Pattern-----')
service=1
match service:
    case 1:
        print("ฝากเงิน")
    case 2:
        print("ถอนเงิน")
    case 3:
        print("ตรวจสอบยอดเงิน")
    case none:
        print("หมายเลขบริการไม่ถูกต้อง")

print('\n------Wildcard Pattern-----')#มีการกำหนดเงื่อนไขแล้วเงื่อนไขที่รับเข้ามาไม่ตรงกับเคสที่มีอยู่
service="hahahaha"
match service:
    case 1:
        print("ฝากเงิน")
    case 2:
        print("ถอนเงิน")
    case 3:
        print("ตรวจสอบยอดเงิน")
    case _:
        print("หมายเลขบริการไม่ถูกต้อง")

print('\n------Capture Pattern-----')#นำเอาข้อมูลที่อยู่ในตัวแปรเพื่อบอกกับผู้ใช้งานว่านอกเหนือจากไม่ตรงกับเคสที่มีอยู่ไม่ตรงกับข้อมูล
#อะไรเลย ให้ป้อนข้อมูลใหม่

service="hahahaha"
match service:
    case 1:
        print("ฝากเงิน")
    case 2:
        print("ถอนเงิน")
    case 3:
        print("ตรวจสอบยอดเงิน")
    case service:
        print(f"ไม่มีบริการในหมายเลขหรือข้อมูลนั้น {service} ในระบบกรุณาทำรายการใหม่อีกครั้ง")

print('\n------Guard Filter-----')#100 = สอบได้คะแนนเต็ม ,50-99 = ผ่านเกณฑ์การทดสอบ
score = 75
#score = int(input("ป้อนคะแนนสอบของคุณ:  "))
print("คะแนนสอบของคุณ คือ: ",score)

match score:
    case 100:
        print("สอบได้คะแนนเต็ม")
    case score if score>=50 and score<=99 :
        print("ผ่านเกณฑ์การสอบ")
    case _:
        print("คะแนนไม่อยู่ในเกณฑ์ที่กำหนด")

print('\n------OR Pattern-----')#กำหนดเคสหลายๆ เคสแล้วเชื่อมกัน
data = "นาย"
#data = (input("ป้อนคำนำหน้า: ")).strip()

match data :
    case "เด็กชาย" | "นาย":
        print("เพศชาย")
    case "เด็กหญิง" | "นางสาว" | "นาง":
        print("เพศหญฺิง")
    case _:
        print("ข้อมูลไม่ถูกต้อง")

print('\n------Sequence Pattern-----')#บริหารจัดการข้อมูลในรูปแบบ list
data=[]
match data :
    case []:
        print("ไม่มีข้อมูล")
    case [1,2]:
        print("มีข้อมูล 2 รายการ 1 และ 2")
    case [1,2,3]:
        print("มีข้อมูล 3 รายการ 1,2 และ 3")

#บริหารจัดการข้อมูลที่อยู่ในรูปแบบ Dictionsry
customer=[
    {"name":"สายชล","type":"member"},
    {"name":"นนท์","type":"general"},
    {"name":"โฟก","type":"member"}
]
id=int(input("ป้อนรหัสลูกค้า"))
print(f"สวัสดีลูกค้า {id} :{customer[id]["name"]}")

match customer[id]:
    case {"type":"member"}:
        print("เป็นสมาชิกได้รับส่วนลด 16%")
    case _:
        print("ไม่ได้รับส่วนลด")