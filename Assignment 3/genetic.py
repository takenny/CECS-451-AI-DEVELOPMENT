from board import Board
import copy
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
    - for each state run this function
3. crossover
    - randomly choose a split point
        - swap the second half of each pair of genes
4. Mutation:
    - use random number from 0 to 8:
        if rn = 8:
            don't mutate
        else:
            mutate the character at that index to a random number between 0 and 7
            
   rn = random.randit(0,8)
   if (rn = 8):
   else:
            
5. Check the fitness of all the states:
    if optimal solution found:
        stop
    else:
        go back to stage 2 and repeat process.
'''
NUM_GENES = 8
NUM_QUEENS = 5
NUM_Pairs = 10


def crossover():
    pass


def mutation():
    pass


def selection():
    pass


def genetic():
    # create the 8 genes
    genes = []
    for i in range(NUM_GENES):
        genes.append(Board(NUM_QUEENS))
        genes[i].fitness()


genetic()
