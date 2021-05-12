#generate JSC table
import random
from faker import Faker, Factory
import xlwt
from data_1 import sno_data
from data_2_2 import  c_id_data

jsc_test = []
jsc_test_temp =()
c_id_data_temp = ['CS-01','CS-02','CS-04','EE-01','EE-02']
c_id_data.extend(c_id_data_temp)
f = Faker(locale='zh_cn')
ws = xlwt.Workbook()
shet = ws.add_sheet(u'abc')
path = r"D:\jsc.xls"
#grade s# c#
grade = 0
sno = ''
c_id = ''
n = 0
while n <= 5000:
    n += 1
    sno = ''.join(random.choice(sno_data))
    c_id = ''.join(random.choice(c_id_data))
    jsc_test_temp = (sno,c_id)
    while jsc_test_temp in jsc_test:
        sno = ''.join(random.choice(sno_data))
        c_id = ''.join(random.choice(c_id_data))
        jsc_test_temp = (sno, c_id)
    jsc_test.append(jsc_test_temp)
    grade = f.pyint(min_value=1, max_value=100, step=1)
    shet.write(n, 0, sno)  # 第一个参数表示行，第二个表示列,第三个自己需要的数据
    shet.write(n, 1, c_id)
    shet.write(n, 2, grade)
    ws.save(path)
