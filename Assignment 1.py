'''The code for this project represents my own, independent work. I 
have neither given nor received help on this assignment from other
students.'''
''' John Rojas '''

import math # Needed to find absolute values

truePrice = int(input('What is the true price of the Prize? '))
contestants_num = int(input('How many contestants are playing today? '))
print()
overBid = truePrice * 2  # Determine overbid - 2 times value of truePrice
winning_contestant = 0   # Stores number of winning contestant

if contestants_num > 50:   # Helps limit the amount of contestants - To minimize error when entering input
    print('Too many contestants!')
else:
    for i in range(contestants_num):
        contestantBid = int(input(f'What is the bid for Contestant {i+1}? '))   # Repeats i Number of contestants in contestants_num
        form = truePrice - contestantBid   # Formula that determines difference b/w truePrice and Contestant

        if i == 0:  # Stores first value  and contestant in first iteration - i == 0
            winning_bid = contestantBid
            winning_contestant = f'{i+1}'

        elif contestantBid == truePrice:   # contestant Bid is equal to the true price - Obvious winner
            winning_bid = contestantBid
            winning_contestant = f'{i+1}'

        elif contestantBid <= truePrice:   # compares value of contestantBid whenever contestantBid is less than truePrice
            if contestantBid > math.fabs(form) and contestantBid != truePrice:
                winning_bid = contestantBid
                winning_contestant = f'{i+1}'

        elif contestantBid >= truePrice:   # compares value of contestantBid whenever contestantBid is greater than truePrice - Opposite
            if contestantBid < math.fabs(form) and contestantBid != truePrice: 
                winning_bid = contestantBid
                winning_contestant = f'{i+1}'  

if winning_bid >= overBid:    # Determines if the closest bid to truePrice is overbid (2 times the trueValue)
    print()
    print('All contestants have overbid!')

else:    # winning Bid did not overbid
    print()
    print(f'Contestant {winning_contestant} wins')
    print(f'The winning bid was {winning_bid}.')
