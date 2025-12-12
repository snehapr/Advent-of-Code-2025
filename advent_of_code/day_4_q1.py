# --- Day 4: Printing Department ---
# You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).
#
# Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.
#
# "Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."
#
# If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.
#
# The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.
#
# For example:
#
# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.
#
# In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):
#
# ..xx.xx@x.
# x@@.@.@.@@
# @@@@@.x.@@
# @.@@@@..@.
# x@.@@@@.@x
# .@@@@@@@.@
# .@.@.@.@@@
# x.@@@.@@@@
# .@@@@@@@@.
# x.x.@@@.x.
# Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?


# input_str = """
# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# """.strip()


# Read the input from input_str.txt
with open('input_str.txt', 'r') as f:
    input_str = f.read().strip()

to_mark = []
matrix = [list(line) for line in input_str.splitlines()]


def find_the_neighbours(i, j, matrix):
    neighbours = []
    if i-1 >= 0:
        if j-1 >=0:
            t1 = matrix[i-1][j-1]
            neighbours.append(t1)
        t2 = matrix[i-1][j]
        neighbours.append(t2)
        if j+1 < len(matrix[0]):
            t3 = matrix[i-1][j+1]
            neighbours.append(t3)


    if j-1 >=0:
        left_ele = matrix[i][j-1]
        neighbours.append(left_ele)

    if j+1 < len(matrix[0]):
        right_ele = matrix[i][j+1]
        neighbours.append(right_ele)

    if i+1 < len(matrix):
        if j-1 >=0:
            d1 = matrix[i+1][j-1]
            neighbours.append(d1)
        d2 = matrix[i+1][j]
        neighbours.append(d2)
        if j+1 < len(matrix[0]):
            d3 = matrix[i+1][j+1]
            neighbours.append(d3)

    return neighbours

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        element = matrix[i][j]
        if element == '@':
            neighbours_list = find_the_neighbours(i, j, matrix)
            count = neighbours_list.count('@')
            print(f"Element at position ({i},{j}) has {count} neighbours")
            if count < 4:
                to_mark.append((i,j))

for i, j in to_mark:
    matrix[i][j] = 'x'

for row in matrix:
    print(''.join(row))
print(sum(row.count('x') for row in matrix))
# count of rolls is 1409



