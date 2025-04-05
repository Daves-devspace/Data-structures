# create a list
my_list = []

#Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert the value 15 at the second position
my_list.insert(1,15)

#extend list with another list:50,60,70
my_list.extend([50,60,70])

#remove the last element from list

my_list.pop()

#sort i ascending order
my_list.sort()

#find and print the index 30
index_of_30 = my_list.index(30)
print("Index of 30:",index_of_30)


