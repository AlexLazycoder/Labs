number = int(input('Введіть натуральне число: '))

if number % 2 == 0:
    print('Число парне')
else:
    print('Число непарне')

if number % 10 == 5:
    print('Число закінчується на 5')
else:
    print('Число не закінчується на 5')