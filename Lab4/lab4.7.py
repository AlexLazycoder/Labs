import datetime

week_days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
now = datetime.datetime.now()
day = week_days[now.weekday()]

if day == 'Monday':
    print ('1')
if day == 'Tuesday':
    print ('2')
if day == 'Wednesday':
    print ('3')
if day == 'Thursday':
    print('4')
if day == 'Friday':
    print('5')
if day == 'Saturday':
    print('6')
if day == 'Sunday':
    print('7')