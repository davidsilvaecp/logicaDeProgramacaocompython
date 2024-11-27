val1 = float(input("digite o 1° valor: "))
val2 = float(input("digite o 2° valor: "))
val3 = float(input("digite o 3° valor: "))

if val1 <= 0 or val2 <= 0 or val3 <= 0: 
    print("não é um triangulo! ")
elif val1 + val2> val3 and val2 + val3 > val1 and val1 + val3 > val2:
    print("não é um triangulo! ")
elif val1 == val2 == val3:
    print("Triangulo Equialátero! ")
elif val1 != val2 != val3 :
    print("Triangulo escaleno! ")
elif val1 == val2 or val1 == val3 or val2 == val3:
    print("triangulo Isósceles! ")

