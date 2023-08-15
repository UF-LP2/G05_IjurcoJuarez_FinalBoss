class Ship:
    def _init_(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        peso_tot = self.draft
        peso_crew = self.crew * 1.5
        peso_real = peso_tot - peso_crew
        if peso_real > 20:
            return peso_real
            # y si pongo un un print diciendo q se puede saquear?
        elif peso_real < 0:
            raise Exception
        # todo diferenciar excepciones
        else:
            raise Exception
# todo hacer el metodo pa las hijas
# todo crear excepcion (try)

    def _del_(self, draft, crew):
        print("Destructor called")