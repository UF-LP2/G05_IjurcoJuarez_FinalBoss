class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        peso_tot = self.draft
        peso_crew = self.crew * 1.5
        peso_real = peso_tot - peso_crew
        if peso_real > 20:
            return peso_real
        else:
            raise Exception
# todo hacer el metodo pa las hijas
# todo crear excepcion (try)

    def __del__(self, draft, crew):
        print("Destructor called")
