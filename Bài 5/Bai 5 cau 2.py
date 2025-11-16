print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

import datetime as dt


format = '%Y-%m-%dT%H:%M:%S'
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)

print('Day      :', t1.day)
print('Month    :', t1.month)
print('Year     :', t1.year)
print('Hour     :', t1.hour)
print('Minute   :', t1.minute)
print('Second   :', t1.second)

t2 = dt.datetime.now()
diff = t2 - t1
print('How many days difference?', diff.days)
