from board import Board
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
