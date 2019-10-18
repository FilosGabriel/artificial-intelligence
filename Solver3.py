from State import *
history = []


def IDDFS(state: State):
    for depth in range(100):
        if DLS(state, depth, []):
            return True
    return False


def get_state(state: State):
    return(state.s_misionari, state.s_canibali, state.poz_barca, state.d_misionari, state.d_canibali)


def DLS(state: State, depth: int, l: list):
    if is_final(state):
        return True
    if depth <= 0:
        return False
    for m in range(-state.capacitate_barca, state.capacitate_barca+1):
        for c in range(-state.capacitate_barca, state.capacitate_barca+1):

            if state.is_valid_transition(m, c):
                history.append((m, c))

                tmp_state = transition_to(state, m, c)
                if not get_state(tmp_state) in l:
                    ll = l.copy()
                    ll.append(tmp_state)
                    if DLS(tmp_state, depth-1, ll):
                        return True
                    history.pop()
    return False


S = State(2, 3, 3)
print(IDDFS(S))
print(history)
