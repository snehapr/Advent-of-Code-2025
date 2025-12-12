# --- Part Two ---

# The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.
#
# So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.
#
# Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:
#
# 3-5
# 10-14
# 16-20
# 12-18
# The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.
#
# Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?

ranges=[]

with open('fresh_ingredients_actual.txt', 'r') as f:
    lines = f.readlines()

# with open('fresh_ingredients.txt', 'r') as f:
#     lines = f.readlines()


lines = [line.strip() for line in lines]

separator_index = lines.index('')

for line in lines[:separator_index]:
    start, end = map(int, line.split('-'))
    ranges.append((start,end))

# fresh_ids = set()
# for start, end in ranges:
#     fresh_ids.update(range(start, end + 1))
#
# print(f'Total fresh ingredient id count is : {len(fresh_ids)}') --> takes a lot of time and memory

# ----------------------------------------------------------

ranges.sort()
# Merge overlapping ranges
merged = []
for start, end in ranges:
    if not merged or merged[-1][1] < start - 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

# Sum the lengths
total_count = sum(end - start + 1 for start, end in merged)
print(f'Total fresh ingredient id count is : {total_count}')
# Total fresh ingredient id count is : 348548952146313
