import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("เกมทายตัวเลข")
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        # สร้าง Label แสดงคำแนะนำ
        self.label = tk.Label(root, text="กรุณาทายตัวเลขระหว่าง 1 ถึง 100", font=("TH Sarabun New", 16))
        self.label.pack(pady=10)

        # ช่องกรอกตัวเลข
        self.entry = tk.Entry(root, font=("TH Sarabun New", 16))
        self.entry.pack(pady=10)

        # ปุ่มยืนยันการทาย
        self.guess_button = tk.Button(root, text="ทาย", command=self.check_guess, font=("TH Sarabun New", 16))
        self.guess_button.pack(pady=10)

        # Label แสดงผลลัพธ์
        self.result_label = tk.Label(root, text="", font=("TH Sarabun New", 16))
        self.result_label.pack(pady=10)

        # ปุ่มรีเซ็ตเกม
        self.reset_button = tk.Button(root, text="เริ่มใหม่", command=self.reset_game, font=("TH Sarabun New", 14))
        self.reset_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < 1 or guess > 100:
                self.result_label.config(text="กรุณาใส่ตัวเลขระหว่าง 1 ถึง 100 เท่านั้น!")
            elif guess < self.number_to_guess:
                self.result_label.config(text="ตัวเลขที่คุณทายน้อยเกินไป ลองใหม่อีกครั้ง.")
            elif guess > self.number_to_guess:
                self.result_label.config(text="ตัวเลขที่คุณทายมากเกินไป ลองใหม่อีกครั้ง.")
            else:
                self.result_label.config(
                    text=f"ยินดีด้วย! คุณทายถูกต้องแล้ว ตัวเลขคือ {self.number_to_guess}\n"
                         f"คุณใช้จำนวนครั้งในการทายทั้งหมด {self.attempts} ครั้ง"
                )
        except ValueError:
            self.result_label.config(text="กรุณาใส่ตัวเลขเท่านั้น!")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.label.config(text="กรุณาทายตัวเลขระหว่าง 1 ถึง 100")

# สร้างหน้าต่างหลักและเรียกใช้เกม
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()


