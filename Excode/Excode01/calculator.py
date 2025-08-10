#เครื่องคิดเลขแบบง่าย
a =int(input())
op =input("ใส่เครื่องหมาย :")
b=int(input())
if op =="+":
  z=a+b
elif  op == "-":
    z=a-b
elif  op == "/":
      z=a / b
elif  op == "*":
        z=a*b
else:
      print("กรอกเครื่องหมายผิด")
      z=None
if z is not None:
  print("คำตอบ =",z)