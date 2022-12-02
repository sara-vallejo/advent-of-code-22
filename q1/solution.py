
def read_input(file_path):
    with open(file_path) as f:
        file_as_list = f.read().splitlines()
    return file_as_list


def get_sum_calories(file_path):
    list_elves = read_input(file_path)

    curr_cals = 0
    all_cals = []
    for i in list_elves:
        if len(i) == 0:
            all_cals.append(curr_cals)
            curr_cals = 0
        else:
            curr_cals += int(i)

    return all_cals


if __name__ == "__main__":
    list_cals = get_sum_calories("input.txt")
    list_cals.sort(reverse=True)
    print("Part 1")
    print("max calories is: ", list_cals[0])
    print()
    print("Part 2")
    print("Sum highest 3 calories:", sum(list_cals[:3]))
