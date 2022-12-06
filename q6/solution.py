

def read_input(file_path):
    with open(file_path) as f:
        file_as_list = f.read()
    return file_as_list


def get_marker_position(file_path, marker_length):
    signal = read_input(file_path)

    i = 0
    chars = set(signal[i:i+marker_length])
    while len(chars) < marker_length:
        i += 1
        chars = set(signal[i:i+marker_length])

    return i+marker_length


if __name__ == "__main__":
    print("Part 1")
    print("SOLUTION: ", get_marker_position("input.txt", 4))
    print()

    print("Part 2")
    print("SOLUTION: ", get_marker_position("input.txt", 14))
    print()

