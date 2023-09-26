num=[1,7,2,5,6,1,3]

for i in num:
    print(i)

for x in range(1,30,2):
    print(x)
else:
    print('finish')

for y in num:
    if y==5:
        print('se encontro el 5')

for j in num:
    if j==6:
        continue
    print(j)

dic={
    'name':'juan',
    'age': 12
}

for x, y in dic.items():
    print(x,'=>',y)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    


