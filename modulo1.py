print("Hello World!")

# for commenting you need to use cardinal (#)
# print serves to imprinting the result of the code we are using

print(1 + 2)
print(5 - 3)

# we can also create variables trough  assignment, using "=":

x = 1 + 2
print(x)


# this variable is stored and it can be used to various applications 

print(x * x)	# multiplications
print(x / 2)	# divisions

print(x > 9)	# logic, x higher than 9?
print(x == x)	# logic, x equals x?
print(x == 4)	# logic, x equals 4?

# other operations

print(18 / x)
print(18 % x)	# the modulo, calculates the rest of a division 

print(x ** 2)	# exponentials
print(x ** (1/2)) # square root 

# alternative 
import math		# importing a package, will be later discussed in greater detail
print(math.sqrt(x))	# bring extra functions

### Exercise 1

# Using the variable x
# How much will 40000€ be after 3 years, with an interest rate of 5%?




#--------------Variables--------------

# Variables names must be practical, logical, easy to memorize and easy to write.
# It mustn't contain special characters or begin with uppercase.

best_workshop_in_the_world = "data_science.py"	# makes sense but it's not practical
print(best_workshop_in_the_world) 				

jest = "data_science.py"
print(jest)                                     # note that two variables can have the same value

# Values have different types. The most common ones are:

a = 4.5
print(type(a))			# Float - It can have a decimal part
print(type(x))			# Int - It only contains integer 
print(type(jest))		# String (str) - Contains one or more words

validity = x > 9		# As we could see before, this logic example returns true or false
print(type(validity))	# Boolean (bool) 

# Q: If we apply an operation between a variable from type int and a variable type float, which type is the result?



### Exercise 2
# Using only variables now
# How much would cost 40000€ stored with a interest rate of 5%, 3 years later?




# Advantages of using variables:
# It's much more practical and simple. Image that you want answer to the same question but instead of interest rate of 5% you want it to be 3%
# you only need to change the value of the variable "interest" and get your result.

# NOTE
# If we try to print the string: "The result is:" and the variable result you should do it like this:
print("The result is: " + result) 

result = str(result)
print("The result is: " + result)

print("The result is ", result)

#--------------Lists--------------

# List are the most convenient way to store multiple values without having to create lots of different variables.

# For example, if we want to store the ages of a group of persons...
age1 = 17
age2 = 20
age3 = 30
# ...
# Or
# Create a list
ages = [17, 20, 30]

# A list can have different types of values, including lists!
# For example, we can store the names and the corresponding ages of some JEST members;

participants = ["Rute", 20, "Hugo", 19, "Calil", 28, "Coelho", 24]
print(participants)

# Or, we can do even better:
# Alternative list
participants32 = [["Rute",20],["Hugo",19],["Calil",28],["Coelho",24]]
print(participants32)

# But how can we print/select one or various elements of a list?

# For example, selecting the 3th element of the previous list:

# NOTE: The count of the elements starts with 0!

# code: nameofthelist[index]
print(participants[2]) 	# Output "Hugo"

# Or, starting from the ending of the list. The last element will correspond to [-1].
print(participants[-1]) # Output gives back "24"



 #Using the alternative list we would have to do:
 #participants32[[2][1]]
print(participants32[1][0])

### Exercise 3

# Starting from the end of the list, print "Hugo"



# Now imagine the you want to create a second list identical to the first one but excluding "Coelho" and his age:


participants2 = participants		
print(participants2)				

# Either you do:
participants2 = participants[:6] # creats an range that goes from the first element to the 6th without including it.

# Or,  instead of creating a new list you can just use a command that deletes the elements "Coelho" and "24":
del(participants[6])
print(participants)
del(participants[6])# We have already deleted the 6th element, so "24" is the new 6th element
print(participants) 

# Now we want to add the elements again:
participants = participants + ["Coelho", 24] # or participants.append("Coelho") e participants.append(24)                  
print(participants)

# Now we are changing an element. Rute's age becomes 21:
participants[1] = 21 
print(participants)

### Exercise 4 - What is the mean average of the participants ages?


# Note: when we create, for example, a list x and a list y and we define list y as an equal of x (y=x) and if then we change an element from list y and print both lists, this element will also be changed in x. That's because both variables, x and y, are pointing to the same list.

# To work around this situation we can do: y = x[:], y corresponds now to a copy of the list defined in x and not the list it self! 

# Now we can change y and its will not affect x. 


# --------------- Functions --------------------

# Pieces of code that can be used for resolving different tasks. For example, 
# on "Variables" we introduced the function o type() which is used to return the type 
# of the variable we chose.

# Other useful functions are:
#max() 		# tell us the higher element of a list, for example.
#round() 	# rounds values
#len() 		# gives the length of an object
#help(len) 	# gives details about how functions work and which arguments they need

# There are a lot of useful functions that can help us writing efficient code.
# The best way to find them is to google, (StackOverflow and Github are also yours friends).
# You can search for manuals or tutorials that will indicate you all the useful functions of Pyhton.

# One function that we will use is input()
# You can use help(intput) to learn what it does, but short answer, it keeps a string provided by the user.
# For example:

age = input("Qual achas que é a idade do Coelho? " ) 
print(type(age)) 		# thus, you can always expect type string

# So, how could we calculate the year he was born?

print("O ano de nascimento dele é então ", 2017-age)  # error, because you can't do operations between int and str
# thus we need to convert the age (type string) variable in an integer using:
# int()

age = int(age)
print("O ano de nascimento dele é então ", 2017 - age)

age = int(input("Qual achas que é a idade do Coelho? " ))
print(type(age))

# -------------- Tuples -----------

# Tuples are similar to lists, and can contain multiple types of objects (int, str, lists, other tuples) 
# The main difference among tuples and lists, is that you cannot change elements of tuples. 
# Tuples are immutable!
# See the following example:

clubes = ['Sporting','Academica','Porto','Benfica','Braga']	# type list
print(clubes)
clubes[1] = 'Guimarães' 
print(clubes)	# we verify that that the element Academica was substituted by Guimarães

# Let's create it as a tuple instead. Lists use [], while tuples use ().

clubes_1 = ('Sporting','Academica','Porto','Benfica','Braga')	# type tuple
clubes_1[1] = 'Guimarães' #would give an error. This is useful when we don't want changes to happen in our dataset.

# There are other operations that can be used with tuples

print(len(clubes_1)) 			# tuple's size.
print(clubes_1.index('Porto'))	# position where Porto first appears.
print('Sporting' in clubes_1) 	# Uses a boolean (TRUE or FALSE) to indicate if Sporting exists or not within this specific tuple.

clubes_europa = clubes_1 + ('Real Madrid','Chelsea')
print(clubes_europa)


# Even though you cannot change them, you can still consult them.

melhor_clube = clubes_1[0]
print("O melhor clube é", melhor_clube)

# --- Methods
#
# In Python everything is an object. Object's have specific methods according to their types.
# For example, until now we have been using the object variable, and variables have different types: string, integer, etc.
# Thus, methods are specific functions of objects. Then, some of those will not apply to different types, or will behave in non-expected ways.

# Example:
# Going back to our list of clubs, we can add "Tondela", as we have learned before
# clubes = clubes + ["Tondela"]
# clubes.append("Tondela")

# Or we can use a method specific to type list objects:
print(clubes.index("Braga"))
# Output 4
print(clubes)
# Index method can be applied to type string:
# For example, melhor_clube is a string defined as "Sporting" 
print(melhor_clube.index("S"))
# Output 0
print(melhor_clube)
# There other methods for lists, like pop. Check it's behaviour below:
Guardar = clubes.pop(4)
print(Guardar)
print(clubes)

### Exercise 5 - Construct a list that stores numbers inserted by the user.


# --------------- Dictionaries --------------------

# Let's look at dictionaries
idades = {'Rute':20, 'Hugo':19, 'Coelho':24, 'Calil':28}

# We have seen that lists use [], tuples use (), now we have dictinaries that use {}.
# Each element in a dictionary, as 2 components. 'Rute':19 is ONE element, where 'Rute' is key and 19 is its value.
# In lists and and tuples we used the position to access elements. However, dictionaries are unordered.
print(idades) # As you have *probably* seen, orders didn't always come exactly the same.

# So using idades[0] will not give us Rute's age. To check that, we have to use the key!
print(idades['Rute']) 	# gives us 20.

# Other operations we ca use dictionaries for are:
print(len(idades)) 		# how many items does the dictionary has
del idades['Calil'] 	# remove an element
print(idades) # it deletes both key and value
print(len(idades))

# To add Calil back to the list as an element we do the following:
idades['Calil'] = 28
print(idades)			# Calil is back.

# Other methods that work in dictionaries:

## Methods that do NOT modify dictionaries:
#idades.copy() 						gives copy of dictionary
#idades.items() 					gives elements of dictionary
#idades.keys() 						gives keys of dictionary
#idades.values() 					gives values of dictionary
#idades.get(key,default=None)) 		gives value of specific key, if it exists, otherwise gives None.

## methods that modify dictionaries:
#idades.clear() 						removes all elements of dictionary
#idades.pop(key,default=None) 			remove, while giving as output, a value
#idades.popitem() 						removes randomly, while giving as output, a key-value pair.
#idades.update(dict2) 					adds the pair (key,value) from a dict2 to dict1
#idades.setdefault(key,default=None)) 	like .get but updates the pair with key:default


# --------------- Conditions --------------------
#
# It is recurrent, in every programming language, to learn how to write things like: 
# if (your condition):		
#	your code

# Thus, if condition is true, program executes code, otherwise it does not.
# Example:
idade = int(input("Your age please: ")) # We use input to tell the user to add a value.

if (idade <= 12):
	print("You are a child.")
elif (12 < idade < 18):
	print("You are a teenager.")
else:
	print ("You are an adult")

# Notice if(), then elif() and else.

# Exercise 6 - Ask user a number, give "It's even." or "It's odd." depending on if the number is even or odd.



# --------------- Loops --------------------

# For and While Loops

# Example 1. We want to print the names in a list, separated.

nomes = ["Joana", "Tiago", "João", "Joana", "Marta", "Mariana", "Joana"]

# Using for 
for x in nomes: # In each iteration x will correspond to a specific element
	print(x)

print (x) # this print() is outside of the loop, thus will only give the last element

# Alternative
for i in range(len(nomes)):
	print(i)
	print(nomes[i])

# Using While
i = 0
while (i<len(nomes)): 	# while the condition is true, the code below will be repeated 
	
	print (nomes[i])
	i +=1 				# add one. It could also be, 	i = i+1

#print (nomes[i])

# Exercise 7 - How many times does the name "Joana" appears?
