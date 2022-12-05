
def read_input(file_path):
    with open(file_path) as f:
        file_as_list = f.read().splitlines()
    return file_as_list


def split_drawing_instructions(file_list):
    for i, row in enumerate(file_list):
        if row == "":
            return file_list[:i], file_list[i+1:]


def transform_stack_levels(level):
    level_split = level.split(" ")
    transformed_level = []
    i = 0
    while i < len(level_split):
        letter = level_split[i]
        if letter == "":
            i += 4
            transformed_level.append("")
        else:
            i += 1
            transformed_level.append(letter[1])
    return transformed_level


def get_stacks(drawing):

    num_stacks = int(drawing[-1].split(" ")[-2])

    transformed_drawing = list(map(transform_stack_levels, drawing[:-1]))
    stacks = {i+1: [] for i in range(num_stacks)}
    for level in reversed(transformed_drawing):
        for i in range(num_stacks):
            letter = level[i]
            if letter != "":
                stacks[i+1].append(letter)
    return stacks


def clean_instruction(instruction):
    split_instructions = instruction.split(" ")
    return {"from": int(split_instructions[3]), "to": int(split_instructions[5]), "num": int(split_instructions[1])}


def do_move(stacks, instruction, reverse):
    to_move = stacks[instruction["from"]][-instruction["num"]:]
    stacks[instruction["from"]] = stacks[instruction["from"]][:-instruction["num"]]
    if reverse:
        stacks[instruction["to"]] += list(reversed(to_move))
    else:
        stacks[instruction["to"]] += to_move
    return stacks


def get_top_of_each_stack(file_path, reverse):
    file_list = read_input(file_path)
    drawing, instructions = split_drawing_instructions(file_list)

    stacks = get_stacks(drawing)

    instructions = list(map(clean_instruction, instructions))
    for move in instructions:
        stacks = do_move(stacks, move, reverse)

    top_of_stacks = ""
    for stack in stacks.values():
        top_of_stacks += stack[-1]
    return top_of_stacks


if __name__ == "__main__":
    print("Part 1")
    print("TOP OF STACKS: ", get_top_of_each_stack("input.txt", reverse=True))
    print()

    print("Part 2")
    print("TOP OF STACKS: ", get_top_of_each_stack("input.txt", reverse=False))
    print()

