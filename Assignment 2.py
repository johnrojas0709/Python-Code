'''The code for this project represents my own, independent work. I 
have neither given nor received help on this assignment from other
students.'''
''' John Rojas '''

import random
snake_start = []
snake_end = [] # less than snake_start

ladder_start = []
ladder_end = [] # larger than ladder_start

# function that creates board 
def create_board(snake_start, snake_end, ladder_start, ladder_end):   
    #VARIABLES
    usedspaces = []
    snake_num = 0
    ladder_num = 0
    snake_random = 0
    ladder_random = 0

    # SNAKE GENERATION
    snake_num = random.randint(2,8)
    print(f'{snake_num} snakes')
    
    for i in range(snake_num):   # creates x amount of random snakes from 2 to 8
        snake_random = random.randint(2, 63)
        x = True
        while x == True:    # determines repeated numbers in usedspaces
            for n in usedspaces:
                if n == snake_random:
                    snake_random = random.randint(2, 63)
                    n = 0
            x = False
        # Adds spaces not repeated to both lists
        snake_start.append(snake_random) 
        usedspaces.append(snake_random)

        snake_random = random.randint(2, 63)
        x = True
        while x == True:    # determines repeated numbers in usedspaces
            for n in usedspaces:
                if n == snake_random:
                    snake_random = random.randint(2, 63)
                    n = 0     
            x = False
        # Adds spaces not repeated to both lists
        snake_end.append(snake_random)
        usedspaces.append(snake_end[i])

        # Switches places if start is less than end
        if snake_start[i] < snake_end[i]:
            snake_start.append(snake_end[i])
            snake_end.append(snake_start[i])
            snake_start.pop(i)
            snake_end.pop(i)

        print(f'Snake #{i+1}: {snake_start[i]} to {snake_end[i]}')
    i = 0
    n = 0

    # LADDER GENERATION
    ladder_num = random.randint(2,8)
    print(f'\n{ladder_num} ladders')

    for i in range(ladder_num):   # creates x amount of random snakes from 2 to 8
        ladder_random = random.randint(2, 63)
        x = True
        while x == True:    # determines repeated numbers in usedspaces
            for n in usedspaces:
                if n == ladder_random:
                    ladder_random = random.randint(2, 63)
                    n = 0
            x = False
        # Adds spaces not repeated to both lists
        ladder_start.append(ladder_random)
        usedspaces.append(snake_random)

        ladder_random = random.randint(2, 63)
        x = True
        while x == True:    # determines repeated numbers in usedspaces
            for n in usedspaces:
                if n == ladder_random:
                    ladder_random = random.randint(2, 63)
                    n = 0     
            x = False
        # Adds spaces not repeated to both lists
        ladder_end.append(ladder_random)
        usedspaces.append(ladder_end[i])

        # Switches places if start is less than end
        if ladder_start[i] > ladder_end[i]:
            ladder_start.append(ladder_end[i])
            ladder_end.append(ladder_start[i])
            ladder_start.pop(i)
            ladder_end.pop(i)

        print(f'Ladder #{i+1}: {ladder_start[i]} to {ladder_end[i]}')

# function to determine if player is on snake or ladder
def snake_or_ladder(pos, snake_start, snake_end, ladder_start, ladder_end):
    for i in snake_start:
        if pos == i:
            print('Snake!')
            z = snake_start.index(i)
            pos = snake_end[z]
            return pos

    for n in ladder_start:
        if pos == n:
            print('Ladder!')
            pos = ladder_end[ladder_start.index(n)]
            return pos
    else:
        return pos

        
# defines player position
def take_turn(pos):
    pos = random.randint(1, 6)   #random num from 1 to 6 inclusive
    return pos # returns random number

player_num = [1, 2] # list for num of players
player_pos = [1, 1] # list for position of player

final = 0 # final pos - helps determine end of while loop
die = 0 # stores return of take_turn function
x = 0

create_board(snake_start, snake_end, ladder_start, ladder_end)

print()

while final < 64: # loop iterates whenever final is less than 64
    for i in range(2):  # loop that iterates twice (number of players)
        print(f'Player {player_num[0]} is on space {player_pos[0]}')  #updates on spaces for players
        print(f'Player {player_num[1]} is on space {player_pos[1]}')

        x = player_pos[i]   #stores position of i player in x
        die = take_turn(die) #store random num per iteration 

        print(f'Player {player_num[i]} rolls the dice: {die}')   #prints roll die num

        player_pos[i] += die   # adds position to roll die num
        player_pos[i] = snake_or_ladder(player_pos[i], snake_start, snake_end, ladder_start, ladder_end)   #sends updated position to snake_or_ladder
        final = player_pos[i]   #updates final position to updated position

        if player_pos[i] == 64:   #condition: if position of player i is 64, win - break loop
            print(f'Player {player_num[i]} wins!')
            break

        elif player_pos[i] > 64:  #if not 64, if position of player i is > 64, go back to last position (x), update final as well (for while loop)
            player_pos[i] = x
            final = player_pos[i]
