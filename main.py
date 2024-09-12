from circulo import Circulo

circulo = Circulo ()

circulo_uno = Circulo(4)
circulo_dos = Circulo(8)
circulo_tres = Circulo(12)

radio_uno= circulo_uno.radio 
area_uno = circulo_uno.calcular_area(),
perimetro_uno = circulo_uno.calcular_perimetro()

radio_dos = circulo_dos.radio 
area_dos = circulo_dos.calcular_area(),
perimetro_dos = circulo_dos.calcular_perimetro()

radio_tres = circulo_tres.radio 
area_tres = circulo_tres.calcular_area(),
perimetro_tres = circulo_tres.calcular_perimetro()

print(radio_uno, area_uno, perimetro_uno)
print(radio_dos, area_dos, perimetro_dos)
print(radio_tres, area_tres, perimetro_tres)
