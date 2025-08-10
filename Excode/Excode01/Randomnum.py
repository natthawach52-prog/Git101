import random

number = random.randint(1, 1001)
print("🎲 ทายเลขระหว่าง 1 ถึง 1000")

while True:
    guess = int(input("คุณคิดว่าเป็นเลขอะไร?: "))
    if guess == number:
        print("ถูกต้อง! ยินดีด้วย 🎉")
        break
    elif guess < number:
        print("มากกว่านี้หน่อยครับ")
    else:
        print("น้อยกว่านี้อีกนิดครับ")