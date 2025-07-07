# Task 1:

def cat_greeting (word):
    print(f'cat says {word}')

print()
print('-cat greetings function-')
print()
cat_greeting('wiwiwiwi')

# Task 2: 

def generate_superhero_power ():
    name = 'Max'
    power = 'flying'
    print(f"{name} is a super hero that has the power of {power}")

print()
print('-function with fixed values with integrated printing-')
print()

generate_superhero_power()

#Task 3:

def generate_superhero_power2 ():
    power = "night vision"
    return power

print()
print('-function with return-')
print()
print('Carl is a superhero that has the power of ' + generate_superhero_power2())

# Task 4:

def generate_superhero_power3 (user_name, super_power):
    hero_description = f"{user_name} is a super hero that has the power of {super_power}!"
    return hero_description

print()
print('-function with arguments-')
print()
print(generate_superhero_power3 ("Angel", "X-ray vision"))

# Task 5:

def cat_greeetings_loop ():
    for i in range(5):
        print('meow!')

print()
print('-cat greetings loop function-')
print()
cat_greeetings_loop()

# Task 6:

def generate_multiple_powers (powers_list):
    for i in range(len(powers_list)):
        current_power = powers_list[i]
        print(f'-{current_power} \n')

powers = ["flying", 'X-ray vision', 'Super strength', 'Invisibility', 'fire control']
print()
print('-super powers list iteration function-')
print()
print('powers list:')
print()
generate_multiple_powers(powers)
print()

# EXTRA BECAUSE I WAS BORED :)

# my example:

#Angel is a super hero that has the power of Fixing stuff!

#He fights chatgpt to save the city of oakland from Extreme Lazyness!

def generate_story (villain_name, city, issue):
    print(f'He fights {villain_name} to save the city of {city} from {issue}!')


user_name1 = input("Now enter your name here!: ")
print()
user_power = input("Now enter the power you want to have here!: ")
print()
user_villain = input('Enter the name of the villain you fight here: ')
print()
user_city = input('what city do you protect from your villain?: ')
print()
user_issue = input('finally, what issue is your villain causing to the city?: ')
print()
print(generate_superhero_power3(user_name1, user_power))
print()
generate_story(user_villain, user_city, user_issue)
print()


