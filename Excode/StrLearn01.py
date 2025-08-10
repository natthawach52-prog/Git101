#เจาะลึก String
print('----1---- \n----1----')
fname ='Chon'
lname= 'tedHee'

fullname =fname + lname + 'ไอ้ควาย'
print(fullname)

print('----2---- \n----2----')

myfriend="""chon
folk
Tee
non
ping"""

print(myfriend)

print('----3---- \n----3----')

text = "ChonTedHee" #0-10, -1 ถึง -10
print(len(text))
text = "ChonTedHee"
print(text[5])
text = "ChonTedHee"
print(text[4:])
text = "ChonTedHee"
print(text[:4])
text = "ChonTedHee"
print(text[-6:-3]) #หรือ(4,7),(-6,-3)

print('----4---- \n----4----')

name ="ChonKuayLeg"
print(name.upper())
print(name.lower())

name_text="นายสายชลเสียชีวิต"
print(name_text.startswith("นาย"))