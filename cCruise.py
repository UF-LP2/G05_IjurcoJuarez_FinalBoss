import cShip


class Cruise(cShip):
    def __init__(self, passengers, draft, crew):
        super().__init__(draft, crew)
        # super para heredar del padre
        self.passengers = passengers

    def __del__(self, passengers, draft, crew):
        print("Destructor called")

