print("Introduccion a clases")
class Animal:
    edad=3
    raza="Chihuas"
    comida="croquetas"
    def come(self):
        print("El perro come " +self.comida)
print(Animal)
print("creando el objeto de la clase animal")
perro=Animal()
print(f"Edad del perro {perro.edad}")
print(f"Raza del perro {perro.raza}")
perro.come()