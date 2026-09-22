import numpy as np

def func(omega):
    return (omega[0]-1)*(omega[1]-1)

def gradient_func(omega):
    return np.array([omega[1]-1,omega[0]-1])

def norm(grad,p):
    sum=0
    for val in grad:
        sum+=abs(val)**p
    return sum**(1/p)

gamma=1
tol=1
omega0=np.array([2,2])


gradn=gradient_func(omega0)
dist_n=norm(gradn,2)
print(dist_n)
omega=omega0

while dist_n>tol:
    gradn=gradient_func(omega)
    omega_old=omega
    omega=omega_old-gamma*gradient_func(omega)
    gradn=gradient_func(omega)
    dist_n=norm(gradn,2)
    print(dist_n)