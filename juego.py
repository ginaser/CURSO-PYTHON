import random

opciones = {
'piedra':{
'papel':{
'tijera': True;
}
'papel': {
'piedra': True;
'tijera': false;
}
'tijera':{
'Piedra': false;
'papel' = True;
}
}

aleatorio = random.randrange(0, 3)
elijePc = ""
print("1)Piedra")
print("2)Papel")
print("3)Tijera")
opcion = int(input("Que elijes: "))

if opcion == 1:
    elijeUsuario = "piedra"
elif opcion == 2:
    elijeUsuario = "papel"
elif opcion == 3:
    elijeUsuario = "tijera"
print("Tu elijes: ", elijeUsuario)

if aleatorio == 0:
    elijePc = "piedra"
elif aleatorio == 1:
    elijePc = "papel"
elif aleatorio == 2:
    elijePc = "tijera"
print("PC elijio: ", elijePc)
print("...")

