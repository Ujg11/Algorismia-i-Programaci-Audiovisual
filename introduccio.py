# Comandos bàsics:

# Altres tipus de comentaris (es crea un objecte i després es destrueix)
'''
dfdv
ffv
dfv
'''

#Operador redondeig
round(2.6) #-> 3
round(2.4) #-> 2
		#Si es X.5 va cap a baix o cap al enter parell més proper

#Operadors
min(4,3)
max(4,3)
sum(5,6)
print(4, "hola")
len("hola")
_ #para recuperar el ultimo resultado
pow(4, 3)
4 ** 3 #També fer la potència

# Operadors:
a += 1
a -= 2
a *= 4
a /= 5

a < b
a > b
a == b
False 
True
4 < 8 and 4 > 2 # True
2 < 4 < 8  # True

# Les funcions retornen sempre alguna cosa, sino igualment retornen "None"
a = print("Hola")
print(a) # Dirà "None" ja que print no retorna res

0 or print("Hola") #Executara el print i retornara False o en aquest cas 0


# Operadors INCLUSIO (in) i IDENTITAT (is)
1 in (1, 2, 3) #--> True
1 not in (1, 2, 3) #--> False

a = 571
b = a
a is b #--> True

a = 571
b = 571
a == b #--> True
a is b #--> False

# Para tener el plot de Matlab:
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear el gráfico
plt.plot(x, y)

# Añadir título y etiquetas
plt.title('Ejemplo de gráfico de línea')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar el gráfico
plt.show()


# Utilitzarem també el numpy
import numpy as np
# N-dimensional array

# Hi ha el linspace (comença desde 0, fins a 10 i té 11 llocs)
np.linspace(0, 10, 11)

arr = np.array([1, 2, 3, 4, 5])
print("Array unidimensional:", arr)

# Crear un array bidimensional
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Array bidimensional:\n", arr_2d)

# Operaciones básicas
suma = np.sum(arr)
print("Suma de los elementos del array:", suma)

media = np.mean(arr)
print("Media de los elementos del array:", media)

# Crear un array de ceros
ceros = np.zeros((3, 3))
print("Array de ceros:\n", ceros)

# Crear un array de unos
unos = np.ones((2, 4))
print("Array de unos:\n", unos)

# FFT:
x = np.linspace(0, 10, 9)
np.fft.fft(x)


# Hi ha més paquets
import scipy as sc

# Ens permet llegir i escriure archius d'audio
import soundfile as sf

import sounddevice as sd

#Ex 1:
import soundfile as sf

x, fm = sf.read('data/luzbel64.wav')

print('fm')
