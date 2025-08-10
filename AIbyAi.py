import random

responses = {
    "สวัสดี": "สวัสดีครับ ยินดีที่ได้คุยกับคุณ!",
    "คุณชื่ออะไร": "ผมเป็นโปรแกรม Python ที่ถูกสร้างโดยนักเรียนสุดเท่ 😎",
    "บอกเรื่องตลก": "ทำไมเป็ดถึงไม่ไปโรงเรียน... เพราะมันขี้เกียจ 'เป็ด' เรียน! ฮ่า ๆ ๆ",
}

def chat():
    print("👋 ยินดีต้อนรับ! พิมพ์ 'exit' เพื่อออกจากโปรแกรม")
    while True:
        user_input = input("คุณ: ")
        if user_input.lower() == "exit":
            print("ลาก่อนครับ 👋")
            break
        response = responses.get(user_input, random.choice(["ขอโทษครับ ผมไม่เข้าใจ 😅", "คุณลองถามอีกแบบได้ไหมครับ?"]))
        print("AI: " + response)

chat()