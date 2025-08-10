class myfriend :
    def __init__(self, name, high, weight):
        self.name = name
        self.high = high
        self.weight = weight
    def show_info(self):
        print("ชื่อ :",self.name)
        print("ส่วนสูง :",self.high)
        print("ส่วนสูง :",self.weight)

print("🤵เพื่อนคนที่ 1: ")
name_one=input("ใส่ชื่อเพื่อน: ")
high_one=input("ใส่ส่วนสูง: ")
weight_one=input("ใส่น้ำหนัก: ")

print("🤵เพื่อนคนที่ 2: ")
name_two=input("ใส่ชื่อเพื่อน: ")
high_two=input("ใส่ส่วนสูง: ")
weight_two=input("ใส่น้ำหนัก: ")

print("🤵เพื่อนคนที่ 3: ")
name_three=input("ใส่ชื่อเพื่อน: ")
high_three=input("ใส่ส่วนสูง: ")
weight_three=input("ใส่น้ำหนัก: ")

myfriend_one = myfriend(name_one, high_one, weight_one)
myfriend_two = myfriend(name_two, high_two, weight_two)
myfriend_three = myfriend(name_three, high_three,weight_three)

print("🫂เพื่อนคนที่ 1:")
myfriend_one.show_info()

print("🫂เพื่อนคนที่ 2:")
myfriend_two.show_info()

print("🫂เพื่อนคนที่ 3:")
myfriend_three.show_info()



