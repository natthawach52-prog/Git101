
#แม่สูตรคูณ
'''
num = int(input('ป้อนตัวเลขแม่สูตรคูณ'))

# i*1-i*12
for i in range (1,13):
    print(num,"x",i,'=',num*i)

'''
#หาผลรวมของตัวเลข 5 จำนวน

total=0
for i in range(1,5+1) :
    num = int(input("ลำดับที่ "+str(i)+":"))
    total+=num

print("ผลรวม =",total)

#หาผลรวมของตัวเลขไม่จำกัดจำนวน
'''
total=0
while True:
    num = int(input('ป้อนตัวเลข:'))
    if num <=0:
        break
    total+=num

print('ผลรวม =',total)
'''
#Nested-loop
'''
for i in range(2):
    print('รอบที่:',i)
    for j in range(3):
        print(j)
'''
#แม่สูตรคูณแบบกำหนดช่วง
'''
start= int(input("แม่สูตรคูณเริ่มต้น :")) 
end= int(input("แม่สูตรคูณสุดท้าย :"))    

for num in range(start,end+1):
    print("สูตรคูณแม่",num)
    print('---------------') 
    for num1 in range(1,13):
      print(num,'x',num1," = ",num*num1)
    print('---------------')
'''