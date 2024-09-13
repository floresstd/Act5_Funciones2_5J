print("Funciones v2")
print("Flores Rodríguez Jesus Daniel")

# Lista
celulares = ["Samsung a52",  "Iphone 11", "Chafa"]
def verlista(telefonos):
    for uncelular in telefonos:
        print(uncelular)
print("Imprime celulares")
verlista(celulares)

# Tupla
ciudades = ("Madrid", "Ciudad de México", "Buenos Aires")
def ver_tupla(lugares):
    for ciudad in lugares:
        print(ciudad)
print("Imprime ciudades de la tupla")
ver_tupla(ciudades)

# Set
frutas = {"Manzana", "Banana", "Mango"}
def ver_set(comidas):
    for fruta in comidas:
        print(fruta)
print("Imprime frutas del set")
ver_set(frutas)

# Diccionario
paises = {"España": "Madrid", "México": "Ciudad de México", "Argentina": "Buenos Aires"}
def ver_diccionario(naciones):
    for pais, capital in naciones.items():
        print(f"País: {pais}, Capital: {capital}")
print("Imprime países y sus capitales del diccionario")
ver_diccionario(paises)

