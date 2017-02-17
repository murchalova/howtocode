n = input('Введите имя: ')
c = len(n)

print ('Hello,',n + '!')
print('You have',c,'characters in your name.')
if c % 2 == 0:
    print('It is an even number.')
else:
    print('It is an uneven number.')
