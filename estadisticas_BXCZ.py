notas = [2.25, 9, 10, 7, 8.5, 4, 5, 6.5,0]

print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))
print("Nota media:", sum(notas) / len(notas))
print("¿Hay algún suspenso?", any(nota < 5 for nota in notas))
print("¿No hay ningún cero?", all(nota != 0 for nota in notas))