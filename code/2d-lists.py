#declaring a 2D list
list_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#indexing the first item within a 2d list
index_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(index_list[0][0])

#iterate through each item in a 2D list
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in grid:
    for col in row:
        print(col)