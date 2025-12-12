# --- Part Two ---


# The Elves just remembered: they can only switch out tiles that are red or green. So, your rectangle can only include red or green tiles.
#
# In your list, every red tile is connected to the red tile before and after it by a straight line of green tiles. The list wraps, so the first red tile is also connected to the last red tile. Tiles that are adjacent in your list will always be on either the same row or the same column.
#
# Using the same example as before, the tiles marked X would be green:
#
# ..............
# .......#XXX#..
# .......X...X..
# ..#XXXX#...X..
# ..X........X..
# ..#XXXXXX#.X..
# .........X.X..
# .........#X#..
# ..............
# In addition, all of the tiles inside this loop of red and green tiles are also green. So, in this example, these are the green tiles:
#
# ..............
# .......#XXX#..
# .......XXXXX..
# ..#XXXX#XXXX..
# ..XXXXXXXXXX..
# ..#XXXXXX#XX..
# .........XXX..
# .........#X#..
# ..............
# The remaining tiles are never red nor green.
#
# The rectangle you choose still must have red tiles in opposite corners, but any other tiles it includes must now be red or green. This significantly limits your options.
#
# For example, you could make a rectangle out of red and green tiles with an area of 15 between 7,3 and 11,1:
#
# ..............
# .......OOOOO..
# .......OOOOO..
# ..#XXXXOOOOO..
# ..XXXXXXXXXX..
# ..#XXXXXX#XX..
# .........XXX..
# .........#X#..
# ..............
# Or, you could make a thin rectangle with an area of 3 between 9,7 and 9,5:
#
# ..............
# .......#XXX#..
# .......XXXXX..
# ..#XXXX#XXXX..
# ..XXXXXXXXXX..
# ..#XXXXXXOXX..
# .........OXX..
# .........OX#..
# ..............
# The largest rectangle you can make in this example using only red and green tiles has area 24. One way to do this is between 9,5 and 2,3:
#
# ..............
# .......#XXX#..
# .......XXXXX..
# ..OOOOOOOOXX..
# ..OOOOOOOOXX..
# ..OOOOOOOOXX..
# .........XXX..
# .........#X#..
# ..............
# Using two red tiles as opposite corners, what is the largest area of any rectangle you can make using only red and green tiles?




from itertools import combinations
from bisect import bisect_left, bisect_right

# 1. Read points from file
with open('red_tiles_locations_v1.txt', 'r') as f:
    points = [tuple(map(int, line.strip().split(','))) for line in f if line.strip()]

# 2. Build edges (bounds)
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2,s3), ..."
    a, b = iterable[:-1], iterable[1:]
    return zip(a, b)

bounds = list(pairwise(points)) + [(points[-1], points[0])]

# 3. Prepare horizontal and vertical segments
horz = sorted((u[0][1], u[0][0], u[1][0]) for u in bounds if u[0][1] == u[1][1])
vert = sorted((u[0][0], u[0][1], u[1][1]) for u in bounds if u[0][0] == u[1][0])

# 4. Rectangle validity check
def is_valid(x0, y0, x1, y1, horz, vert):
    if x0 > x1: x0, x1 = x1, x0
    if y0 > y1: y0, y1 = y1, y0
    # Check horizontal segments
    l = bisect_left(horz, y0, key=lambda u: u[0])
    r = bisect_right(horz, y1, key=lambda u: u[0])
    for y, s, e in horz[l:r]:
        if y0 < y < y1 and min(s, e) < x1 and max(s, e) > x0:
            return False
    # Check vertical segments
    l = bisect_left(vert, x0, key=lambda u: u[0])
    r = bisect_right(vert, x1, key=lambda u: u[0])
    for x, s, e in vert[l:r]:
        if x0 < x < x1 and min(s, e) < y1 and max(s, e) > y0:
            return False
    return True

# 5. Find largest rectangle (unconstrained)
A_unconstrained = max(
    (abs(x0-x1)+1) * (abs(y0-y1)+1)
    for (x0, y0), (x1, y1) in combinations(points, 2)
)
print("Largest unconstrained rectangle area:", A_unconstrained)
# Largest unconstrained rectangle area: 4765757080

# 6. Find largest rectangle (constrained by polygon)
A_constrained = 0
best_rect = None
for (x0, y0), (x1, y1) in combinations(points, 2):
    area = (abs(x0-x1)+1) * (abs(y0-y1)+1)
    if is_valid(x0, y0, x1, y1, horz, vert):
        if area > A_constrained:
            A_constrained = area
            best_rect = (x0, y0, x1, y1)

print("Largest rectangle inside polygon area:", A_constrained)
# Largest rectangle inside polygon area: 1498673376

print("Rectangle corners:", best_rect)
# Rectangle corners: (5664, 67242, 94679, 50407)