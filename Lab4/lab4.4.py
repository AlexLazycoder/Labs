second = int(input('Введіть кількість секунд: '))
hour = second / 3600
minute = (second / 60) % 60
sec = second % 60
if minute < 10:
    minute = '0' + str(minute)
else:
    minute = str(minute)
if sec<10:
    sec = '0' + str(sec)
else:
    sec = str(sec)
print('Години: ', hour, 'Хвилини: ', minute, 'Секунди: ', sec)