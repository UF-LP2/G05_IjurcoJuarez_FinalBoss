class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        peso_tot = self.draft
        peso_crew = self.crew * 1.5
        peso_botin = peso_tot - peso_crew
        if peso_botin > 20:
            print("el barco merece ser saqueado.")
        elif peso_botin < 0:
            raise ValueError("hay un error en los datos")
        else:
            raise ValueError("no se puede saquear")

# todo crear excepcion (try)

    def __del__(self, draft, crew):
        print("Destructor called")
