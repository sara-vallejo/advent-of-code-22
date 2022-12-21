
def read_input(file_path):
    with open(file_path) as f:
        return f.read().split("\n\n")


def parse_monkeys(monkeys_list):
    monkeys_dict = {}
    for monkey in monkeys_list:
        monkey_rows = monkey.splitlines()
        monkeys_dict[int(monkey_rows[0].split()[1][:-1])] = {
            "worries": [
                int(i) for i in monkey_rows[1].split(":")[1].split(",")
            ],
            "operation": monkey_rows[2].split("=")[1],
            "test": int(monkey_rows[3].split()[-1]),
            "test_output": {
                True: int(monkey_rows[4].split()[-1]),
                False: int(monkey_rows[5].split()[-1])
            },
            "inspected": 0
        }

    return monkeys_dict

def perform_rounds(monkeys_dict, relief=True, rounds=20):
    num_monkeys = len(monkeys_dict)
    round = 1
    while round <= rounds:
        if round%1000==0:
            print("Round:", round)
        for monkey_id in range(num_monkeys):
            monkey = monkeys_dict[monkey_id].copy()

            for old in monkey["worries"]:
                new_worry = eval(monkey["operation"])
                if relief:
                    new_worry = int(new_worry / 3)
                if new_worry % monkey["test"] == 0:
                    throw_to = monkey["test_output"][True]
                else:
                    throw_to = monkey["test_output"][False]

                monkeys_dict[throw_to]["worries"].append(new_worry)

            monkey["inspected"] += len(monkey["worries"])
            monkey["worries"] = []
            monkeys_dict[monkey_id] = monkey

        round += 1

    return monkeys_dict


def perform_rounds_new(monkeys_dict, relief=True, rounds=20):
    num_monkeys = len(monkeys_dict)
    round = 1
    while round <= rounds:
        if round%1000==0:
            print("Round:", round)
        for monkey_id in range(num_monkeys):
            monkey = monkeys_dict[monkey_id].copy()

            new_worries = [eval(monkey["operation"]) for old in monkey["worries"]]
            if relief:
                new_worries = [int(worry/3) for worry in new_worries]
            condition = [(worry % monkey["test"] == 0) for worry in new_worries]

            true_conditions = [i for (i, v) in zip(new_worries, condition) if v]
            monkeys_dict[monkey["test_output"][True]]["worries"].extend(
                true_conditions
            )
            false_conditions = [i for (i, v) in zip(new_worries, condition) if not v]
            monkeys_dict[monkey["test_output"][False]]["worries"].extend(
                false_conditions
            )

            monkey["inspected"] += len(monkey["worries"])
            monkey["worries"] = []
            monkeys_dict[monkey_id] = monkey

        round += 1

    return monkeys_dict


def part1(file_path):
    monkeys_list = read_input(file_path)
    monkeys_dict = parse_monkeys(monkeys_list)
    monkeys_dict = perform_rounds_new(monkeys_dict)

    inspected_items = []
    for monkey in monkeys_dict.values():
        inspected_items.append(monkey["inspected"])

    inspected_items.sort()

    return inspected_items[-1]*inspected_items[-2]


def part2(file_path):
    monkeys_list = read_input(file_path)
    monkeys_dict = parse_monkeys(monkeys_list)
    monkeys_dict = perform_rounds_new(monkeys_dict, relief=False, rounds=10000)

    inspected_items = []
    for monkey in monkeys_dict.values():
        inspected_items.append(monkey["inspected"])

    inspected_items.sort()

    return inspected_items[-1]*inspected_items[-2]


if __name__ == "__main__":
    print("Part 1")
    print(part1("input.txt"))
    print()

    print("Part 2")
    print(part2("input.txt"))
    print()











