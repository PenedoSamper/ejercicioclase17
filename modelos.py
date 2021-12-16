class modelos:
    def __init__(self, archivo):
        a = open(archivo)
        self.fabricantes = {}
        for linea in a:
            modelo, fabricante = linea.strip().split(" ")
            if fabricante in self.fabricantes:
                self.fabricantes[fabricante].append(modelo)
            else:
                 self.fabricantes[fabricante] = []
                 self.fabricantes[fabricante].append(modelo)