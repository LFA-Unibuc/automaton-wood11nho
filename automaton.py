class Automaton():

    def __init__(self, config_file):
        self.config_file = config_file
        self.states = []
        self.words = []
        self.transitions = []
        self.final = []
        self.dictionar = {}
        print("Hi, I'm an automaton!")

    def validate(self):

        Tranzitii = []

        ok = 0

        input_file = open(self.config_file)
        text_input = input_file.readlines()
        for linie in text_input:
            if '#' in linie or linie == '\n':
                continue
            if "Sigma" in linie:
                ok = 1
            if "States" in linie:
                continue

            if "Transitions" in linie:
                continue

            if linie.startswith('End'):
                ok = ok + 1
                continue

            if ok == 1:  # suntem pe alfabet
                self.words.append(linie.strip())
            if ok == 2:  # suntem pe stari
                # cazul 1, stari care pot fi finale SI initiale, in acelasi timp
                if len(linie.strip().split(',')) > 2:
                    self.states.append(linie.strip().split()[0])
                    if linie.strip().split(',')[2] == 'F' or linie.strip().split(',')[1] == 'F':
                        self.final.append(linie.strip().split(' ,')[0])
                    if linie.strip().split(',')[2] == 'S' or linie.strip().split(',')[1] == 'S':
                        self.initial = linie.strip().split(' ,')[0]
                # cazul 2, stari care sunt doar finale SAU doar initiale
                elif len(linie.strip().split(',')) == 2:
                    self.states.append(linie.strip().split()[0])
                    if linie.strip().split(',')[1] == 'S':
                        self.initial = linie.strip().split(' ,')[0]
                    if linie.strip().split(',')[1] == 'F':
                        self.final.append(linie.strip().split(' ,')[0])
                # cazul 3, stari care nu sunt nici finale, nici initiale
                else:
                    self.states.append(linie.strip())
            if ok == 3:  # suntem pe tranzitii

                tranzitie = linie.strip().split(", ")
                tranzitie[0] = tranzitie[0]
                tranzitie[2] = tranzitie[2]
                tranzitie[1] = tranzitie[1][0:1]
                self.transitions.append(tuple(tranzitie))

        verificare = 1
        # print(self.transitions)
        # print(Stari)
        # print(Initial)
        # print(Tranzitii)
        # print(Final)
        self.words.remove("Sigma :")
        # print(Alfabet)
        Tranzitii_stari = {}
        # fac un dictionar cu tranzitiile, pt fiecare stare
        for tranzitie in self.transitions:
            if tranzitie[0] not in Tranzitii_stari:
                Tranzitii_stari[tranzitie[0]] = dict()
                Tranzitii_stari[tranzitie[0]][tranzitie[1]] = [tranzitie[2]]
            else:
                if tranzitie[1] in Tranzitii_stari[tranzitie[0]]:
                    Tranzitii_stari[tranzitie[0]][tranzitie[1]].append(tranzitie[2])
                else:
                    Tranzitii_stari[tranzitie[0]][tranzitie[1]] = [tranzitie[2]]
        for stare in self.states:
            if stare not in Tranzitii_stari:
                Tranzitii_stari[stare] = {}
                for cuvant in self.words:
                    Tranzitii_stari[stare][cuvant] = []
        for elem in Tranzitii_stari:
            for cuvant in self.words:
                if cuvant not in Tranzitii_stari[elem]:
                    Tranzitii_stari[elem][cuvant] = []
        # print(Tranzitii_stari)
        self.dictionar = Tranzitii_stari
        # print(self.words)
        # print(self.states)
        # print(self.final)
        # print(self.initial)
        # print(self.dictionar)
        
        for tranzitie in self.transitions:
            if tranzitie[0] not in self.states or tranzitie[1] not in self.words or tranzitie[2] not in self.states:
                print("INPUT NEVALID!!! NASPA")
        if verificare == 1:
            print("In primul rand, este valid inputul?")
            return True

    def accepts_input(self, input_str):
        """Return a Boolean
        Returns True if the input is accepted,
        and it returns False if the input is rejected.
        """
        pass

    def read_input(self, input_str):
        pass



if __name__ == "__main__":
    a = Automaton('date.in')
    print(a.validate())