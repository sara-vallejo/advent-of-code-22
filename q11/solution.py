import numpy as np

def read_input(file_path):
    with open(file_path) as f:
        return f.read().split("\n\n")


def parse_monkeys(monkeys_list):
    monkeys_dict = {}
    for monkey in monkeys_list:
        monkey_rows = monkey.splitlines()
        monkeys_dict[int(monkey_rows[0].split()[1][:-1])] = {
            "worries": np.array([
                int(i) for i in monkey_rows[1].split(":")[1].split(",")
            ], dtype='int64'),
            "operation": monkey_rows[2].split("=")[1],
            "test": int(monkey_rows[3].split()[-1]),
            "test_output": {
                True: int(monkey_rows[4].split()[-1]),
                False: int(monkey_rows[5].split()[-1])
            },
            "inspected": 0
        }

    return monkeys_dict


def perform_rounds_new(monkeys_dict, relief=True, rounds=20):
    num_monkeys = len(monkeys_dict)
    round = 1
    while round <= rounds:
        for monkey_id in range(num_monkeys):
            monkey = monkeys_dict[monkey_id].copy()

            new_worries = np.array(
                [eval(monkey["operation"]) for old in monkey["worries"]], dtype='int32'
            )
            if relief:
                new_worries = new_worries//3
            condition = new_worries % monkey["test"] == 0

            true_conditions = new_worries[condition]
            monkeys_dict[monkey["test_output"][True]]["worries"] = np.append(
                monkeys_dict[monkey["test_output"][True]]["worries"], true_conditions
            )
            false_conditions = new_worries[~condition]
            monkeys_dict[monkey["test_output"][False]]["worries"] = np.append(
                monkeys_dict[monkey["test_output"][False]]["worries"], false_conditions
            )

            monkey["inspected"] += len(monkey["worries"])
            monkey["worries"] = np.array([], dtype='int64')
            monkeys_dict[monkey_id] = monkey.copy()

        if round%1000==0 or round ==20:
            print("Round:", round)
            print("monkey 0:", monkeys_dict[0]["inspected"])
            print("monkey 1:", monkeys_dict[1]["inspected"])
            print("monkey 2:", monkeys_dict[2]["inspected"])
            print("monkey 3:", monkeys_dict[3]["inspected"])
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
    print(part1("dummy.txt"))
    print()

    print("Part 2")
    print(part2("input.txt"))
    print()











