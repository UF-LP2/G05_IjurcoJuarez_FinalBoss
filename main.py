import csv
from cShip import Ship
# para que me deje crear un barco del tipo ship
from cCargo import Cargo
from cCruise import Cruise

def main():
    listaships = []
    with open("ships.csv") as barcos:
        lector = csv.reader(barcos)
        header = next(lector)

    for row in lector:
        if row[3] == " " and row[2] == " ":
            # me fijo q no haya nada en el ultimo ni anteultimo porque tiene solo 2 carac
            barco = Ship(row[0], row[1])
            listaships.append(barco)
        elif row[3] == " " and row[2] != " ":
            # me fijo que el ultimo este vacio pero el anteultimo no tiene 3 carac
            crucero = Cruise(row[0], row[1], row[2])
            listaships.append(crucero)
        elif row[3] != " " and row[2] != " ":
            # si tiene escritos todos los casilleros es un cargo
            cargo = Cargo(row[0], row[1],  row[2], row[3])
            listaships.append(cargo)
        else:
            print("el barco ingresado no existe")

    for i in range(len(listaships)):
        print("%d" % (i+1))
        try:
            barco_aux = listaships[i]
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    main()

