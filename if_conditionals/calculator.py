print("""
1. Suma
2. Resta
3. Multiplicación
4. División
5. Potencia
6. Módulo
7. Comparar
8. Valor absoluto
""")
selection = input("Ingrese el numero correspondiente a la operacion matematica que desea realizar: ")
if selection.isnumeric():
    if int(selection) in range(1,9):
        a = input("ingrese un numero: ")
        if a.isnumeric():
            if int(selection) == 8:
                if int(a) >= 0:
                    abs = int(a)
                else:
                    abs = int(a)*-1
                print(f"El valor absoluto de {a} es {abs}.")
            else:
                b = input("ingrese otro numero: ")
                if b.isnumeric():
                    if int(selection) == 1:
                        c = int(a)+int(b)
                        print(f"{a}+{b}={c}")
                    elif int(selection) == 2:
                        c = int(a)-int(b)
                        print(f"{a}-{b}={c}")
                    elif int(selection) == 3:
                        c = int(a)*int(b)
                        print(f"{a}*{b}={c}")
                    elif int(selection) == 4:
                        c = int(a)/int(b)
                        print(f"{a}/{b}={c}")
                    elif int(selection) == 5:
                        c = int(a)**int(b)
                        print(f"{a}^{b}={c}")
                    elif int(selection) == 6:
                        c = int(a)%int(b)
                        print(f"El modulo de {a}/{b} es {c}")
                    elif int(selection) == 7:
                        if int(a) > int(b):
                            print(f"{a} es mayor que {b}")
                        elif int(a) < int(b):
                            print(f"{a} es menor que {b}")
                        else:
                            print("Ambos numeros son iguales")
        else:
            print("El valor ingresado no es un numero")
    else:
        print("Esta opcion no existe")          


else:
    print("El valor ingresado es invalido")