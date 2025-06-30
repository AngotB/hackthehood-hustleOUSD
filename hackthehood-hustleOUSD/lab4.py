# Task 1:
checking = "yes"

while checking == "yes":
    print('What is your age?')
    user_input = input()
    if int(user_input) >= 18:
        print("you can vote!")
    else:
        print('sorry, you cannot vote') 
    print('would you like to input another age?')
    user_input2 = input()
    checking = user_input2  

# Task 2

list1 = [5, -1, 3, 0, 7, -8]

for x in list1:
    if x > 0:
        print('the number is positive')
    elif x < 0:
        print('the number is negative')
    elif x == 0:
        print('the number is zero')

# Task 3

blocks = ['coal', 'dirt', 'diamond', 'gravel', 'stone']
print('INVENTORY:')
for i in blocks:
    if i == 'diamond':
        print(f'JACKPOT, YOU HAVE A {i} BLOCK!')
    else:
        print(f'you have a {i} block')

# Extra challenge:

checking = "yes"

while checking == "yes":
    print('welcome to the vote elegibility checker! Please enter your age or type exit to end program')
    user_input = input()
    if user_input == "exit":
        break
    elif int(user_input) >= 18:
        print("you can vote!")
    else:
        print('sorry, you cannot vote') 
    print('would you like to input another age?')
    user_input2 = input()
    checking = user_input2  