# --- Part Two ---

# Now, the Elves just need help accessing as much of the paper as they can.
#
# Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?
#
# Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:





# Read the input from input_str.txt
with open('input_str.txt', 'r') as f:
    input_str = f.read().strip()


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

to_mark = []
matrix = [list(line) for line in input_str.splitlines()]
total_count_rolls = []

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


while True:
    to_mark = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            element = matrix[i][j]
            if element == '@':
                neighbours_list = find_the_neighbours(i, j, matrix)
                count = neighbours_list.count('@')
                print(f"Element at position ({i},{j}) has {count} neighbours")
                if count < 4:
                    to_mark.append((i,j))

    if not to_mark:
        break

    for i, j in to_mark:
        matrix[i][j] = 'x'

    rolls_count = sum(row.count('x') for row in matrix)
    print(f'Count in iteration: {rolls_count}')

    total_count_rolls.append(rolls_count)


    # marked as removed
    for i,j in to_mark:
        matrix[i][j] = '.'

    for row in matrix:
        print(''.join(row))


print(f'Total rolls removed: {sum(total_count_rolls)}')
# Total rolls removed: 8366

