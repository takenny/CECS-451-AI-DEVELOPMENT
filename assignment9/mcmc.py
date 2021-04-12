import numpy as np
import copy

TRANS_MAP = [[0.9321, 0.0069, 0.0610, 0.0000],
             [0.0134, 0.3153, 0.0000, 0.6713],
             [.4390, 0.0000, .4701, .0909],
             [0.0000, .1552, .4091, 0.4357]]

STATES = ["1011", "1001", "0011", "0001"]


class State:

    def __init__(self, state, trans_list):
        self.state = state
        self.counter = 0
        self.__trans_list__ = copy.deepcopy(trans_list)
        self.__ps__ = []
        self.__gen_ps__()

    def __gen_ps__(self):

        for i in range(len(self.__trans_list__)):
            if self.__trans_list__[i] != 0:
                self.__ps__.append(i)
            else:
                remove = self.__trans_list__[i]
        self.__trans_list__.remove(remove)

        self.__trans_list__ = np.cumsum(self.__trans_list__)

    def get_next_state(self):
        num = np.random.rand()
        # print(num, self.__trans_list__, self.__ps__)
        if num > self.__trans_list__[1]:
            return STATES[self.__ps__[2]]
        elif num > self.__trans_list__[0]:
            return STATES[self.__ps__[1]]
        else:
            return STATES[self.__ps__[0]]


def print_a():
    print("Part A: The sampling Probabilities")
    print("P(C|-s,r) = <0.8780, 0.1220>")
    print("P(C|-s,-r) = <0.3103, 0.6897>")
    print("P(R|c,-s,w) = <0.9863, 0.0137>")
    print("P(R|-c,-s,w) = <0.8182, 0.1818>")


def print_b():
    print("\nPart B: The transition probability matrix")
    print("\tS1\t\tS2\t\tS3\t\tS4")
    for i in range(len(TRANS_MAP)):
        print("S%d\t%.4f\t%.4f\t%.4f\t%.4f" %
              ((i + 1), TRANS_MAP[i][0], TRANS_MAP[i][1], TRANS_MAP[i][2], TRANS_MAP[i][3]))


def print_c(prob):
    print("\nPart C. The probability for the query")
    print("P(C|-s,w) = <%.4f, %.4f>" % (prob[0], prob[1]))


def normalize(a, b):
    alpha = 1 / (a + b)
    return [a * alpha, b * alpha]


if __name__ == "__main__":
    states = {}
    for i in range(len(STATES)):
        states.update({STATES[i]: State(STATES[i], TRANS_MAP[i])})

    rand = np.random.randint(0, 4)
    current_state = STATES[rand]
    states[current_state].counter += 1

    for i in range(99999):
        current_state = states[current_state].get_next_state()
        states[current_state].counter += 1

    # for state in STATES:
    #     print(state, states[state].counter)

    prob = normalize((states[STATES[0]].counter + states[STATES[1]].counter),
                     (states[STATES[2]].counter + states[STATES[3]].counter))

    print_a()
    print_b()
    print_c(prob)
