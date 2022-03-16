class Automaton():

    def __init__(self, config_file):
        self.config_file = config_file
        print("Hi, I'm an automaton!")

    def validate(self):
        """Return a Boolean
        Returns true if the config file is valid,
        and raises a ValidationException if the config is invalid.
        """
        return "I can't tell if the config file is valid... yet!"

    def accepts_input(self, input_str):
        """Return a Boolean
        Returns True if the input is accepted,
        and it returns False if the input is rejected.
        """
        pass

    def read_input(self, input_str):

        Alfabet = set()
        Stari = set()
        Tranzitii = []
        Final = set()

        ok = 0

        input_file = open(input_str, "r")
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

            if ok == 1:         #suntem pe alfabet
                Alfabet.add(linie.strip())
            if ok == 2:         #suntem pe stari
                #cazul 1, stari care pot fi finale SI initiale, in acelasi timp
                if len(linie.strip().split(',')) > 2:
                    Stari.add(int(linie.strip().split()[0]))
                    if linie.strip().split(',')[2] == 'F' or linie.strip().split(',')[1] == 'F':
                        Final.add(linie.strip().split(',')[0])
                    if linie.strip().split(',')[2] == 'S' or linie.strip().split(',')[1] == 'S':
                        Initial = linie.strip().split(',')[0]
                #cazul 2, stari care sunt doar finale SAU doar initiale
                elif len(linie.strip().split(',')) == 2:
                    Stari.add(int(linie.strip().split()[0]))
                    if linie.strip().split(',')[1] == 'S':
                        Initial = linie.strip().split(',')[0]
                    if linie.strip().split(',')[1] == 'F':
                        Final.add(linie.strip().split(',')[0])
                #cazul 3, stari care nu sunt nici finale, nici initiale
                else:
                    Stari.add(int(linie.strip()))
            if ok == 3:         #suntem pe tranzitii

                tranzitie = linie.strip().split(", ")
                tranzitie[0] = int(tranzitie[0])
                tranzitie[2] = int(tranzitie[2])
                tranzitie[1] = tranzitie[1][0:1]
                Tranzitii.append(tuple(tranzitie))

        verificare = 1
        print(Stari)
        print(Tranzitii)
        for tranzitie in Tranzitii:
            if tranzitie[0] not in Stari or tranzitie[1] not in Alfabet or tranzitie[2] not in Stari:
                print("INPUT NEVALID!!! NASPA")
                verificare = 0
                return 0
        if verificare == 1:
            print("INPUT VALID!!! BRAVO")
        return 1


if __name__ == "__main__":
    a = Automaton('date.in')
    a.read_input('date.in')
