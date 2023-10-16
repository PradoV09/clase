class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.monedas = 0
        self.vidas = 3
        self.tamano = "pequeño"
        self.mundo = 1
        self.nivel = 1

    def recoger_moneda(self):
        self.monedas += 1
        if self.monedas >= 100:
            self.monedas -= 100
            self.vidas += 1

    def recoger_hongo_vida(self):
        self.vidas += 1

    def recoger_hongo_crecimiento(self):
        if self.tamano == "pequeño":
            self.tamano = "grande"

    def recoger_flor_fuego(self):
        if self.tamano == "grande":
            # Poder de disparar
            pass

    def enfrentar_incidente(self, tipo):
        if tipo == "sencillo":
            if self.tamano == "grande":
                self.tamano = "pequeño"
            else:
                self.vidas -= 1
        elif tipo == "grave":
            if self.tamano == "grande":
                self.tamano = "pequeño"
            else:
                self.vidas -= 1

    def cambiar_mundo(self):
        self.mundo += 1
        if self.mundo > 8:
            self.mundo = 1
        self.nivel = 1

    def cambiar_nivel(self):
        self.nivel += 1
        if self.nivel > 4:
            self.nivel = 1

    def reiniciar(self):
        self.monedas = 0
        self.vidas = 3
        self.tamano = "pequeño"
        self.mundo = 1
        self.nivel = 1


# Ejemplo de uso
mario = Personaje("Mario")
print(f"{mario.nombre} - Monedas: {mario.monedas}, Vidas: {mario.vidas}, Tamaño: {mario.tamano}, Mundo: {mario.mundo}, Nivel: {mario.nivel}")

mario.recoger_moneda()
print(f"{mario.nombre} - Monedas: {mario.monedas}, Vidas: {mario.vidas}, Tamaño: {mario.tamano}, Mundo: {mario.mundo}, Nivel: {mario.nivel}")

mario.recoger_hongo_vida()
print(f"{mario.nombre} - Monedas: {mario.monedas}, Vidas: {mario.vidas}, Tamaño: {mario.tamano}, Mundo: {mario.mundo}, Nivel: {mario.nivel}")

mario.enfrentar_incidente("sencillo")
print(f"{mario.nombre} - Monedas: {mario.monedas}, Vidas: {mario.vidas}, Tamaño: {mario.tamano}, Mundo: {mario.mundo}, Nivel: {mario.nivel}")

mario.cambiar_mundo()
print(f"{mario.nombre} - Monedas: {mario.monedas}, Vidas: {mario.vidas}, Tamaño: {mario.tamano}, Mundo: {mario.mundo}, Nivel: {mario.nivel}")

mario.cambiar_nivel()
print(f"{mario.nombre} - Monedas: {mario.monedas}, Vidas: {mario.vidas}, Tamaño: {mario.tamano}, Mundo: {mario.mundo}, Nivel: {mario.nivel}")

mario.reiniciar()
print(f"{mario.nombre} - Monedas: {mario.monedas}, Vidas: {mario.vidas}, Tamaño: {mario.tamano}, Mundo: {mario.mundo}, Nivel: {mario.nivel}")
