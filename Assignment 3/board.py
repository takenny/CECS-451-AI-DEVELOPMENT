import random
import numpy as np


class Board:
    # constructor
    # takes an int as a parameter
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)] # this is a multi-dimentional list
        self.fit = 0

        # Generate A random board
        # The boad will only have 1 queen per row
        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1

    # calculates how many pairs of queens are attacking each other
    def fitness(self):
        # added this so that it doesnt add to the fitness everytime you run fitness
        self.fit = 0
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

    # prints out the board
    # 1 means that there is a queen there
    # 0 means that it is an empty space
    def show(self):
        print(np.matrix(self.map))
        print("Fitness: ", self.fit)

    # change a specific space in the board
    # i and j are the index of the space being flipped
    def flip(self, i, j):
        if self.map[i][j] == 0:
            self.map[i][j] = 1
        else:
            self.map[i][j] = 0

    # getters
    def get_map(self):
        return self.map

    def get_fit(self):
        return self.fit

    # convert the board into an encoded string
    # the encoded string will consist of numbers from  1 to the number of queens
    # the index of each of the numbers represents the row the queen is in
    # the numbers represents the columns that that the queen is in
    def __str__(self):
        full_str = ''
        for elem in self.map:
            pos = 0
            result = list(elem)
            pos = result.index(1)
            pos += 1
            full_str += str(pos)
        return full_str

    # Converts the encoded string back into a board
    def set_map(self, gene):
        for i in range(self.n_queen):
            self.map[i] = [0] * 5
            self.flip(i, int(gene[i]) - 1)


if __name__ == '__main__':
    test = Board(5)
    test.fitness()
    test.show()
    print(test)
