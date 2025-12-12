# --- Day 6: Trash Compactor ---

# After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie scene when you over-enthusiastically jumped into the garbage chute!
#
# A brief fall later, you find yourself in a garbage smasher. Unfortunately, the door's been magnetically sealed.
#
# As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure they can get the door open, but it will take some time. While you wait, they're curious if you can help the youngest cephalopod with her math homework.
#
# Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of problems; each problem has a group of numbers that need to either be either added (+) or multiplied (*) together.
#
# However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:
#
# 123 328  51 64
# 45 64  387 23
# 6 98  215 314
# *   +   *   +
# Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.
#
# So, this worksheet contains four problems:
#
# 123 * 45 * 6 = 33210
# 328 + 64 + 98 = 490
# 51 * 387 * 215 = 4243455
# 64 + 23 + 314 = 401
# To check their work, cephalopod students are given the grand total of adding together all of the answers to the individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.
#
# Of course, the actual worksheet is much wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.
#
# Solve the problems on the math worksheet. What is the grand total found by adding together all of the answers to the individual problems?
import operator

ops = {
    '+': operator.add,
    '*': operator.mul,
    '-': operator.sub,
    '/': operator.truediv
}


with open('numbers_list.txt', 'r') as f:
    # Read non-empty lines and strip whitespace
    rows = [line.strip().split('\n') for line in f if line.strip()]



# input_data = """
# 123 328 51 64
# 45 64 387 23
# 6 98 215 314
# * + * +
# """


# rows = [line.split() for line in input_data.strip().split('\n')]
operands_1 = [int(num) for num in rows[0][0].split()]
operands_2 = [int(num) for num in rows[1][0].split()]
operands_3 = [int(num) for num in rows[2][0].split()]
operands_4 = [int(num) for num in rows[3][0].split()]
operators = rows[4][0].split()

results = []
for i in range(len(operators)):
    result1 = ops[operators[i]](operands_1[i], operands_2[i])
    result2 = ops[operators[i]](result1, operands_3[i])
    result3 = ops[operators[i]](result2, operands_4[i])
    results.append(result3)

print(f'the sum of results of all operations is : {sum(results)}')
# the sum of results of all operations is : 5060053676136
