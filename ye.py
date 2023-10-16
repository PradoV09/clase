import random

class Personaje:
    def __init__(self, nombre, monedas, vidas, tamaño, mundo, nivel, poder_disparo, pasos):
        self.nombre_personaje = nombre
        self.monedas = monedas
        self.vidas = vidas
        self.tamaño = tamaño
        self.mundo = mundo
        self.nivel = nivel
        self.poder_disparo = poder_disparo
        self.pasos = pasos

    def atributos_del_personaje(self):
        print(self.nombre_personaje, ":", sep="")
        print("vidas", self.vidas)
        print("monedas", self.monedas)
        print("tamaño", self.tamaño)
        print("mundo", self.mundo)
        print("nivel", self.nivel)
        print("Poder de disparo:", self.poder_disparo)
        print("Pasos:", self.pasos)

    def cambiar_tamaño(self, hongo):
        if hongo:
            self.tamaño = "grande"
            print(f"{self.nombre_personaje} ha recogido un hongo y ahora está grande.")
        else:
            self.tamaño = "pequeño"
            self.poder_disparo = False

    def recoger_flor(self):
        if self.tamaño == "grande":
            self.poder_disparo = True
            print(f"{self.nombre_personaje} ha recogido una flor y ahora tiene el poder de disparo.")

    def recoger_monedas(self, cantidad):
        self.monedas += cantidad
        vidas_extra = self.monedas // 100
        self.monedas %= 100
        self.vidas += vidas_extra
        print(f"{self.nombre_personaje} ha recogido {cantidad} monedas. Ahora tiene {self.monedas} monedas y {self.vidas} vidas.")

    def recoger_hongo(self):
        if self.tamaño == "pequeño" and random.choice([True, True, False]):
            self.cambiar_tamaño(True)

    def incidente_cencillo(self):
        incidente_sencillo = random.choice([True, False])
        if self.tamaño == "pequeño" or incidente_sencillo:
            self.vidas -= 1
            if self.vidas <= 0:
                print(f"{self.nombre_personaje} ha perdido todas las vidas.")
        else:
            self.cambiar_tamaño(False)
            
    def incidente_grave(self):
        grave = random.choice([True,False])
        if self.tamaño == "grande" or grave:
            self.tamaño = "pequeño"
            print(f"{self.nombre_personaje} ha enfretado un incidente y se ha vuelto pequeño")
        else:
            self.tamaño(False)
            print(f"{self.nombre_personaje} ha muerto")

    def tomar_hongo_vida(self):
        self.vidas += 1
        print(f"{self.nombre_personaje} ha tomado un hongo de vida y ahora tiene {self.vidas} vidas.")

    def reiniciar_personaje(self):
        self.__init__(self.nombre_personaje, 0, 3, "pequeño", 1, 1, False, 0)

    def cambiar_nivel(self):
        if self.nivel < 4:
            self.nivel += 1
        else:
            self.nivel = 1
            if self.mundo < 8:
                self.mundo += 1
            else:
                self.mundo = 1

    def avanzar_pasos(self, pasos):
        self.pasos += pasos
        if self.pasos >= 100:
            self.cambiar_nivel()
            self.pasos -= 100

def mostrar_menu():
    print("Menú del juego:")
    print("1. Ver atributos del personaje")
    print("2. Cambiar tamaño (recoger hongo de crecimiento)")
    print("3. Recoger flor (poder de disparo)")
    print("4. Recoger monedas")
    print("5. Enfrentar incidente grave")
    print("6. Enfrentar incidente cencillo")
    print("7. Tomar hongo de vida")
    print("8. Cambiar de nivel")
    print("9. Reiniciar personaje")
    print("W. Avanzar 10 pasos (Tecla 'w')")
    print("0. Salir")

def crear_personaje(nombre):
    return Personaje(nombre, 0, 3, "pequeño", 1, 1, False, 0)

personaje_elegido = None
while personaje_elegido is None:
    print("Elija un personaje:")
    print("1. Mario")
    print("2. Luigi")
    opcion_personaje = input("Ingrese el número de personaje: ")
    if opcion_personaje == "1":
        personaje_elegido = crear_personaje("Mario")
    elif opcion_personaje == "2":
        personaje_elegido = crear_personaje("Luigi")
    else:
        print("Opción no válida. Por favor, elija un personaje válido.")

while True:
    mostrar_menu()
    opcion = input("Elija una opción (0-9) y w para dar pasos: ")

    if opcion == "0":
        break
    elif opcion == "1":
        personaje_elegido.atributos_del_personaje()
    elif opcion == "2":
        personaje_elegido.cambiar_tamaño(True)
    elif opcion == "3":
        personaje_elegido.recoger_flor()
    elif opcion == "4":
        cantidad_monedas = random.randint(1, 5)  
        personaje_elegido.recoger_monedas(cantidad_monedas)
    elif opcion == "5":
        personaje_elegido.incidente_grave()
    elif opcion == "6":
        personaje_elegido.incidente_cencillo()
    elif opcion == "7":
        personaje_elegido.tomar_hongo_vida()
    elif opcion == "8":
        personaje_elegido.cambiar_nivel()
    elif opcion == "9":
        personaje_elegido.reiniciar_personaje()
    elif opcion == "W" or "w":
        print("Avanzando 10 pasos...")
        personaje_elegido.avanzar_pasos(10)
    else:
        print("Opción no válida. Por favor, elija una opción válida.")