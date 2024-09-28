number_input = input("Ingresa un numero: ")
if number_input.isnumeric():
    number = int(number_input)
    if number%2 == 0:
        print(f"El numero {number} es par")
    else:
        print(f"El numero {number} es impar")
else:
    print("El valor ingresado es invalido, debe ser un numero.")