import cShip


class Cruise(cShip):
    def __init__(self, passengers, draft, crew):
        super().__init__(draft, crew)
        # super para heredar del padre
        self.passengers = passengers

    def is_worth_it(self):
        peso_botin = self.draft - self.crew * 1.5 - self.passengers * 1.25
        if peso_botin > 20:
            print("el barco merece ser saqueado.")
        elif peso_botin < 0:
            raise ValueError("hay un error en los datos")
        else:
            raise ValueError("no se puede saquear")
