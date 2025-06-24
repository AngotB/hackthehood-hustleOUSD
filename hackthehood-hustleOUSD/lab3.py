# task 1: working with strings
food = "burger"
print(food[0:3]) #print the 3 first characters
print(food[-3:]) #print the 3 last characters
first_last = food[0] + food[-1] #combine first and last character
print(first_last)
food_list = food.split() #places the element into a list
print(food_list)
joined_food =  ' '.join(food_list) #re-integrates the element as a single string
print(joined_food)

# task 2: working with lists
number_list = [1,2,3,4,5]
print(number_list)
number_list.append(6) #adds an element to the end of a list
print(number_list)
number_list.insert(3,3.5) #inserts an element at a specific index 
print(number_list)
number_list.pop() #removes an element at a specific index
print(number_list)
number_list.remove(number_list[1]) #removes specified element from the list
print(number_list)
print(number_list[:3]) #prints the first 3 elements from the list
print(number_list[-3:]) #prints the last 3 elements from the list

# task 3: working with dictionaries
books = {'Goe Booth':'Tyrell','John Steinbeck':'Of mice and men', 'Art Spiegelman':'Maus','Laura Esquivel':'Like water for Chocolate'}
print(books.keys()) #Prints all of the keys in the dictionary
print(books.values()) #Prints all of the values in the dictionary
print(books.get('Goe Booth'))
books.pop('Art Spiegelman')
print(books)
del books['Goe Booth']
print(books)

