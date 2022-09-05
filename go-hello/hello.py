import sys
import math
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def q3(num):
    if num < 0:
        return -((-num)**(1/3))
    else:
        return num**(1/3)
    
if len(sys.argv) != 5:
    print("Specify four numbers")
    quit()
a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
d = sys.argv[4]
if not(isfloat(a) and isfloat(b) and isfloat(c) and isfloat(d)):
    print("Specify  four numbers")
    quit()

af = float(a)
bf = float(b)
cf = float(c)
df = float(d)
p=((3*af*cf) - bf*bf)/(3*af*af)
q= (2*bf**3-9*af*bf*cf+27*af*af*df)/(27*af**3)
Q=(p/3)**3+(q/2)**2
print(p,q)
print("Q=",Q)
if  Q >= 0:
 alpha =q3(-q/2+math.sqrt(Q))
 betta = q3(-q/2-math.sqrt(Q))
 print(alpha,betta)
 y=alpha+betta
 x=y-(bf/(3*af))

if Q<0:
 alpha=(-(q/2)+Q**(1/2))**(1/3)
 betta=(-(q/2)-Q**(1/2))**(1/3)
 print(alpha,betta)
 y=alpha+betta
 x=y-(bf/(3*af))
 print("x1=",x)   
 #print("y2=",-(alpha+betta)/2, "+ i*", (alpha-betta)/2*math.sqrt(3))
print("There are one real solution and two complex solutions")
quit()
print("Other case")