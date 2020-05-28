sum=0
for i in range(0,101,2):    #range(lb,ub,step_size) and[lb,ub)
    sum=sum+i
print (sum)


#输入两个正整数，计算最大公约数和最小公倍数

x=int(input('x='))
y=int(input('y='))

if x>y:
    (x,y)=(y,x)
for i in range(y,0,-1):
    if x%i==0 and y%i==0:
        print('%{} 和 %{} 的最大公约数是:%{}'.format(x,y,i))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // i))
        break


row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        #print('now the _ is %{}'.format(_))
        print('*', end='')    # end='' is used not to jump to the next line
    print()