
def read_input(file_path):
    with open(file_path) as f:
        return f.read().splitlines()


def get_neighbours(pos, total_rows, total_cols):
    pos_up = (pos[0], pos[1]+1)
    pos_down = (pos[0], pos[1]-1)
    pos_r = (pos[0] + 1, pos[1])
    pos_l = (pos[0] - 1, pos[1])

    neighbours = []
    for position in [pos_up, pos_down, pos_r, pos_l]:
        if position[0]>=0 and position[1]>=0:
            if position[0]< total_rows and position[1]< total_cols:
                neighbours.append(position)

    return neighbours


def run_solution(file_path, part):
    file_list = read_input(file_path)
    heightmap_chars = [[i for i in row] for row in file_list]

    total_rows = len(heightmap_chars)
    total_cols = len(heightmap_chars[0])
    for row_num, row in enumerate(heightmap_chars):
        for col_num, col in enumerate(row):
            if col == "S":
                starting_position = (abs(row_num-total_rows+1), col_num)
            elif col == "E":
                end_position = (abs(row_num-total_rows+1), col_num)

    heightmap = [[ord(char)-96 for char in row] for row in heightmap_chars]
    map_dict = {}
    for i, row in enumerate(heightmap):
        for j, col in enumerate(row):
            map_dict[(abs(i-total_rows+1),j)] = {
                "height": col,
                "distance": 999
            }

    map_dict[end_position]["distance"] = 0
    map_dict[end_position]["height"] = ord("z")-96
    map_dict[starting_position]["height"] = ord("a")-96

    pos_to_visit = [end_position]
    while len(pos_to_visit) > 0:
        pos = pos_to_visit.pop(0)
        neighbours = get_neighbours(pos,total_rows, total_cols)
        for neighbour in neighbours:
            if (
                    (map_dict[neighbour]["height"] >= map_dict[pos]["height"]-1) and
                    (map_dict[neighbour]["distance"] > map_dict[pos]["distance"]+1)
            ):
                map_dict[neighbour]["distance"] = map_dict[pos]["distance"]+1
                pos_to_visit.append(neighbour)

    if part == 1:
        return map_dict[starting_position]["distance"]

    elif part == 2:
        shortest_distance = 999
        for info in map_dict.values():
            if info["height"] == 1:
                if info["distance"] < shortest_distance:
                    shortest_distance = info["distance"]
        return shortest_distance



if __name__ == "__main__":
    print("Part 1")
    print(run_solution("input.txt", part=1))
    print()

    print("Part 2")
    print(run_solution("input.txt", part=2))
    print()


