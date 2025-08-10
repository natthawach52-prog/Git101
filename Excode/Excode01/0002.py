def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
              return False
    return True

num = int(input("🔍 ป้อนตัวเลขเพื่อตรวจสอบว่าเป็นจำนวนเฉพาะหรือไม่: "))

if is_prime(num):
    print(f"✅ {num} เป็นจำนวนเฉพาะ")
else:
    print(f"❌ {num} ไม่ใช่จำนวนเฉพาะ")
