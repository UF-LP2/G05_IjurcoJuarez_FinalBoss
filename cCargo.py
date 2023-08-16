import cShip


class Cargo(cShip):
    def __init__(self, cargo, quality, draft, crew):
        super().__init__(draft, crew)
        # super para heredar del padre
        self.cargo = cargo
        self.quality = quality

    def is_worth_it(self):
        peso_tot = self.draft
        peso_crew = self.crew * 1.5
        if self.quality == 1:
            peso_cargo = self.cargo * 3.5
        elif self.quality == 0.5:
            peso_cargo = self.cargo * 2
        elif self.quality == 0.25:
            peso_cargo = self.cargo * 0.5
        else:
            raise ValueError(" valor de calidad erroneo/no tiene calidad")

        peso_botin = peso_tot - peso_crew - peso_cargo
        if peso_botin > 20:
            print("el barco merece ser saqueado.")
        elif peso_botin < 0:
            raise ValueError("hay un error en los datos")
        else:
            raise ValueError("no se puede saquear")

    def __del__(self, cargo, quality, draft, crew):
        print("Destructor called")

