class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.name}: ฝากเงิน {amount:.2f} บาทเรียบร้อยแล้ว")
        else:
            print("จำนวนเงินที่ฝากต้องมากกว่า 0 บาทนะจ๊ะ")

    def withdraw(self, amount):
        if amount <= 0:
            print("จำนวนเงินที่ถอนต้องมากกว่า 0 บาทนะจ๊ะ")
        elif amount > self.balance:
            print("ยอดเงินไม่เพียงพอสำหรับการถอนจ้า~")
        else:
            self.balance -= amount
            print(f"{self.name}: ถอนเงิน {amount:.2f} บาทเรียบร้อยแล้ว")

    def show_balance(self):
        print(f"{self.name}: ยอดเงินคงเหลือ {self.balance:.2f} บาท")

# สร้างบัญชี 2 บัญชี
account1 = BankAccount("บัญชีที่ 1")
account2 = BankAccount("บัญชีที่ 2")

def choose_account():
    while True:
        print("\n--- เลือกบัญชี ---")
        print("1. บัญชีที่ 1")
        print("2. บัญชีที่ 2")
        print("3. ออกจากระบบ")

        choice = input("กรุณาเลือกบัญชี (1-3): ")

        if choice == '1':
            do_transaction(account1)
        elif choice == '2':
            do_transaction(account2)
        elif choice == '3':
            print("ขอบคุณที่ใช้บริการค่ะ ♥")
            break
        else:
            print("กรุณาเลือกเลข 1, 2 หรือ 3 เท่านั้นนะจ๊ะ")

def do_transaction(account):
    while True:
        print(f"\n--- เมนูธุรกรรม: {account.name} ---")
        print("1. ฝากเงิน")
        print("2. ถอนเงิน")
        print("3. แสดงยอดเงิน")
        print("4. กลับไปหน้าเลือกบัญชี")

        action = input("เลือกเมนู (1-4): ")

        if action == '1':
            amount = float(input("จำนวนเงินที่ต้องการฝาก: "))
            account.deposit(amount)
        elif action == '2':
            amount = float(input("จำนวนเงินที่ต้องการถอน: "))
            account.withdraw(amount)
        elif action == '3':
            account.show_balance()
        elif action == '4':
            print(f"กลับสู่หน้าเลือกบัญชีแล้วค่ะ~\n")
            break
        else:
            print("เมนูไม่ถูกต้อง กรุณาเลือก 1-4 นะคะ")

# เริ่มระบบ
choose_account()
