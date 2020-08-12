"""
a*x^2+b*x+c=0
delta = b^2-4*a*c
if delta=0, x = 
"""
import math # giua import va noi dung file phai co 2 dau xuong dong


def solve(a, b, c):
    """
    dien code vao day
    """ 
     # import phai dat o dau file
    delta = b**2 - 4 * a * c # giua toan tu 2 ngoi (+ - * / %) va toan hang (a b c...) phai co 1 dau space
    if delta < 0: # dau cach
        print("pt vo nghiem")
        return None
    elif delta == 0:
        x = - b / (2 * a) # o day
        print("x1=x2=", x)
        return x
    else:
        x1 = float(-b + math.sqrt(delta) / (2 * a)) # bug here
        print("x1=", x1)
        x2 = float(-b - math.sqrt(delta) / (2 * a)) # dau space
        print("x2=", x2)
        return (x1, x2) # <- Cai nay nghia la gi? Khog phai, seach 'python tuple', i think it fix the value of x1 and x2

# cai nay phai in ra -1
print(solve(1,2,1))
print(solve(1,2,0))
print(solve(1,3,5))