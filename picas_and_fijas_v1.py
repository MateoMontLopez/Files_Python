import random as rand

fijas = 0
picas = 0
ronda = 1
cont = 0
game = True

print("Desea jugar Picas y Fijas? y/n:")
rta = input()

while rta == "y":
    # Generar una lista con números del 1 al 10
    numeros = list(range(0,9))

    # Mezclar la lista de números de forma aleatoria
    rand.shuffle(numeros)

    # Tomar los primeros cuatro números de la lista mezclada
    numbers = numeros[:4]

    print(numbers)

    while game == True:
        print("\n Ronda ",ronda,end="\n\n")
        num1 = int(input("Digite un numero entre 0 a 9: "))
        num2 = int(input("Digite un numero entre 0 a 9: "))
        num3 = int(input("Digite un numero entre 0 a 9: "))
        num4 = int(input("Digite un numero entre 0 a 9: "))

        if num1 == numbers[0]:
            fijas = fijas+1
            cont = cont+1
        else:
            if num1 in numbers:                    
                picas = picas+1
            
        if num2 == numbers[1]:
            fijas = fijas+1
            cont = cont+1
        else:
            if num2 in numbers:
                picas = picas+1
            
        if num3 == numbers[2]:
            fijas = fijas+1
            cont = cont+1
        else:
            if num3 in numbers:
                picas = picas+1
            
        if num4 == numbers[3]:
            fijas = fijas+1
            cont = cont+1
        else:
            if num4 in numbers:
                picas = picas+1
                    
        print("Hay ",fijas," Fijas")
        print("Hay ",picas," Picas")

        if cont == 4:
            game = False

        fijas = 0
        picas = 0
        
        ronda = ronda+1
    
    if cont == 4:
        cont = 0

    print("El numero oculto es: ",numbers)
    print("Felicidades has adivinado el numero")    
    print("Desea jugar de nuevo? y/n:")
    rta = input()
    game = True
    ronda = 0
