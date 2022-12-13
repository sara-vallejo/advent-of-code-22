
def read_input(file_path):
    with open(file_path) as f:
        return f.read().splitlines()


def move_head(pos, motion):
    if motion == "R":
        pos[0] += 1
    elif motion == "L":
        pos[0] -= 1
    elif motion == "U":
        pos[1] += 1
    elif motion == "D":
        pos[1] -= 1
    return pos


def get_tail_pos(head_pos, tail_pos):
    if (abs(head_pos[0] - tail_pos[0]) in [0,1]) and (abs(head_pos[1] - tail_pos[1]) in [0,1]):
        return tail_pos
    elif head_pos[0] == tail_pos[0]:
        if (head_pos[1] - tail_pos[1]) > 1:
            tail_pos[1] += 1
        else:
            tail_pos[1] -= 1
    elif head_pos[1] == tail_pos[1]:
        if (head_pos[0] - tail_pos[0]) > 1:
            tail_pos[0] += 1
        else:
            tail_pos[0] -= 1
    elif head_pos[0] > tail_pos[0]:
        if head_pos[1] > tail_pos[1]:
            tail_pos[0] += 1
            tail_pos[1] += 1
        else:
            tail_pos[0] += 1
            tail_pos[1] -= 1
    else:
        if head_pos[1] > tail_pos[1]:
            tail_pos[0] -= 1
            tail_pos[1] += 1
        else:
            tail_pos[0] -= 1
            tail_pos[1] -= 1

    return tail_pos


def perform_move(knots_pos, move, num_knots):
    tail_positions = []
    motion, num = move.split(" ")
    for j in range(int(num)):
        knots_pos[0] = move_head(knots_pos[0], motion)
        for i in range(num_knots-1):
            knots_pos[i+1] = get_tail_pos(knots_pos[i], knots_pos[i+1])
        tail_positions.append(knots_pos[num_knots-1][:])
    return knots_pos, tail_positions


def part1(file_path):
    motions = read_input(file_path)
    knots_pos = {0: [0,0], 1: [0,0]}
    tail_positions = [knots_pos[1][:]]
    for move in motions:
        knots_pos, move_tail_positions = perform_move(knots_pos, move, 2)
        tail_positions.extend(move_tail_positions)
    return len(set(tuple(x) for x in tail_positions))


def part2(file_path, num_knots=10):
    motions = read_input(file_path)
    knots_pos = {}
    for i in range(num_knots):
        knots_pos[i] = [0,0]

    tail_positions = [knots_pos[num_knots-1][:]]
    for move in motions:
        knots_pos, move_tail_positions = perform_move(knots_pos, move, num_knots)
        tail_positions.extend(move_tail_positions)
    return len(set(tuple(x) for x in tail_positions))


if __name__ == "__main__":
    print("Part 1")
    print("Number of tail positions", part1("input.txt"))
    print()

    print("Part 2")
    print("Number of tail positions", part2("input.txt"))
    print()

