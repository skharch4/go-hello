def solve(a,b,c,d):
    Q = (3*a*c - (b**2)) / (9*(a**2))
    R = (9*a*b*c - 27*(a**2)*d - 2*(b**3)) / (54*(a**3))
    D = (Q**3) + (R**2)
    S = (R + (D**(1/2)))**(1/3)
    T = (R - (D**(1/2)))**(1/3)

    x1 = S + T - (b/(3*a))
    x2 = -((S + T)/2) - (b/(3*a)) + 0.5j * (3**(1/2)) * (S - T)
    x3 = -((S + T)/2) - (b/(3*a)) - 0.5j * (3**(1/2)) * (S - T)
    return (x1,x2,x3)   
    print("Hello")
    def verify(a,b,c,d,x):
    return (a*(x**3) + b*(x**2) + c*x + d)


roots = solve(a,b,c,d)

for x in roots:
    print(verify(a,b,c,d,x))