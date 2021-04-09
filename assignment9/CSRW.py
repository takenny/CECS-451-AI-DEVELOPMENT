import numpy as np


# Probability functions
def prob_c():
    return .5


def prob_c(c: int) -> int:
    return 1 if c < .5 else 0


def prob_r(r, c):
    if c:
        return .8 if r else .2
    else:
        return .2 if r else .8


def prob_s(s, c):
    if c:
        return .1 if s else .9
    else:
        return .5


def prob_w(w, s, r):
    if s and r:
        return .99 if w else .10
    if s and not r:
        return .95 if w else .05
    if not s and r:
        return .90 if w else .1
    if not s and not r:
        return .05 if w else .95


class CSRW:

    def __init__(self, args):

        self.__static__= []
        self.__csrw_dict__ = {}

        for i in range(len(args)):
            if args[i] is not None:
                self.__static__.append(i)
            self.__csrw_dict__[i] = args[i]

        self.__states__ = self.__gen_states__()

    def __gen_states__(self):
        states = []
        for i in range(16):
            temp = str(bin(i))[2:]
            if len(temp) < 4:
                temp = '0' * (4 - len(temp)) + temp
            if self.__check_state_valid__(temp):
                states.append(temp)
        return states

    def __check_state_valid__(self, state):
        print(state)
        for index in self.__static__:
            if bool(int(state[index])) != self.__csrw_dict__[index]:
                return False
        return True

    def get_static(self):
        return self.__static__

    def get_states(self):
        return self.__states__

    def __get_first_state__(self):
        state = ""
        flip = np.random.rand()




if __name__ =="__main__":
    test = CSRW([None, True, None, True])
    print(test.get_static())
    print(test.get_states())
    print(prob_w(w=False, s=False, r=True))
