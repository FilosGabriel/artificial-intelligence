from State import *
from random import randint


class Engine():
    def __init__(self, stare: State):
        self.stare = stare
        self.capacitate_barca = stare.capacitate_barca
        self.canibali = stare.s_canibali
        self.misionari = stare.s_misionari

    # def generate_next(self) -> (int, int):
    #     return 0, 0


class RandomEngine(Engine):
    def __init__(self, stare,  nr_max_tranziti=100):
        super().__init__(stare)
        self.nr_max_tranziti = nr_max_tranziti

    def generate_next(self):
        m, c = 1, 1
        c = randint(-self.capacitate_barca, self.capacitate_barca)
        m = randint(-self.capacitate_barca, self.capacitate_barca)
        return m, c


class BacktrackingEngine(Engine):
    def __init__(self, stare: State):
        super().__init__(stare)
        self.reg = []
        self.h = History()
        self.run = True

    def generate_next2(self):
        a, b = self.change()
        m = a
        c = a
        while not is_final(self.stare) and self.run:

            while m <= b:
                if is_final(self.stare):
                    return True

                while c <= b:
                    if is_final(self.stare):
                        return True
                    if self.stare.is_valid_transition(m, c) and not self.h.exist(transition_to(self.stare, m, c)):
                        self.stare = transition_to(self.stare, m, c)
                        if is_final(self.stare):
                            return True
                        else:
                            self.h.append2(self.stare, m, c)
                            self.reg.append((m, c))
                            a, b = self.change()
                            m, c = a, a
                            CCC = 1
                    c += 1

                m += 1
                c = a
            CCC = 1
            if is_final(self.stare):
                return True
            # m, c = self.revert()
            if self.reg.__len__() == 0:
                return False
            m, c = self.reg.pop()
            self.h.hh.pop()
            self.stare = transition_to(
                self.stare, moved_canibals=-c, moved_misionars=-m)
            CCC = 2
            a, b = self.change()

            CCC = 1
            if c >= b:
                c = a
                m += 1
            else:
                c += 1
        print(self.stare)

    def revert(self):

        m, c = self.reg.pop()
        self.h.hh.pop()
        self.stare = transition_to(
            self.stare, moved_canibals=-c, moved_misionars=-m)
        return m, c

    def change(self):
        if self.stare.poz_barca == 1:
            return 0, self.stare.capacitate_barca
        else:
            return -self.stare.capacitate_barca, 0

    def getSolution(self):
        tmp = []
        for a, b in self.reg:
            tmp.append((-a, -b))
            # print(a)
        return tmp

    def solve(self):
        self.generate_next2()
        tmp = self.getSolution()
        if tmp.__len__() > 0:
            print("Solved")
            print(tmp)
        else:
            print("Solution dont found")
