class Bankaccount :
    def __init__(self, name):
        self.name = name
        self.Allmoney = 0.0

    def deposit(self, money):
        if money > 0:
            self.Allmoney += money
            print(f"{self.name}: ฝากเงิน {money:.2f} บาทเรียบร้อยแล้ว")
        else :
            print("ยอดเงินที่ต้องการฝากต้องมากกส่า 0 บาท")  

    def withdraw(self, money):
        if money <= 0:
            print("จำนวนเงินที่ต้องการถอนต้องมากกว่า 0 บาท")
        elif money > self.Allmoney:
            print("ไอ้จน")
        else:
            self.Allmoney -= money
            print(f"{self.name}: ถอนเงิน {money:.2f} บาท")

    def show_info(self):
        print(f"{self.name}: ยอดเงินคงเหลือ {self.Allmoney} บาทถ้วน")

acc_1 = Bankaccount("บัญชีที่ 1")
acc_2 = Bankaccount("บัญชีที่ 2")

def choose_account():
    while True:
        print("\n--- เลือกบัญชี ---")
        print("1. บัญชีที่ 1")
        print("2. บัญชีที่ 2")
        print("3. ออกจากระบบ")

        choice = input("เลือกบัญชี (1-3): ")

        if choice == "1":
             do_transaction(acc_1)
        elif choice == "2":
             do_transaction(acc_2)
        elif choice == "3":
            print("ขอให้วันนี้เป็นวันที่ดี")
            break
        else :
            print("เลือกเมนูไม่ถูกต้อง")

def do_transaction(account):
    while True:
        print(f"\n--- เมนูธุรกรรม: {account.name} ---")
        print("1. ฝากเงิน")
        print("2. ถอนเงิน")
        print("3. แสดงยอดเงิน")
        print("4. กลับไปหน้าเลือกบัญชี")

        action = input("เลือกเมนู (1-4): ")

        if action == "1":
            money = float(input("จำนวนเงินที่ต้องการฝาก: "))
            account.deposit(money)
        elif action == "2":
            money = float(input("จำนวนเงินที่ต้องการถอน: "))
            account.withdraw(money)
        elif action == "3":
            account.show_info()
        elif action == "4":
            print(f"กลับสู่หน้าเลือกบัญชีเรียบร้อย")
            break
        else :
            print("เมนูไม่ถูกต้อง")

choose_account()