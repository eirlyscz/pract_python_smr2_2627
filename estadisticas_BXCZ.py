notas = [5.25, 6, 7, 2.25, 8.33, 9, 10]

minimo = min(notas)
maximo = max(notas)
lista = len(notas)

print("Cantidad de notas que hay:", lista)
print("Maximo de las notas:", maximo)
print("Minimo de las notas:", minimo)
print("Nota media:", sum(notas)/len(notas))
print("Hay suspensos?", any(notas)<5)
print("Hay algún cero?:", all(notas)==0)
