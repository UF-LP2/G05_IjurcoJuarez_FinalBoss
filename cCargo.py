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
            raise Exception
        # todo excepcion calidad no existe
        peso_real = peso_tot - peso_crew - peso_cargo
        if peso_real > 20:
            return peso_real
         # y si pongo un un print diciendo q se puede saquear?
        else:
            raise Exception

    def __del__(self, cargo, quality, draft, crew):
        print("Destructor called")

