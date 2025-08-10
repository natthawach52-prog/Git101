print('----1---- \n----1----')

#while loop
cot=0
while cot<5:
    cot +=1
    print(cot)

print('----2---- \n----2----')

#For loop
for j in range(5):
    print('chon and folk')

print('----3---- \n----3----')

#break
for counter in range(1,11):
    if counter == 5 :
        break
    print(counter)


print('----4---- \n----4----') 

#continue
for counter in range(10,21):
    if counter == 16 :
        continue
    elif counter== 18:
          continue
    print(counter)

print('----5---- \n----5----') 

text="folktedHee"
for i in text:
    print(i)