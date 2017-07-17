import random

DIC={
    'piedra':{
        'papel':'papel' ,'tijera':'tijera','piedra':'empate'},
    'papel':{
        'piedra':'piedra','tijera':'tijera','papel':'empate'},
    'tijera':{
        'piedra':'piedra','papel':'papel','tijera':'empate'}}

if __name__ == '__main__':
    count = 0
    vic_user = 0
    vic_maq = 0
    nombre = input("Ingrese tu nombre ==> ")

while count < 5:
    
    if vic_maq == 3  or vic_user == 3 :
        print()
        print(nombre+":"+str(vic_user)+"-----"+"Maquina:"+str(vic_maq))
        break
    
    else:
        print()
        print(nombre+":"+str(vic_user)+"-----"+"Maquina:"+str(vic_maq))
        Decision = input(nombre+": Eliges entre piedra, papel o tijera ==>")
        maquina = random.choice(list(DIC[Decision].keys()))
        print('Usuario Maquina: '+ maquina)
    
        if Decision == 'papel':
            if maquina == 'tijera':
                print('la Maquina ha ganado esta ronda')
                vic_maq=vic_maq+1
                
            elif maquina == 'piedra':
                print('Has ganado esta ronda')
                vic_user = vic_user+1
            elif maquina == 'papel':
                print('EMPATE')
                count = count-1
            
            
        elif Decision == 'piedra':
            if maquina == 'tijera':
                print('Has ganado esta ronda')
                vic_user = vic_user+1
            elif maquina == 'piedra':
                print('Empate')
                count = count-1
            elif maquina == 'papel':
                print('La maquina ha ganado esta ronda')
                vic_maq=vic_maq+1
            
            
        elif Decision == 'tijera':
            if maquina == 'tijera':
                print('EMPATE')
                count = count-1
            elif maquina == 'piedra':
                print('La maquina ha ganado esta ronda')
                vic_maq = vic_maq+1
            elif maquina == 'papel':
                print('Has ganado esta ronda')
                vic_user = vic_user+1
        count = count + 1
        



if vic_maq == 3:
    print('LA MAQUINA HA GANADO :( ')
elif vic_user == 3:
    print('FELICIDADES HAS GANADO :)')