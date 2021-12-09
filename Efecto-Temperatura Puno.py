
import numpy as np 
import sympy as sym 
import matplotlib.pyplot as plt 


xi = np.array([    0,     1,     2,     3,     4,     5,     6,     7,     8,     9,     10,    11,    12]) 
fi = np.array([9.383, 9.216, 9.509, 9.392, 0.385, 9.654, 9.529, 9.785, 9.406, 9.764, 10.539, 9.779, 0.397]) 




titulo = ['i   ','xi  ','fi  '] 
n = len(xi)
ki = np.arange(0,n,1)
tabla = np.concatenate(([ki],[xi],[fi]),axis=0)
tabla = np.transpose(tabla)


dfinita = np.zeros(shape=(n,n),dtype=float)
tabla = np.concatenate((tabla,dfinita), axis=1)


[n,m] = np.shape(tabla)
diagonal = n-1
j = 3
while (j < m):
   
    titulo.append('F['+str(j-2)+']')

    
    i = 0
    paso = j-2 
    while (i < diagonal):
        denominador = (xi[i+paso]-xi[i])
        numerador = tabla[i+1,j-1]-tabla[i,j-1]
        tabla[i,j] = numerador/denominador
        i = i+1
    diagonal = diagonal - 1
    j = j+1


dDividida = tabla[0,3:]
n = len(dfinita)

x = sym.Symbol('x')
polinomio = fi[0]
for j in range(1,n,1):
    factor = dDividida[j-1]
    termino = 1
    for k in range(0,j,1):
        termino = termino*(x-xi[k])
    polinomio = polinomio + termino*factor


polisimple = polinomio.expand()


px = sym.lambdify(x,polisimple)


muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a,b,muestras)
pfi = px(pxi)

# EVALUACIÓN EN x = 2.8
#def f(x):
#    return -0.654761904761907*x**3 - 3.76785714285713*x**2 + 38.9404761904761*x - 49.5714285714285

#yy=f(2.8)

# CÁLCULO DEL ERROR
#error=0.6548*(2.8-2)*(2.8-2.5)*(2.8-3.2)*(2.8-4)

# SALIDA
np.set_printoptions(precision = 4)
print('Tabla Diferencia Dividida')
print([titulo])
print(tabla)
print('dDividida: ')
print(dDividida)
print('polinomio: ')
print(polinomio)
print('polinomio simplificado: ' )
print(polisimple)
#print('Para x=2.8, se tiene f(2.8)= {0:.2f}'.format(yy))
#print('Para x=2.8, el error es: {0:.2f}'.format(error))

# Gráfica
plt.plot(xi,fi,'o', label = 'Puntos')
##for i in range(0,n,1):
##    plt.axvline(xi[i],ls='--', color='yellow')
plt.plot(pxi,pfi, label = 'Polinomio')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Diferencias Divididas - Newton')
plt.show()