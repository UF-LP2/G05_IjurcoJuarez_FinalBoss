import cShip


class Cargo(cShip):
    def __init__(self, cargo, quality, draft, crew):
        super().__init__(draft, crew)
        # super para heredar del padre
        self.cargo = cargo
        self.quality = quality

    def __del__(self, cargo, quality, draft, crew):
        print("Destructor called")

