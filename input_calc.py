def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    pass 
    numero_uno = float(input())
    numero_dos = float(input())
    operacion = input()

    if operacion == "+":
        print(f"Resultado: {numero_uno + numero_dos}")

    elif operacion == "-":
        print(f"Resultado: {numero_uno - numero_dos}")

    elif operacion == "*":
        print(f"Resultado: {numero_uno * numero_dos}")

    elif operacion == "/":
        if numero_dos == 0:
            print("Error: division por cero")
        else:
            print(f"Resultado: {numero_uno / numero_dos}")

    else:
        print("Operacion invalida")
