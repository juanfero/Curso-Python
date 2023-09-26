file = open('./text.txt')
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

for line in file:
  print(line)

file.close()

#esta es la mejor forma de abrir un archivo 
with open('./txt.txt', 'r+') as file:
  for line in file:
    print(line)

'''
with open("./archivos/numbers.txt", "r", encoding="UTF-8") as f:
'''
 
 
  