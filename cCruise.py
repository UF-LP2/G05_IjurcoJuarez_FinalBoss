import cShip


class Cruise(cShip):
    def __init__(self, passengers, draft, crew):
        super().__init__(draft, crew)
        # super para heredar del padre
        self.passengers = passengers

    def is_worth_it(self):
        peso_real = self.draft - self.crew * 1.5 - self.passengers * 1.25
        if peso_real > 20:
            return peso_real
            # y si pongo un un print diciendo q se puede saquear?
        elif peso_real < 0:
            raise Exception
        # todo diferenciar excepciones

        else:
            raise Exception

    def __del__(self, passengers, draft, crew):
        print("Destructor called")

