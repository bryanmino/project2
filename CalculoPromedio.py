nota1 = int(input("Ingrese la Nota 1 "))
nota2 = int(input("Ingrese la Nota 2 "))
nota3 = int(input("Ingrese la Nota 3 "))
promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 7:
    print("Aprobado")
else:
    print("Reprobado")