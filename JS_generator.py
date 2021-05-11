#generate JS table
import random
from faker import Faker, Factory
import xlwt

direction = ['东','南','西','北']
sex = ['男','女']
f = Faker(locale='zh_cn')
ws = xlwt.Workbook()
shet = ws.add_sheet(u'abc')
dormstr = ''
sno = ''
sno_data = []
bdate = ''
height = ''
path = r"D:\js.xls"
n = 0
while n <= 1000:
    n += 1
    dormstr = ''.join(random.choice(direction)) + \
              str(f.pyint(min_value=1,max_value=30,step=1)) +'舍'+\
              str(f.pyint(min_value=1,max_value=600,step=1))
    sno = '0' + str(f.pyint(min_value=1000000, max_value=9999999, step=1))
    while sno  in sno_data:
        sno = '0' + str(f.pyint(min_value=1000000, max_value=9999999, step=1))
    sno_data.append(sno)
    bdate = str(f.date_of_birth(minimum_age = 18,maximum_age = 30) )
    height = '1.'+str(f.pyint(min_value=50, max_value=95, step=1))
    shet.write(n, 0, sno)
    shet.write(n, 1, f.name() )  # 第一个参数表示行，第二个表示列,第三个自己需要的数据
    shet.write(n, 2, ''.join(random.choice(sex)))
    shet.write(n, 3, bdate)
    shet.write(n, 4, height )
    shet.write(n, 5, dormstr)
    ws.save(path)
