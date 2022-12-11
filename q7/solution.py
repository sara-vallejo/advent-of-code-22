

def read_input(file_path):
    with open(file_path) as f:
        return f.read().splitlines()


class DirectoryNode:
    def __init__(self, parent, name, node_type, size):
        self. parent = parent
        self. name = name
        self.node_type = node_type
        self.size = size

        if self.node_type == "dir":
            self.children = {}
            self.dir_size = -1

    def add_child(self, node):
        self.children[node.name] = node


def create_file_system(file_list):
    if file_list[0][:4] != "$ cd":
        raise ValueError("Please indicate initial directory")
    else:
        outermost_name = file_list[0].split()[-1]
        outermost_node = DirectoryNode(None, outermost_name, "dir", 0)

    current_node = outermost_node
    for line in file_list[1:]:
        if line.startswith("$ ls"):
            continue
        elif line.startswith("$ cd"):
            next_directory = line.split()[-1]
            if next_directory == "/":
                current_node = outermost_node
            elif next_directory == "..":
                current_node = current_node.parent
            else:
                if next_directory in current_node.children.keys():
                    current_node = current_node.children[next_directory]
                else:
                    raise ValueError("Directory specified not in current directory")
        elif line.startswith("dir"):
            current_node.add_child(
                DirectoryNode(current_node, line.split()[-1], "dir", 0)
            )
        else:
            size, name = line.split()
            current_node.add_child(
                DirectoryNode(current_node, name, "file", int(size))
            )
    return outermost_node


def get_directory_size(node):
    if node.node_type == "file":
        return node.size
    else:
        if node.dir_size == -1:
            dir_size = 0
            for child in node.children.values():
                dir_size += get_directory_size(child)
            node.dir_size = dir_size
            return node.dir_size


def sum_total_size(node, thr):
    total_size = 0

    if node.node_type == "dir":
        if node.dir_size <= thr:
            total_size += node.dir_size
    if node.node_type == "file":
        return 0
    for child in node.children.values():
        total_size += sum_total_size(child, thr)

    return total_size


def smallest_dir_to_delete(node, min_size, size_to_delete):
    if node.node_type == "dir":
        if node.dir_size >= min_size:
            if size_to_delete == -1 or node.dir_size < size_to_delete:
                size_to_delete = node.dir_size

    if node.node_type == "dir":
        for child in node.children.values():
            size_to_delete = smallest_dir_to_delete(child, min_size, size_to_delete)

    return size_to_delete


def part1(file_path):
    file_list = read_input(file_path)
    outermost_dir = create_file_system(file_list)
    get_directory_size(outermost_dir)
    return sum_total_size(outermost_dir, 100000)


def part2(file_path):
    file_list = read_input(file_path)
    outermost_dir = create_file_system(file_list)
    get_directory_size(outermost_dir)
    to_delete = outermost_dir.dir_size - (70000000-30000000)

    return smallest_dir_to_delete(outermost_dir, to_delete, -1)


if __name__ == "__main__":
    print("Part 1")
    print("TOTAL SIZE: ", part1("input.txt"))
    print()

    print("Part 2")
    print("SIZE OF DIRECTORY TO DELETE: ", part2("input.txt"))
    print()