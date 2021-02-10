from board import Board
import random
import numpy as np
import copy
import time

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
NUM_PAIRS = 10
START_TIME = time.time()


def crossover(genes_string):
    for i in range(0, len(genes_string), 2):
        rn = random.randint(0, NUM_QUEENS)

        # leftover = len(genes_String) - rn
        if rn != 0:
            str1 = genes_string[i]  # getting the first string
            str2 = genes_string[i + 1]
            temp1 = [str1[0:rn], str1[rn:len(str1)]]
            temp2 = [str2[0:rn], str2[rn:len(str2)]]
            temp1[1], temp2[1] = temp2[1], temp1[1]

            # grabs the string from split point to end
            genes_string[i] = ''.join(temp1)
            genes_string[i + 1] = ''.join(temp2)


def mutation(genes_string):
    # run for each gene string
    for i in range(len(genes_string)):
        # convert string to list
        s = list(genes_string[i])
        genes_string[i] = ""

        # Generate random numbers for the index and  the number in that index
        # rn is the random index. if index is 0 then no character is changed
        # ran is the number that is written to the random index
        rn = random.randint(0, NUM_QUEENS - 1)
        ran = random.randint(0, NUM_QUEENS)
        if rn != 0:
            s[rn] = ran

        # convert back into a string and put it back into genes_string
        for character in s:
            genes_string[i] += str(character)


def selection(genes):
    gene_fitness = []
    genes_temp = []
    fit_sum = 0
    # for gene in genes:
    #   print("og", gene, gene.get_fit())
    for gene in genes:
        fit = NUM_PAIRS - gene.get_fit()
        fit_sum += fit
        gene_fitness.append(fit)
    for i in range(len(gene_fitness)):
        gene_fitness[i] = gene_fitness[i] / fit_sum
        # print(genes[i], genes[i].get_fit(), gene_fitness[i])
    cdf = np.cumsum(gene_fitness)
    for i in range(len(genes)):
        rn = random.random()
        for j in range(len(cdf)):
            if rn < cdf[j]:
                genes_temp.append(copy.deepcopy(genes[j]))
                # print(rn, genes[j], cdf)
                break
    for i in range(len(genes)):
        genes[i] = copy.deepcopy(genes_temp[i])
    # for gene in genes:
    #    print("new", gene)


def genetic():
    # create the 8 genes
    genes = []
    genes_string = []
    solution_index = 10
    solution_found = False
    for i in range(NUM_GENES):
        genes.append(Board(NUM_QUEENS))
        genes[i].fitness()

    # Repeat the process until the solution is found
    while not solution_found:
        selection(genes)

        for i in range(len(genes)):
            if genes[i].get_fit() == 0:
                solution_index = i
                solution_found = True
                break

        # clear the genes_string if there is strings in there
        # the array will continue to grow
        genes_string.clear()

        # convert boards to strings and place them in genes_string
        # this array is used for the crossover and mutation function
        for gene in genes:
            genes_string.append(gene.__str__())

        crossover(genes_string)
        mutation(genes_string)

        # convert the strings back into boards and generate their fitness
        for i in range(NUM_GENES):
            genes[i].set_map(genes_string[i])
            genes[i].fitness()
            # For each board check if the solution is found,
            # If the solution is found then we can stop looking
            if genes[i].get_fit() == 0:
                solution_found = True
                solution_index = i
                break

    # Print the solution
    run_time = round((time.time() - START_TIME) * 1000, 2)
    print("Runtime: %3.2fms" % run_time)
    genes[solution_index].show()


genetic()