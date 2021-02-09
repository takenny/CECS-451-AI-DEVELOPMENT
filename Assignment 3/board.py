import random
import numpy as np


class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)]
        self.fit = 0

        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1

    def fitness(self):
        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    for k in range(1, self.n_queen - i):
                        if self.map[i + k][j] == 1:
                            self.fit += 1
                        if j - k >= 0 and self.map[i + k][j - k] == 1:
                            self.fit += 1
                        if j + k < self.n_queen and self.map[i + k][j + k] == 1:
                            self.fit += 1

    def show(self):
        print(np.matrix(self.map))
        print("Fitness: ", self.fit)

    def flip(self, i, j):
        if self.map[i][j] == 0:
            self.map[i][j] = 1
        else:
            self.map[i][j] = 0

    def get_map(self):
        return self.map

    def get_fit(self):
        return self.fit

    def __str__(self):
        full_str = ' '
        for elem in self.map:
            pos = 0
            result = list(elem)
            pos = result.index(1)
            pos += 1
            full_str += str(pos)
        return full_str

    def set_map(self, gene):
        for i in range(self.n_queen):
            self.map[i] = [0] * 5
            self.flip(i, int(gene[i]) - 1)
        print(self.map)


if __name__ == '__main__':
    test = Board(5)
    test.fitness()
    test.show()
    print(test)

