print(" ")
print("Ordonez Martinez Valeria 1203 3W")
print(" ")

archivo = open("demofile.txt", "w")
archivo.write("El contenido se ha eliminado")
archivo.close()

archivo= open("demofile.txt" , "r")
print(archivo.read())