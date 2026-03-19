import cmath
import math
print('已知一个方程"ax^2+bx+c=0",其中')
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
delta=b**2-4*a*c
if delta>0:
    print('该方程的解为\nx1='+str((-b+math.sqrt(delta))/(2*a))+'\nx2='+str((-b-math.sqrt(delta))/(2*a)))
elif delta==0:
    print('该方程有两个相等的实数根 x1=x2='+str((-b)/(2*a)))
else:
    print('该方程的解为\nx1='+str((-b+cmath.sqrt(delta))/(2*a))+'\nx2='+str((-b-cmath.sqrt(delta))/(2*a)))