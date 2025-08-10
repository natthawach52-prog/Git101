class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, จำนวนเงิน):
        self.balance += จำนวนเงิน
        print(f"ฝากเงิน {จำนวนเงิน} บาท")

    def show_balance(self):
        print(f"ยอดเงินคงเหลือ: {self.balance} บาท")

# ทดลองใช้งาน
account = BankAccount()
account.deposit(50)
account.deposit(200)
account.show_balance()
