thislist = ["apple", "banana", "orange"]
print(thislist)

# indexing
#0 , 1 , 2

print(thislist[-1])

# range of indexing : [start : end]
print(thislist[:2])
print(thislist[1:])

# check a list element
# ['apple','banana','orange','apple']

if "apple" in thislist:
    print('Apple is inside the list')
else:
    print('The list does not have the Apple')

# length of the list.

print(len(thislist))

# insert a new element
# Appened - Join a new element => appened()
# Position - Specified index number => insert()

# append()
thislist.append('jack fruit')
print(thislist)

# insert()
thislist.insert(1, 'berries')
print(thislist)

# update()
thislist[0] = "Green Apple"
print(thislist)


# Deleting : pop, remove, del
# pop(): By default it removes the last element. If you specified any index number it will removes that specified index number
# remove() : This method removes the element by value.
# del : It is keyword . It can delete an entire list or a specified index.
# clear() : This method clears all the elements inside the list

# pop()
thislist.pop(1)
print(thislist)

# remove()
thislist.remove('orange')
print(thislist)


# iterate - fetching the elemets from the lsit one by one
for name in thislist:
    print(name)

for i in range(len(thislist)):
    print(thislist[i])

# clear()
thislist.clear()
print(thislist)
