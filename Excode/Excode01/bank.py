class BankAccount:
    def __init__(self):
        self.balance = 0.0  # เริ่มต้นยอดเงินเป็น 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"ฝากเงินจำนวน {amount:.2f} บาทเรียบร้อยแล้ว")
        else:
            print("จำนวนเงินที่ฝากต้องมากกว่า 0 บาท")

    def withdraw(self, amount):
        if amount > self.balance:
            print("ยอดเงินไม่พอสำหรับการถอน")
        elif amount <= 0:
            print("จำนวนเงินที่ถอนต้องมากกว่า 0 บาท")
        else:
            self.balance -= amount
            print(f"ถอนเงินจำนวน {amount:.2f} บาทเรียบร้อยแล้ว")

    def show_balance(self):
        print(f"ยอดเงินปัจจุบัน: {self.balance:.2f} บาท")

# ตัวอย่างการใช้งาน
account = BankAccount()

while True:
    print("\n--- เมนู ---")
    print("1. ฝากเงิน")
    print("2. ถอนเงิน")
    print("3. แสดงยอดเงิน")
    print("4. ออกจากโปรแกรม")

    choice = input("เลือกเมนู (1-4): ")

    if choice == '1':
        amount = float(input("ใส่จำนวนเงินที่ต้องการฝาก: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("ใส่จำนวนเงินที่ต้องการถอน: "))
        account.withdraw(amount)
    elif choice == '3':
        account.show_balance()
    elif choice == '4':
        print("ออกจากระบบแล้ว")
        break
    else:
        print("กรุณาเลือกเมนูที่ถูกต้อง")
