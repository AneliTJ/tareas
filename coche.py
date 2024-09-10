class Coche:
    marca = ""
    modelo = ""
    año = 0

    def __init__(self, marca, modelo, año):
        self.marca = marca 
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        print("marca",self.marca)
        print("modelo",self.modelo)
        print("año",self.año)
