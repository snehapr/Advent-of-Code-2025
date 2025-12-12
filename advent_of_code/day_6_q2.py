# --- Part Two ---

# The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.
#
# Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)
#
# Here's the example worksheet again:
#
# 123 328  51 64
# 45 64  387 23
# 6 98  215 314
# *   +   *   +
# Reading the problems right-to-left one column at a time, the problems are now quite different:
#
# The rightmost problem is 4 + 431 + 623 = 1058
# The second problem from the right is 175 * 581 * 32 = 3253600
# The third problem from the right is 8 + 248 + 369 = 625
# Finally, the leftmost problem is 356 * 24 * 1 = 8544
# Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.
#
# Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?

# worksheet = [
#     "123 328  51 64 ",
#     " 45 64  387 23 ",
#     "  6 98  215 314",
#     "*   +   *   +  "
# ]

def parse_worksheet(lines):
    maxlen = max(len(line) for line in lines)
    lines = [line.rstrip('\n').ljust(maxlen) for line in lines]
    cols = list(zip(*[list(line) for line in lines]))
    cols = cols[::-1]
    problems = []
    current_problem = []
    for col in cols:
        if all(c == ' ' for c in col):
            if current_problem:
                problems.append(current_problem)
                current_problem = []
        else:
            current_problem.append(col)
    if current_problem:
        problems.append(current_problem)
    return problems

def solve_problem(problem_cols):
    digits_per_col = []
    for col in problem_cols:
        digits = ''.join(col[:-1]).replace(' ', '')
        digits_per_col.append(digits if digits else '0')
    operator = problem_cols[-1][-1]
    numbers = [int(col) for col in digits_per_col]
    if operator == '+':
        return sum(numbers)
    elif operator == '*':
        prod = 1
        for n in numbers:
            prod *= n
        return prod
    else:
        raise ValueError(f"Unknown operator: {operator}")

# Read from file
with open('numbers_list.txt', 'r') as f:
    worksheet = [line.rstrip('\n') for line in f]

problems = parse_worksheet(worksheet)
for problem_cols in problems:
    digits_per_col = [''.join(col[:-1]).replace(' ', '') for col in problem_cols]
    operator = problem_cols[-1][-1]
    print(f"Digits: {digits_per_col}, Operator: {operator}")
answers = [solve_problem(problem_cols) for problem_cols in problems]
print("Answers:", answers)
print("Grand Total:", sum(answers))
# Grand Total: 9695042567249