cookbook = ['egg', 'bacon', 'burger']

# Using this recipe parameter allows us to add any item we desire later when calling the function.
def create (recipe):
    cookbook.append(recipe)
    print(f'You added the recipe: {recipe}')

# takes in the index of our list to access any item in the list and returns it.
def read (index):
    if index < len(cookbook):
        return cookbook[index]   
    else:
        print(f'index {index} is not in the cookbook!')

# uses the index to access the value at an index and uptade its contents.
def update (index, recipe):
    if index < len(cookbook):
        cookbook[index] = recipe
        print(f'has been updated to -{recipe}- succesfully!')
    else:
        print(f'index {index} is not in the cookbook! Please select an index within the range to modify its content')

# Deletes the elememnt at a specified index.
def destroy (index):
    if index < len(cookbook):
        cookbook.pop(index)
        print('has been deleted succesfully!')
    else:
        print(f'index {index} is not in the cookbook! Please select an index within the range to delete it')

# Prints the entire list.
def list_all_recipes():
    print(cookbook)

def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            print()
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            print()
            print('REMEMBER THAT THE INDEX STARTS AT 0')
            print()
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
            past_recipe = cookbook[index]
            print()
            print(f'recipe at index {index}: {past_recipe}')
        elif choice == "3":
            print()
            print('REMEMBER THAT THE INDEX STARTS AT 0')
            print()
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            print()
            past_recipe = cookbook[index]
            print(f'recipe selected at index {index}: -{past_recipe}-')
            update(index, recipe)
        elif choice == "4":
            print()
            print('REMEMBER THAT THE INDEX STARTS AT 0')
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            past_recipe = cookbook[index]
            print()
            print(f'recipe selected at index {index}: -{past_recipe}-')
            destroy(index)
        elif choice == "5":
            print()
            print('COOKBOOK CONTENTS:')
            list_all_recipes()
        elif choice == "6":
            print()
            print("Exiting the program.")
            break
        else:
            print()
            print("Invalid choice, please try again.")


main()




