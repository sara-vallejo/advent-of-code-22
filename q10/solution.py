
def read_input(file_path):
    with open(file_path) as f:
        return f.read().splitlines()



def part1(file_path):
    instructions = read_input(file_path)
    cycles_to_compute = [20,60,100,140,180,220]

    current_cycle = 0
    X = 1
    cycle_X = {}
    for instruction in instructions:
        if instruction == "noop":
            current_cycle += 1
            cycle_X[current_cycle] = X
        else:
            current_cycle += 1
            cycle_X[current_cycle] = X
            current_cycle += 1
            cycle_X[current_cycle] = X
            V = int(instruction.split(" ")[-1])
            X += V

    strenghts = []
    for cycle in cycles_to_compute:
        strenghts.append(cycle*cycle_X[cycle])

    return sum(strenghts)


def draw_CRT(current_row, CRT_pos, X):
    if CRT_pos in [X - 1, X, X + 1]:
        current_row.append("#")
    else:
        current_row.append(".")
    return current_row

def check_if_change_row(CRT_pos, myimage, current_row):
    if CRT_pos == 40 or (CRT_pos == 39 and len(myimage) == 5):
        myimage.append(current_row)
        CRT_pos = 0
        current_row = []
    return CRT_pos, myimage, current_row


def part2(file_path):
    instructions = read_input(file_path)

    myimage = []
    current_cycle = 0
    current_row = []
    CRT_pos = 0
    X = 1
    for instruction in instructions:
        CRT_pos, myimage, current_row = check_if_change_row(CRT_pos, myimage, current_row)
        if instruction == "noop":
            current_cycle += 1
            current_row = draw_CRT(current_row, CRT_pos, X)
            CRT_pos += 1
        else:
            current_cycle += 1
            current_row = draw_CRT(current_row, CRT_pos, X)
            CRT_pos += 1

            CRT_pos, myimage, current_row = check_if_change_row(CRT_pos, myimage, current_row)

            current_cycle += 1
            current_row = draw_CRT(current_row, CRT_pos, X)
            CRT_pos += 1

            X += int(instruction.split(" ")[-1])

    return myimage


if __name__ == "__main__":
    print("Part 1")
    print(part1("input.txt"))
    print()

    print("Part 2")
    myimage = part2("input.txt")
    for row in myimage:
        print(row)
    print()

