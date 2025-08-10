class Dog:
    def __init__(self, name, color):
        self.name = name     # Attribute
        self.color = color   # Attribute

    def bark(self):          # Method
        print(f"{self.name} บ๊อกๆ!")

    def col(self):           # Method
        print(f"สี: {self.color}")

# 🔹 รับข้อมูลจากผู้ใช้
print("🐶 กำลังเพิ่มหมาตัวที่ 1")
name1 = input("➡️ ใส่ชื่อหมา: ")
color1 = input("➡️ ใส่สีของหมา: ")

print("\n🐶 กำลังเพิ่มหมาตัวที่ 2")
name2 = input("➡️ ใส่ชื่อหมา: ")
color2 = input("➡️ ใส่สีของหมา: ")

# 🔹 สร้าง Object
dogone = Dog(name1, color1)
dogtwo = Dog(name2, color2)

# 🔹 แสดงข้อมูลหมาทั้งสองตัว
print("\n📌 ข้อมูลหมาของคุณ:")

print("\n🐾 ตัวที่ 1")
print(f"ชื่อ: {dogone.name}")
dogone.bark()
dogone.col()

print("\n🐾 ตัวที่ 2")
print(f"ชื่อ: {dogtwo.name}")
dogtwo.bark()
dogtwo.col()
