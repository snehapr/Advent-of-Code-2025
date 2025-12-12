
# ---Part Two ---

# You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while you think.
#
# As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:
#
# "Due to newer security protocols, please use password method 0x434C49434B until further notice."
#
# You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.
#
# Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:
#
# The dial starts by pointing at 50.
# The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
# The dial is rotated L30 to point at 52.
# The dial is rotated R48 to point at 0.
# The dial is rotated L5 to point at 95.
# The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
# The dial is rotated L55 to point at 0.
# The dial is rotated L1 to point at 99.
# The dial is rotated L99 to point at 0.
# The dial is rotated R14 to point at 14.
# The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
# In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation. So, in this example, the new password would be 6.
#
# Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!



with open('rotations.txt', 'r') as f:
    rotations = [line.strip() for line in f if line.strip()]

# rotations = [
#     'L68',
#     'L30',
#     'R48',
#     'L5',
#     'R60',
#     'L55',
#     'L1',
#     'L99',
#     'R14',
#     'L82'
# ]

start_point = 50
password = 0


# def get_password(start_point, rotation, distance, password):
#     crosses = 0
#     if rotation == 'L':
#         start_point = (start_point - distance) % 100
#     elif rotation == 'R':
#         start_point = (start_point + distance) % 100
#     if start_point == 0:
#         password += 1
#     return password, start_point

def get_password(start_point, rotation, distance, password):
    passed_zero = False

    if rotation == 'L':
        for i in range(1, distance + 1):
            pos = (start_point - i) % 100
            if pos == 0:
                password += 1
                passed_zero = True
        start_point = (start_point - distance) % 100
    elif rotation == 'R':
        for i in range(1, distance + 1):
            pos = (start_point + i) % 100
            if pos == 0:
                password += 1
                passed_zero = True
        start_point = (start_point + distance) % 100

    # If landed on 0 and did NOT pass 0 during the move, count it
    if start_point == 0 and not passed_zero:
        password += 1

    return password, start_point


for code in rotations:
    direction = code[0]
    distance = int(code[1:])
    password, start_point = get_password(start_point, direction, distance, password)
    # print("The password is:", password)
    # print('The current dial position is:', start_point)
    # is_available = input("Do you want to continue? (yes/no): ").lower()
    # if is_available == 'no':
    #     is_available = False

print("The final password is:", password)
# The final password is: 6133



print('Break')