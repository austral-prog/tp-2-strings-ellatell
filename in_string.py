def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    pass 
    nombre = input ("Ingrese un nombre: ")
    nombre = nombre.lower()
    print ("El nombre contiene a: ", nombre.find("a"))
    print("El nombre contiene e: ", nombre.find("e"))
    print("El nombre contiene i: ", nombre.find("i"))
    print("El nombre contiene o: ", nombre.find("o"))
    print("El nombre contiene u: ", nombre.find("u"))

