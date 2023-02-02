
'''1-Escribe una función generar_n_caracteres(n, carácter) a la que se le pasa un número
entero n y un carácter. Devolverá el carácter multiplicado por n.
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx". Tantas x como indique el
número.'''

def generar_n_caracteres(n, caracter):
    return n * caracter
print(generar_n_caracteres(5, "x"))

'''2-Crea una función llamada histograma(lista_números) a la que se le pasa una lista de números 
enteros. Se mostrará un histograma cuyas columnas midan el valor de los números.'''

def histograma(lista_numeros):
    for i in lista_numeros:
        print(i * "*")
print(histograma([4, 9, 2, 7]))


'''3-Escribe una función funcionLista(función, lista) que reciba otra función creada 
anteriormente y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada 
uno de los elementos de la lista.
Por ejemplo, la función que se le pasa calcula el cubo de un número. 
La lista que se pasa es una lista de números enteros. A cada número de la lista se le aplica la 
función y se calculará el cubo de todos ellos, mostrándolos en otra lista nueva.
Si la lista que se pasara fuera [1,2,3,4,5] la función devolvería [1,8,27,64,125]'''

'''Funcion calcula el cubo de un número'''

def cubo(numero):
    return numero ** 3
print(cubo(3))

def funcionLista(funcion, lista):
    return [funcion(i) for i in lista]
print(funcionLista(cubo, [1, 2, 3, 4, 5]))


'''4-Escribe una función palabrasLongitud(frase) que reciba una frase y devuelva un diccionario 
con las palabras que contiene y su longitud.
Por ejemplo, la función recibe la frase ‘Hola y adiós’ y devuelve un diccionario de la forma 
{‘Hola’:4, ‘y’:1, ‘adiós’:5}'''

def palabrasLongitud(frase):
    return {palabra: len(palabra) for palabra in frase.split()}
print(palabrasLongitud('Hola y adiós'))


'''5-Escribe una función calificaPalabras(diccionario) que reciba un diccionario con las 
asignaturas y las notas numéricas de un alumno y devuelva otro diccionario con las asignaturas en 
mayúsculas y las calificaciones correspondientes a las notas con palabras.
El criterio será el siguiente: nota <5 → Suspenso; 5 <= nota < 7 → Aprobado; 
7 <= nota < 9 → Notable; 9 <= nota <=10 → Sobresaliente. La nota no puede sobrepasar 10.
Por ejemplo, la función recibe el diccionario {'Android':8.2, 'Hilos':5, 'Python':9.3, 'Interfaces':4.4}
y devuelve el diccionario {'ANDROID’:’Notable’, ‘HILOS’:’Aprobado’, ‘PYTHON’:’Sobresaliente’, 
‘INTERFACES’:’Suspenso’ }'''

def calificaPalabras(diccionario):
    return {asignatura.upper(): 'Suspenso' if nota < 5 else 'Aprobado'if nota < 7 else 'Notable' if nota < 9 else 'Sobresaliente' for asignatura, nota in diccionario.items()}
print(calificaPalabras({'Android':8.2, 'Hilos':5, 'Python':9.3, 'Interfaces':4.4}))








