# x = ["Prodip","Raju",True,22,39.22]
# print(x)

# # Duplicate values
# y = ["Prodip","Raju",True,22,39.22,22,32,"Raju"]
# print(y)

# # length
# print(len(y))

# print(type(x))

# List constructor

# z = list(["Prodip","Raju",True,22,39.22,22,32,"Raju"])
# print(type(z),z)
# print("-----------------")
# x = list(("Prodip","Raju",True,22,39.22))
# print(type(x),x)

# Python Collection (Arrays)
# 1. List 2. Tuple 3. Set 4.  Dictionary
# How to access items
# x = ["Prodip","Raju",True,22,39.22]
# print(x[0])   # Accessing first element of the list
# print(x[-3])
# print(x[::-1])    # Reverse the order of elements in a list
# # Slicing  [start:stop:step]
# print(x[1:3])     # From second element till third element
# print(x[:3])      # From beginning till third element
# print(x[3:])       # From fourth element till end

# Range of Indexes
'''
x = ["Apple", "Bannana", "Orange", "Cherry",
     "Prodip", "Mou", "Raju", "Bamangacchi"]
print(x[-6:-1])
print(x[1:4]) # ['Bannana', 'Orange', 'Cherry']
print(x[:4]) #  ['Apple', 'Bannana', 'Orange', 'Cherry']
print(x[:1]) #  ['Apple']
print(x[1:]) #  ['Bannana','Orange','Cherry','Prodip','Mou','Raju','Bamangacchi']

# How to Check if the items Exists in List
x = ["Apple", "Bannana", "Orange", "Cherry",
     "Prodip", "Mou", "Raju", "Bamangacchi"]

if "Raju" in x : print("Yes Raju is present in the list")
else              : print("No Raju is present in the list")


# Modify the list
x = ["Apple", "Bannana", "Orange", "Cherry",
     "Prodip", "Mou", "Raju", "Bamangacchi"]

print(x)
x[6] = "Rahul"
print(x)
del x[5]        # Deleting an item from the list using index
print(x)

# Change a Range of Items values in List 
x = ["Apple", "Bannana", "Orange", "Cherry",
     "Prodip", "Mou", "Raju", "Bamangacchi"]

# x[1:3] = ["Kolkata","Barasat"]
# print(x)
# x[1:2] = ["Bangalore","Mumbai"]
# print(x)

x[1:3] = ["Raja"]
print(x)

# appeend 
x = ["Apple", "Bannana", "Orange", "Cherry",
     "Prodip", "Mou", "Raju", "Bamangacchi"]
x.append("Goa")
print(x)

# Insert 
x = ["Apple", "Bannana", "Orange", "Cherry",
     "Prodip", "Mou", "Raju", "Bamangacchi"]

x.insert(1,"Gurgao")
print(x)

# extend 
x = ["Apple", "Bannana", "Orange", "Cherry",
     "Prodip", "Mou", "Raju", "Bamangacchi"]

y = ["Prodip","Raju",True,22,39.22,22,32,"Raju"]

x.extend(y)
print(x)


# Remove the list

x = ["Apple", "Bannana", "Orange", "Cherry",
     "Prodip", "Mou", "Raju", "Bamangacchi"]
#x.remove("Prodip")
#x.pop()
# x.pop(3) # Specific  index of element to remove   
# x.remove("Raju")   # Value of element to remove     
# del  x[5]   # Using del keyword and specific index of element to delete
print(x)

# Deleting the list completely
# del x 

# clear the List Method
x.clear()
print(x)


# loop through list
x = ["Apple", "Bannana", "Orange", "Cherry",
     "Prodip", "Mou", "Raju", "Bamangacchi"]

for i in x:
    print(i)

print("Loop through the index number")

# Loop through the index number

for i in range(len(x)):
    print(x[i])


# Using a while loop
print("While Loop through the index number")
i = 0
while  i < len(x):
    print(x[i])
    i += 1

# Looping using list comprehension
x = ["Apple", "Bannana", "Orange", "Cherry",
     "Prodip", "Mou", "Raju", "Bamangacchi"]

[print(i) for i in x]

# [ expression  for item in list if condition]

fruit_list = ['apple','banana', 'cherry']

filtered_fruits = [fruit for fruit in fruit_list if len(fruit)>6]

print(filtered_fruits)

#  Nested List Comprehensions
matrix = [[3*i+j for j in range(4)] for i in range(2)]
print(matrix)
'''
# sort in list

x = ["Apple", "Bannana", "Orange", "Cherry",
     "Prodip", "Mou", "Raju", "Bamangacchi"]

x.sort()
print(x)
# Sort in descending order
x.sort(reverse=True)
print(x)

# revesed
