import modelos
mc = modelos.Modelos("coches.txt")
while true:
    modelo = unidecode.unidecode(input("Modelo:")).lower()
    if modelo == "fin"
        break
    encontrado = False
    for f in mc.fabricantes:
        if modelo in mc.fabricantes[f]:
            prtint("fabricante: ", f)
            encontrado = True
            break
    if encontrado == False:
        print("No existe este modelo")


