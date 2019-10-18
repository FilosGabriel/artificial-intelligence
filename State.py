
class State():
    def __init__(self, capacitate_barca: int, misionari: int, canibali: int):
        if misionari < canibali:
            raise Exception("misionari<canibali")
        self.capacitate_barca = capacitate_barca
        self.s_misionari = misionari
        self.d_misionari = 0
        self.s_canibali = canibali
        self.d_canibali = 0
        self.poz_barca = 1

    def is_valid_transition(self, moved_misionars, moved_canibals) -> bool:

        if self.s_misionari > 0 and self.s_misionari < self.s_canibali:
            return False
        if self.d_misionari > 0 and self.d_misionari < self.d_canibali:
            return False

        if abs(moved_canibals+moved_misionars) > self.capacitate_barca:
            return False

        if self.s_misionari-moved_misionars < 0 or self.d_misionari+moved_misionars < 0:
            return False
        if self.s_canibali-moved_canibals < 0 or self.d_canibali+moved_canibals < 0:
            return False

        if (self.s_canibali-moved_canibals > self.s_misionari-moved_misionars and self.s_misionari-moved_misionars > 0) or (self.d_canibali + moved_canibals > self.d_misionari+moved_misionars and self.d_misionari+moved_misionars > 0):
            return False

        if abs(moved_canibals+moved_misionars) > self.capacitate_barca:
            return False
        sum_ = moved_canibals+moved_misionars

        if sum_ > 0 and moved_misionars >= 0 and moved_canibals >= 0 and self.poz_barca == 1:
            return True

        if sum_ < 0 and moved_misionars <= 0 and moved_canibals <= 0 and self.poz_barca == 2:
            return True

        return False


class History():
    def __init__(self):
        self.history = []
        self.hh = [((4, 4, 1, 0, 0), 0, 0)]

    def append(self, state: State):
        self.history.append(state)

    def append2(self, state: State, m, c):
        a = (state.s_misionari, state.s_canibali,
             state.poz_barca, state.d_misionari, state.d_canibali)
        self.history.append(a)
        self.hh.append((a, m, c))

    def exist(self, state: State):
        a = (state.s_misionari, state.s_canibali,
             state.poz_barca, state.d_misionari, state.d_canibali)
        return a in self.history

    def state_was_used(self, state: State, moved_misionars: int, moved_canibals: int) -> bool:
        a = (state.s_misionari-moved_misionars,
             state.s_canibali-moved_canibals,
             3-state.poz_barca,
             state.d_misionari+moved_misionars, state.d_canibali+moved_canibals)
        return a in self.history

    def limit(self):
        return self.history.__len__() > 100

    # def rem(state)
    def reset(self):
        self.history = []


def is_final(state: State) -> bool:
    return state.s_misionari == 0 and state.s_canibali == 0 and state.poz_barca == 2


def transition_to(state: State, moved_misionars: int, moved_canibals: int) -> State:
    s = State(0, 0, 0)
    s.capacitate_barca = state.capacitate_barca
    s.s_misionari = state.s_misionari - moved_misionars
    s.s_canibali = state.s_canibali - moved_canibals
    s.d_misionari = state.d_misionari + moved_misionars
    s.d_canibali = state.d_canibali + moved_canibals
    s.poz_barca = 3-state.poz_barca
    return s
