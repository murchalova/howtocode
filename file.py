with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write('1\n')
   f.write('2\n')
   f.write('3\n')
   f.write('4\n')
   f.write('5\n')
   f.write('6\n')
   f.write('7\n')
   f.write('8\n')
   f.write('9\n')
   f.write('10\n')

f = open("test.txt")
print(f.read(34))


def firstline(n):
   with open("test.txt", encoding='utf-8') as f:
      line = f.readlines()
      for i in range(n):
         print(line[i])


def delline(n):
   with open("test.txt", encoding='utf-8') as f:
      line = f.readlines()
      line.remove(line[n - 1])
   with open("test.txt", 'w', encoding='utf-8') as f:
      f.writelines(line)

