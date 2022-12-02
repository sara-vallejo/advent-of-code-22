outcome_points = {"W": 6, "D": 3,"L": 0,}
shape_points = {"R": 1, "P": 2, "S": 3,}
converter_1 = {"A": "R", "B": "P", "C": "S", "X": "R", "Y": "P", "Z": "S"}
converter_2 = {"A": "R", "B": "P", "C": "S", "X": "L", "Y": "D", "Z": "W"}
outcome_rules = {
    "R S": "L",
    "S R": "W",
    "S P": "L",
    "P S": "W",
    "P R": "L",
    "R P": "W",
    "R R": "D",
    "S S": "D",
    "P P": "D",
}
move_needed = {
    "R L": "S",
    "R D": "R",
    "R W": "P",
    "S L": "P",
    "S D": "S",
    "S W": "R",
    "P L": "R",
    "P D": "P",
    "P W": "S",
}

def read_input(file_path):
    with open(file_path) as f:
        file_as_list = f.read().splitlines()
    return file_as_list

def convert_names(round, converter):
    for key, value in converter.items():
        round = round.replace(key, value)
    return round


def get_my_total_score_part_1(file_path):
    strategy_guide = read_input(file_path)
    strategy_guide = list(map(lambda x: convert_names(x, converter_1), strategy_guide))

    my_outcome = list(map(lambda x: outcome_rules[x], strategy_guide))
    my_outcome_points = list(map(lambda x: outcome_points[x], my_outcome))
    my_shape_points = list(map(lambda x: shape_points[x[-1]], strategy_guide))

    return sum(my_outcome_points) + sum(my_shape_points)


def get_my_total_score_part_2(file_path):
    strategy_guide = read_input(file_path)
    strategy_guide = list(map(lambda x: convert_names(x, converter_2), strategy_guide))

    my_outcome_points = list(map(lambda x: outcome_points[x[-1]], strategy_guide))
    my_shape = list(map(lambda x: move_needed[x], strategy_guide))
    my_shape_points = list(map(lambda x: shape_points[x], my_shape))

    return sum(my_outcome_points) + sum(my_shape_points)


if __name__ == "__main__":
    print("Part 1")
    print("TOTAL SCORE: ", get_my_total_score_part_1("input.txt"))
    print()

    print("Part 2")
    print("TOTAL SCORE: ", get_my_total_score_part_2("input.txt"))
    print()

