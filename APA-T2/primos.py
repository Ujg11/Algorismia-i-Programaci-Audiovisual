'''Oriol Jiménez Garrich
Para hacer los test:
import doctest
import primos
doctest.testmod(primos, verbose = True)

esPrimo(numero):
>>> [numero for numero in range(2, 50) if esPrimo(numero)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

primos(numero):
>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

descompon(numero):
>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

mcm(num1, num2):
>>> mcm(90, 14)
630

mcd(num1, num2):
>>> mcd(924, 780)
12

mcmN(numeros):
>>> mcmN(42, 60, 70, 63)
1260

mcdN(numeros):
>>> mcdN(840, 630, 1050, 1470)
210
'''


def esPrimo(numero):
	"""
	Devuelve True si su argumento es primo, y False si no lo es.
	"""
	div = 2
	if numero <= 0:
		return False
	elif numero == 1:
		return True
	elif numero == 2:
		return True
	elif numero % 2 == 0:
		return False
	for div in range(3, numero, 2):
		if numero % div == 0:
			return False
	return True


def primos(numero):
	"""
	Devuelve una tupla con todos los números primos menores que su argumento.
	"""
	results = []
	i = 2

	while i < numero:
		if esPrimo(i):
			results.append(i)
		i += 1
	return tuple(results) 

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    """
    results = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            results.append(divisor)
            numero //= divisor
        divisor += 1
        if divisor * divisor > numero:
            if numero > 1:
                results.append(numero)
            break
    return tuple(results)


def mcm(numero1, numero2):
	"""
	Devuelve el mínimo común múltiplo de sus argumentos.
	"""
	primos_num_1 = descompon(numero1)
	primos_num_2 = descompon(numero2)
	result = 1
	#len = len(primos_num_1) if len(primos_num_1) > len(primos_num_2) else len(primos_num_2)
	len1, len2 = len(primos_num_1), len(primos_num_2)
	i, j = 0, 0
	while i < len1 or j < len2:
		if i >= len1:
			result *= primos_num_2[j]
			j += 1
		elif j >= len2:
			result *= primos_num_1[i]
			i += 1
		elif primos_num_1[i] < primos_num_2[j]:
			result *= primos_num_1[i]
			i += 1
		elif primos_num_1[i] > primos_num_2[j]:
			result *= primos_num_2[j]
			j += 1
		else: # Son iguales
			result *= primos_num_1[i]
			i += 1
			j += 1
	return result


def mcd(numero1, numero2):
	"""
	Devuelve el máximo común divisor
	"""
	primos_num_1 = descompon(numero1)
	primos_num_2 = descompon(numero2)
	result = 1
	len1, len2 = len(primos_num_1), len(primos_num_2)
	i, j = 0, 0
	while i < len1 and j < len2:
		if primos_num_1[i] < primos_num_2[j]:
			i += 1
		elif primos_num_1[i] > primos_num_2[j]:
			j += 1
		else:
			result *= primos_num_1[i]
			i += 1
			j += 1
	return result

#print(mcd(450, 360))

def mcmN(*numeros):
	"""
    Devuelve el mínimo común múltiplo de un número arbitrario de argumentos.
    """
	if len(numeros) == 0: return 1

	result = numeros[0]
	for num in numeros[1:]:
		result = mcm(result, num)
	return result

#print(mcmN(1, 5, 6, 18, 31))
numeros = [1, 5, 6, 18, 30]


def mcdN(*numeros):
	"""
    Devuelve el máximo común divisor de un número arbitrario de argumentos.
    """
	if len(numeros) == 0: return 1

	result = numeros[0]
	for numero in numeros[1:]:
		result = mcd(result, numero)
	return result

#print([numero for numero in range(2, 50) if esPrimo(numero)])
#print(primos(50))
#print(descompon(36 * 175 * 143))
#print(mcm(90, 14))
#print(mcd(924, 780))
#print(mcmN(42, 60, 70, 63))
#print(mcdN(840, 630, 1050, 1470))


#if __name__ == "__main__":
#	import doctest
#	doctest.testmod()



#Tests para esPrimo():
#
#>>> esPrimo(9)
#False
#>>> esPrimo(4)
#False
#>>> esPrimo(13)
#True
#>>> esPrimo(17)
#True
#>>> esPrimo(31)
#True
#
#Tests para primos():
#>>> print(f"Los numeros primos menores que 10 son: {primos(10)}")
#Los numeros primos menores que 10 son: (2, 3, 5, 7)
#>>> print(f"Los numeros primos menores que 20 son: {primos(20)}")
#Los numeros primos menores que 20 son: (2, 3, 5, 7, 11, 13, 17, 19)
#>>> print(f"Los numeros primos menores que 40 son: {primos(40)}")
#Los numeros primos menores que 40 son: (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
#>>> print(f"Los numeros primos menores que 50 son: {primos(50)}")
#Los numeros primos menores que 50 son: (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
#
#Tests para descomposicion():
#>>> print(f"La descomposición en numeros primeros de 10 es: {descompon(10)}")
#La descomposición en numeros primeros de 10 es: (2, 5)
#>>> print(f"La descomposición en numeros primeros de 1447 es: {descompon(1447)}")
#La descomposición en numeros primeros de 1447 es: (1447,)
#>>> print(f"La descomposición en numeros primeros de 89 es: {descompon(89)}")
#La descomposición en numeros primeros de 89 es: (89,)
#
#Tests para mcm():
#>>> mcm(90, 14)
#630
#>>> mcm(2, 11)
#22
#>>> mcm(4, 16)
#16
#>>> mcm(70, 66)
#2310
