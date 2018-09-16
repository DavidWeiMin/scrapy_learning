import numpy as np
def perm(n,begin,end):
    if begin>=end:
        a.append((n))
    else:
        i=begin
        for num in range(begin,end):
            n[num],n[i]=n[i],n[num]
            perm(n,begin+1,end)
            n[num],n[i]=n[i],n[num]
    return a
 
n = list(range(10))
global a
a = []
perm(n,0,len(n))
print(a)
a = np.array(a)
num1 = a[:][5] * 100000 + a[:][3] * 10000 + a[:][4] * 1000 + a[:][8] * 100 + a[:][6] * 10 +a[:][5]
num2 = a[:][1] * 100000 + a[:][0] * 10000 + a[:][7] * 1000 + a[:][8] * 100 + a[:][6] * 10 +a[:][5]
num3 = a[:][7] * 100000 + a[:][3] * 10000 + a[:][9] * 1000 + a[:][0] * 100 + a[:][7] * 10 +a[:][2]
num4 = num1 + num2
index = np.where(num3==num4)
try:
    print(a[index])
except:
    print('找不到')
