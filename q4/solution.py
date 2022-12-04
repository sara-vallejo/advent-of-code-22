

def read_input(file_path):
    with open(file_path) as f:
        file_as_list = f.read().splitlines()
    return file_as_list

def get_sections(assignment):
    start, end = assignment.split("-")
    return set(list(range(int(start), int(end) + 1 )))


def check_if_contained(pair):
    assignments = pair.split(",")
    sections = [get_sections(x) for x in assignments]
    return (sections[0].issubset(sections[1]) or sections[1].issubset(sections[0]))


def check_if_overlap(pair):
    assignments = pair.split(",")
    sections = [get_sections(x) for x in assignments]
    return (not sections[0].isdisjoint(sections[1]))


def get_fully_contained(file_path):
    item_list = read_input(file_path)
    fully_contained = list(map(check_if_contained, item_list))
    return sum(fully_contained)


def get_overlap(file_path):
    item_list = read_input(file_path)
    overlap = list(map(check_if_overlap, item_list))
    return sum(overlap)


if __name__ == "__main__":
    print("Part 1")
    print("TOTAL FULLY CONTAINED: ", get_fully_contained("input.txt"))
    print()

    print("Part 1")
    print("TOTAL OVERLAPPING: ", get_overlap("input.txt"))
    print()