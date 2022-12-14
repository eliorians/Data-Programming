from random import uniform

n = int(input("Enter n: "))
c = 0

a = 0
while (a < n):
    x = uniform(-1, 1)
    y = uniform(-1, 1)

    if ((x **2 + y**2)**(1/2)) < 1:
        c += 1
    
    a += 1

print(f'After {n} trials, the approximation is pi = {4*(c/n):.6f}.')