# John Rojas U13874585

# code will receive user input. User will decide what sequence to use and then what the number of values will be.
# for loops, lists, and functions utilized. 
''' I he code for this project represents my own, independent work. I have neither given nor 
received help on this exam from other students'''

import math 

def menu():   # displays menu
    print('Welcome to the number sequence generator program!')
    print('1-Fibonacci Sequence')
    print('2-Catalan Sequence')
    print('3-Lazy Caterer\'s Sequence')

def fib_sequence(n):  #fibonacci sequence
    nums = [0, 1]
    x = 0
    for i in range(n - 2):
        x = nums[-2] + nums[-1]
        nums.append(x)
    return nums

def cat_sequence(n):   # catalan sequence
    nums = []
    for i in range(n):
        c = math.factorial(2 * i) / (math.factorial(i+1) * math.factorial(i))
        nums.append(int(c))
    return nums
    
def laz_sequence(n):   # lazy caterers sequence
    nums = []
    for i in range(n):
        p = (i**2 + i + 2) / 2
        nums.append(int(p))
        p = 0
    return nums

menu()
print('')
x = True
while x == True:    #iterate until user says no 
    choice = int(input('Enter your choice (1-3): '))
    # nested loops that determine values and what functions to call.
    if choice >= 1 and choice <=3:
        if choice == 1:
            value = int(input('Enter Number (>=3): '))
            if value >= 3:
                print(f'Here is a list containing the first {value} numbers of the Fibonacci sequence: {fib_sequence(value)}')
            else:
                print('Invalid entry. Try Again')
        elif choice  == 2:
            value = int(input('Enter Number (>=3): '))
            if value >= 3:
                print(f'Here is a list containing the first {value} numbers of the Catalan sequence: {cat_sequence(value)}')
            else:
                print('Invalid entry. Try Again')
        elif choice == 3:
            value = int(input('Enter Number (>=3): '))
            if value >= 3:
                print(f'Here is a list containing the first {value} numbers of the Lazy Caterer\'s sequence: {laz_sequence(value)}')
            else:
                print('Invalid entry. Try Again')
    else:
        print('Invalid Entry.', end=' ')
        continue
    ques = input('\nWould you like to run the program again? Enter yes or no: ')
    if ques == 'no':
        x = False
        print('\nThank you for using the program. Goodbye!')
    else:
        menu()
            

        
