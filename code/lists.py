#declaring a list
list = ["item", 3, True]
print(list)

#indexing the first item in a list, begins at 0
index_list = ["item", 3, True]
print(index_list[0])

#indexing the first item from the back of a list, begins at -1
back_list = ["item", 3, True]
print(index_list[-1])

#indexing a sublist within a list, second number is non-inclusive
sub_list = ["item", 3, True]
print(sub_list[1:3])

#indexing a sublist beginning at a certain index
sub_list2 = ["item", 3, True]
print(sub_list2[1:])

#modifying an item in a list
modify_list = ["first", "second", "third", "fourth", "fifth"]
modify_list[1] = "change"
print(modify_list)

#appending lists
first_list = [1, 2, 3]
second_list = [4, 5, 6]
first_list.extend(second_list)
print(first_list)

#inserting an item into an index of the list
insert_list = [1, 2, 3, 4]
insert_list.insert(1, "insert")
print(insert_list)

#remove last item in a list
pop_list = [1, 2, 3, 4]
pop_list.pop()
print(pop_list)

#find index of an item in the list
find_list = [1, 2, 3, 4]
print(find_list.index(3))

#count instances of item in list
count_list = [1, 1, 1, 2, 4]
print(count_list.count(1))

#sorting a list
sort_list = [1, 2, 4, 7, 5, 9, 8]
sort_list.sort()
print(sort_list)

#reversing a list
rev_list = [1, 2, 3, 4, 5]
rev_list.reverse()
print(rev_list)

#copying a list
org_list = [1, 2, 3]
new_list = org_list.copy()
print(new_list)