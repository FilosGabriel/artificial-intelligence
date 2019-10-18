from random import randint
from State import *
from Solvers import *


def solver(stare: State, engine: Engine):
    h = History()
    while not is_final(stare):
        m, c = engine.generate_next()
        if h.limit():
            h.reset()
            stare = State(engine.capacitate_barca,
                          engine.misionari, engine.canibali)
        if stare.is_valid_transition(moved_misionars=m, moved_canibals=c):
            # print(m, c, stare.poz_barca)
            # print("------------------------->"+str(stare.transitions)+"\n")
            stare = transition_to(stare, moved_canibals=c, moved_misionars=m)
            h.append((m, c))
    else:
        print("solved")
        print(stare.d_canibali,stare.d_misionari)
        print(h.history)


S = State(4, 6, 6)
# ba = BacktrackingEngine(S)
# ba.solve()
# print(ba.stare.s_canibali, ba.stare.s_misionari, ba.stare.poz_barca)
engine = RandomEngine(S)
solver(S, engine)
