#integer แปลงเป็นเลขฐานต่างๆ

a = 0b1010010#แปลงจากฐานสองเป็นจำนวนเต็ม
print("แปลงจากฐานสองเป็นจำนวนเต็ม =",a)

b=266 #แปลงเป็นฐานสอง
c=bin(b)
print(c)

d = 350 #แปลงเป็นฐาน16
e = hex(d)
print(e)
#float เลขที่มีทศนิยม
f = 2.45
g = 2.75e-2
print(g)

#complex number
i = 2+8j
print(i.imag)
print(i.real)