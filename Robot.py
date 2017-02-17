n = input('Введите имя: ')
c = len(n)

print ('Hello,',n + '!')
print('You have',c,'characters in your name.')
if c % 2 == 0:
    i = 'even number.'
    print('It is an', i)
else:
    i = 'odd number.'
    print('It is an', i)
