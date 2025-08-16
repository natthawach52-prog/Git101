import random

# ฟังก์ชันเพิ่มนักเรียน
def add_student(students):
    name = input("กรอกชื่อนักเรียน: ")
    score = random.randint(0, 100)  # สุ่มคะแนน 0-100
    students.append({"name": name, "score": score})
    print(f"เพิ่ม {name} เรียบร้อย ได้คะแนน {score}")

# ฟังก์ชันแสดงรายชื่อนักเรียนทั้งหมด
def show_students(students):
    if not students:
        print("ยังไม่มีนักเรียนในระบบ")
    else:
        print("\n=== รายชื่อนักเรียน ===")
        for i, student in enumerate(students, start=1):
            print(f"{i}. {student['name']} - {student['score']} คะแนน")

# ฟังก์ชันคำนวณคะแนนเฉลี่ย
def average_score(students):
    if not students:
        print("ไม่มีข้อมูลนักเรียน")
    else:
        avg = sum(s["score"] for s in students) / len(students)
        print(f"คะแนนเฉลี่ย: {avg:.2f}")

# เริ่มโปรแกรมหลัก
students = []

while True:
    print("\n=== เมนู ===")
    print("1. เพิ่มนักเรียน")
    print("2. แสดงรายชื่อ")
    print("3. คำนวณคะแนนเฉลี่ย")
    print("4. ออกจากโปรแกรม")

    choice = input("เลือกเมนู (1-4): ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        show_students(students)
    elif choice == "3":
        average_score(students)
    elif choice == "4":
        print("จบการทำงาน")
        break
    else:
        print("กรุณาเลือกเมนูให้ถูกต้อง")
