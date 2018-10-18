def codigo_morse():
    file = open("Morse.txt", "r")
    lista = []
    for a in file:
        lista.append(a.strip("\n").split())
    file.close()
    for a in range(len(lista)):
        codigo[lista[a][0]] = lista[a][1]
        codigo2[lista[a][1]] = lista[a][0]
    codigo[" "] = " "
    codigo2[" "] = " "

def palabra_a_morse():
    palabra = input("Ingresar palabra: ")
    string = ""
    for x in range(len(palabra)):
        for y in range(len(palabra[x])):
            try:
                string = string + codigo.get(palabra[x][y]) + " "
                B = True
            except:
                print(palabra[x], "no es un caracter aceptado")
                string = string + "* "
                if len(palabra) == 1:
                    B = False
    if B:
        print(string)

def morse_a_palabra():
    palabra = input("Ingresar codigo: ").split()
    string = ""
    for x in range(len(palabra)):
        try:
            string = string + codigo2.get(palabra[x]) + " "
            B = True
        except:
            print(palabra[x], "no es un caracter aceptado")
            string = string + "* "
            if len(palabra) == 1:
                B = False
    if B:
        print(string.strip(" "))

codigo = {}
codigo2 = {}
codigo_morse()

#translation
B = True
while B:
    print("Palabra a morse --> 0", "\n" + "Morse a palabra --> 1", "\n" + "Salir --> exit")
    a = input()
    if a == "0":
        palabra_a_morse()
    if a == "1":
        morse_a_palabra()
    if a == "exit":
        break
    else:
        pass
