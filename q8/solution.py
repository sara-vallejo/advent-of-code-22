
def read_input(file_path):
    with open(file_path) as f:
        file_as_list = f.read().splitlines()
    return file_as_list


def get_quadcopter(file_list):
    return list(map(lambda x: list(map(int, list(x))), file_list))


def check_visible(side_1, side_2, height):
    return all(i<height for i in side_1) or all(i<height for i in side_2)


def count_visible_trees(quadcopter):
    num_rows = len(quadcopter)
    num_cols = len(quadcopter[0])
    num_visible = 2*num_rows + (num_cols-2)*2

    for row_num, row in enumerate(quadcopter):
        if row_num not in [0, num_rows-1]:
            for col, tree_height in enumerate(row):
                if col not in [0, num_cols-1]:
                    if check_visible(row[:col], row[col+1:], tree_height):
                        num_visible += 1
                    else:
                        col_up = list(map(lambda x: x[col], quadcopter[:row_num]))
                        col_down = list(map(lambda x: x[col], quadcopter[row_num+1:]))
                        if check_visible(col_up, col_down, tree_height):
                            num_visible += 1
    return num_visible


def get_num_trees_side(side, height):
    num_trees = 0
    if not side:
        return 1

    for i in side:
        if i < height:
            num_trees += 1
        elif i >= height:
            return num_trees + 1
    return num_trees


def get_scenic_views(quadcopter):
    scenic_views = []
    for row_num, row in enumerate(quadcopter):
        for col_num, col in enumerate(row):
            view = (
                get_num_trees_side(list(reversed(row[:col_num])), col) *
                get_num_trees_side(row[col_num+1:], col) *
                get_num_trees_side(
                    list(reversed(list(map(lambda x: x[col_num], quadcopter[:row_num])))),
                    col
                ) *
                get_num_trees_side(
                    list(map(lambda x: x[col_num], quadcopter[row_num+1:])),
                    col
                )
            )
            scenic_views.append(view)
    return scenic_views


def part1(file_path):
    quadcopter = get_quadcopter(read_input(file_path))
    return count_visible_trees(quadcopter)


def part2(file_path):
    quadcopter = get_quadcopter(read_input(file_path))
    return max(get_scenic_views(quadcopter))


if __name__ == "__main__":
    print("Part 1")
    print("Number of visible trees", part1("input.txt"))
    print()

    print("Part 2")
    print("Best scenic view", part2("input.txt"))
    print()