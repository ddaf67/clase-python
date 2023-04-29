genero = input("ingrese su género (M/F): ")
edad = int(input("ingrese su edad: "))

if genero == "M" and edad >= 17:
    print("puede participar con la edad de",edad,"en esta fiesta")
else:
    print("no puede participar con la edad de",edad,"en esta fiesta")
