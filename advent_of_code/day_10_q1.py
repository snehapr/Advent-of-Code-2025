# --- Day 10: Factory ---
# Just across the hall, you find a large factory. Fortunately, the Elves here have plenty of time to decorate. Unfortunately, it's because the factory machines are all offline, and none of the Elves can figure out the initialization procedure.
#
# The Elves do have the manual for the machines, but the section detailing the initialization procedure was eaten by a Shiba Inu. All that remains of the manual are some indicator light diagrams, button wiring schematics, and joltage requirements for each machine.
#
# For example:
#
# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
# The manual describes one machine per line. Each line contains a single indicator light diagram in [square brackets], one or more button wiring schematics in (parentheses), and joltage requirements in {curly braces}.
#
# To start a machine, its indicator lights must match those shown in the diagram, where . means off and # means on. The machine has the number of indicator lights shown, but its indicator lights are all initially off.
#
#                                                                                               So, an indicator light diagram like [.##.] means that the machine has four indicator lights which are initially off and that the goal is to simultaneously configure the first light to be off, the second light to be on, the third to be on, and the fourth to be off.
#
# You can toggle the state of indicator lights by pushing any of the listed buttons. Each button lists which indicator lights it toggles, where 0 means the first light, 1 means the second light, and so on. When you push a button, each listed indicator light either turns on (if it was off) or turns off (if it was on). You have to push each button an integer number of times; there's no such thing as "0.5 presses" (nor can you push a button a negative number of times).
#
# So, a button wiring schematic like (0,3,4) means that each time you push that button, the first, fourth, and fifth indicator lights would all toggle between on and off. If the indicator lights were [#.....], pushing the button would change them to be [...##.] instead.
#
#     Because none of the machines are running, the joltage requirements are irrelevant and can be safely ignored.
#
# You can push each button as many times as you like. However, to save on time, you will need to determine the fewest total presses required to correctly configure all indicator lights for all machines in your list.
#
# There are a few ways to correctly configure the first machine:
#
#     [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
#     You could press the first three buttons once each, a total of 3 button presses.
# You could press (1,3) once, (2,3) once, and (0,1) twice, a total of 4 button presses.
# You could press all of the buttons except (1,3) once each, a total of 5 button presses.
# However, the fewest button presses required is 2. One way to do this is by pressing the last two buttons ((0,2) and (0,1)) once each.
#
# The second machine can be configured with as few as 3 button presses:
#
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
#  One way to achieve this is by pressing the last three buttons ((0,4), (0,1,2), and (1,2,3,4)) once each.
#
# The third machine has a total of six indicator lights that need to be configured correctly:
#
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
# The fewest presses required to correctly configure it is 2; one way to do this is by pressing buttons (0,3,4) and (0,1,2,4,5) once each.
#
# So, the fewest button presses required to correctly configure the indicator lights on all of the machines is 2 + 3 + 2 = 7.
#
# Analyze each machine's indicator light diagram and button wiring schematics. What is the fewest button presses required to correctly configure the indicator lights on all of the machines?

from itertools import product

def parse_machine(line):
    indicator = line.split('[')[1].split(']')[0]
    target = [1 if c == '#' else 0 for c in indicator]
    buttons = []
    for part in line.split(']')[1].split('{')[0].split('(')[1:]:
        btn = part.split(')')[0]
        buttons.append([int(x) for x in btn.split(',') if x.strip() != ''])
    return target, buttons

def min_presses(target, buttons):
    n = len(target)
    m = len(buttons)
    matrix = [[0]*m for _ in range(n)]
    for j, btn in enumerate(buttons):
        for i in btn:
            matrix[i][j] = 1
    min_press = None
    for presses in product([0,1], repeat=m):
        state = [0]*n
        for j, press in enumerate(presses):
            if press:
                for i in range(n):
                    if matrix[i][j]:
                        state[i] ^= 1
        if state == target:
            total = sum(presses)
            if min_press is None or total < min_press:
                min_press = total
    return min_press if min_press is not None else -1

def solve(filename):
    total = 0
    with open(filename, 'r') as f:
        machines = [line.strip() for line in f if line.strip()]
    for line in machines:
        target, buttons = parse_machine(line)
        presses = min_presses(target, buttons)
        print(f"Machine: {line}\n  Fewest presses: {presses}\n")
        total += presses
    print(f"Total fewest presses for all machines: {total}")
    return total

# Run the solver on machines.txt
solve('machines_initial.txt')
# Total fewest presses for all machines: 535