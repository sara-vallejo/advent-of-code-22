import string


def read_input(file_path):
    with open(file_path) as f:
        file_as_list = f.read().splitlines()
    return file_as_list

def get_priorities():
    alpha_dict_lower = {k: num + 1 for num, k in enumerate(string.ascii_lowercase)}
    alpha_dict_upper = {k: num + 27 for num, k in enumerate(string.ascii_uppercase)}
    return {**alpha_dict_lower, **alpha_dict_upper}

def get_item_repeated(rucksack):
    num_items = len(rucksack)

    compartment1 = set(rucksack[:int(num_items/2)])
    compartment2 = set(rucksack[int(num_items/2):])

    return list(compartment1.intersection(compartment2))[0]

def get_sum_of_priorities_p1(file_path):
    item_list = read_input(file_path)

    alpha_dict = get_priorities()

    repeated_item = list(map(get_item_repeated, item_list))
    priority_list = list(map(lambda x: alpha_dict[x], repeated_item))
    return sum(priority_list)


def get_group_badge(r1, r2, r3):
    return list(set(r1).intersection(set(r2).intersection(r3)))[0]

def get_sum_of_priorities_p2(file_path):
    item_list = read_input(file_path)

    alpha_dict = get_priorities()

    group_badges = []
    for i in range(int(len(item_list)/3)):
        group_badges.append(get_group_badge(*item_list[3*i : 3*i+3]))

    priority_list = list(map(lambda x: alpha_dict[x], group_badges))

    return sum(priority_list)


if __name__ == "__main__":
    print("Part 1")
    print("TOTAL PRIORITY: ", get_sum_of_priorities_p1("input.txt"))
    print()

    print("Part 2")
    print("TOTAL PRIORITY: ", get_sum_of_priorities_p2("input.txt"))
    print()


