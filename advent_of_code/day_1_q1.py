# --- Day 1: Secret Entrance ---

# The Elves have good news and bad news.
#
# The good news is that they've discovered project management! This has given them the tools they need to prevent their usual Christmas emergency. For example, they now know that the North Pole decorations need to be finished soon so that other critical tasks can start on time.
#
# The bad news is that they've realized they have a different emergency: according to their resource planning, none of them have any time left to decorate the North Pole!
#
# To save Christmas, the Elves need you to finish decorating the North Pole by December 12th.
#
# Collect stars by solving puzzles. Two puzzles will be made available on each day; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
#
# You arrive at the secret entrance to the North Pole base ready to start decorating. Unfortunately, the password seems to have been changed, so you can't get in. A document taped to the wall helpfully explains:
#
# "Due to new security protocols, the password is locked in the safe below. Please see the attached document for the new combination."
#
# The safe has a dial with only an arrow on it; around the dial are the numbers 0 through 99 in order. As you turn the dial, it makes a small click noise as it reaches each number.
#
# The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe. A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.
#
# So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19 would cause it to point at 0.
#
# Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0.
#
# So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5 could cause it to point at 0.
#
# The dial starts by pointing at 50.
#
# You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.




with open('rotations.txt', 'r') as f:
    rotations = [line.strip() for line in f if line.strip()]

start_point = 50
password = 0


def get_password(start_point, rotation, distance, password):
    if rotation == 'L':
        start_point = (start_point - distance) % 100
    elif rotation == 'R':
        start_point = (start_point + distance) % 100
    if start_point == 0:
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
# The final password is: 992



print('Break')



