print(" ")
print("Ordonez Martinez Valeria 1203 3W")
print(" ")

archivo = open("demofile.txt", "a")
archivo.write("Ahora elarchivo tiene mayor contenido")
archivo.close()


archivo = open("demofile.txt", "r")
print(archivo.read())
archivo.close()



