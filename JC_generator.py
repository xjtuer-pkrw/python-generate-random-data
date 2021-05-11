#generate JC table
#one cname multiple c#
import random
from faker import Faker, Factory
import xlwt

CS = ['算法导论','软件工程','操作系统','计算机网络',
            '编译原理','数据库系统','计算机图形学','计算机视觉',
            '嵌入式系统','汇编语言']
EE = ['量子力学','模拟电子技术','电路','电磁场与电磁波',
            '射频电路基础','微机原理与系统设计','自动控制技术','通信原理']
MATH = ['高等数学','线性代数','离散数学','概率论','复变函数',
             '数学建模','MATLAB']
c_idpre = ['CS','EE','MATH']
# c_id_temp用来选一个c_idpre
c_id_temp = ''
#  按jc顺序定义
c_id = ''
c_id_data = []
cname = ''
period = ''
credit = ''
teacher = ''
#用来存放   一个Cname 对应多个C#
jc_test = {}
f = Faker(locale='zh_cn')
ws = xlwt.Workbook()
shet = ws.add_sheet(u'abc')
path = r"D:\jc.xls"
n = 0
num_temp = 0
count = 2
while n <= 100:
    n += 1
    c_id_temp = ''.join(random.choice(c_idpre))
    num_temp = f.pyint(min_value=4, max_value=100, step=1)
    if num_temp <10:
        c_id = c_id_temp + '-' + '0' + str(num_temp)
    else:
        c_id = c_id_temp + '-' + str(num_temp)
    while c_id  in jc_test.keys():
        num_temp = f.pyint(min_value=4, max_value=100, step=1)
        if num_temp < 10:
            c_id = c_id_temp + '-' + '0' + str(num_temp)
        else:
            c_id = c_id_temp + '-' + str(num_temp)
    jc_test[c_id] = ' '
    if (c_id_temp == 'CS'):
        cname = ''.join(random.choice(CS))
    elif (c_id_temp == 'EE'):
        cname = ''.join(random.choice(EE))
    else:
        cname = ''.join(random.choice(MATH))
    for key in jc_test.keys():
        if(jc_test[key] == cname):
            cname = cname + str(count)
            count += 1
    jc_test[c_id] = cname
    c_id_data.append(c_id)
    period = str(f.pyint(min_value=30, max_value=100, step=4))
    credit = str(f.pyint(min_value=1, max_value=6, step=1))
    teacher = f.name()
    shet.write(n, 0, c_id)  # 第一个参数表示行，第二个表示列,第三个自己需要的数据
    shet.write(n, 1, cname)
    shet.write(n, 2, period)
    shet.write(n, 3, credit)
    shet.write(n, 4, teacher)
    ws.save(path)

