print(" ")
print("Ordonez Martinez Valeria 1203 ")
print(" ")
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("Este archivo ya no existe")
  print(" ")