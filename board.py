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
        print("Fitness: ",  self.fit)

    def flip(self, i, j):
        if self.map[i][j] == 0:
            self.map[i][j] = 1
        else:
            self.map[i][j] = 0

    def get_map(self):
        return self.map
    
    def get_fit(self):
        return self.fit

            
if __name__ == '__main__':
    test = Board(5)
    test.fitness()
    test.show()

'''
############## Hill Climbing ###############
1. Initialize at random state.

2. Generate successors and check the fitness of each one
    - The one with the lowest random state (less than the current state)
        is the new current state

    For each row try placing the queen in different positions and check the fitness
        - The board with the lowest fitness becomes the new board (state)

3. If fitness of current state is 0, then the solution is reached and can
    end loop
    - If none of the successors are less than the current state, then create
        new random state

hill-climbing:
    create new random board

    while fitness is not 0 or local_min not reached:
        for each row in the board:
            if current state has fitness of 0:
                solution found
            else move the queen to all the possible positions and check the fitness
                if non of the other combinations have a lower fitness:
                    local min reached
                    generate new random board and restart process
                else:
                    state with lowest fitness is new current state
'''
'''
########### Genetic Algorithm#####################
Encoding: the board is encoded as a string
- The index of the string represents the row
- the number represents the column
Ex: 2413
This represents the following board:
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0
- have 1 queen per row

1. Create 8 random states
2. Use selection function to help select 8 new states
    * In the video the fitness is the number of non attacking pairs. in the code
        fitness is the number of attacking pairs, so to match the algorithm in the lecture
        fitness = total number of pairs - fitness?
    - Selection % of state = fitness of state / sum of fitness of states
    - the selection function is a cdf function...
        - generate a random number to choose the state using cdf
    - for each state run this algorithm
3. crossover
    - randomly choose a split point
        - swap the second half of each pair of genes
4. Mutation:
    - use random number from 0 to 8:
        if rn = 8:
            don't mutate
        else:
            mutate the character at that index to a random number between 0 and 7
5. Check the fitness of all the states:
    if optimal solution found:
        stop
    else:
        go back to stage 2 and repeat process.
'''