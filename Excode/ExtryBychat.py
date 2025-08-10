# ตัวอย่างการใช้ try-except จับ Error หลายชนิด + พิมพ์ exit เพื่อออก
while True:
    user_input = input("กรอกอายุ (พิมพ์ exit เพื่อออก): ")
    if user_input.lower() == "exit":
        print("ลาก่อนค่ะ ❤️")
        break

    try:
        # ValueError: กรอกไม่ใช่ตัวเลข
        age = int(user_input)

        # ZeroDivisionError: หารด้วยศูนย์
        divisor_input = input("ใส่ตัวหาร (พิมพ์ exit เพื่อออก): ")
        if divisor_input.lower() == "exit":
            print("ลาก่อนค่ะ ❤️")
            break
        result = 10 / int(divisor_input)

        # IndexError: เข้าถึงตำแหน่ง list ที่ไม่มี
        my_list = [1, 2, 3]
        print("ค่าในตำแหน่ง 5 คือ:", my_list[5])

        # KeyError: ใช้ key ที่ไม่มีใน dictionary
        my_dict = {"name": "Alice"}
        print("ค่า city คือ:", my_dict["city"])

        break

    except ValueError:
        print("⚠️ กรอกตัวเลขเท่านั้นนะคะ")

    except ZeroDivisionError:
        print("⚠️ หารด้วยศูนย์ไม่ได้นะคะ")

    except IndexError:
        print("⚠️ ไม่มีตำแหน่งนั้นใน list")

    except KeyError:
        print("⚠️ ไม่มี key นี้ใน dictionary")

    except Exception as e:
        # จับ error อื่น ๆ ที่ไม่ระบุไว้ข้างบน
        print(f"เกิดข้อผิดพลาดอื่น: {e}")

    finally:
        print("✅ จบการทำงานรอบนี้\n")
