class Binary_Tree:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

    def add_child(self, child):
        if child.data < self.data:
            self.left_child = self.inside_insert(child, self.left_child)
        else:
            self.right_child = self.inside_insert(child, self.right_child)

    def inside_insert(self, to_insert, existing_node):
        if existing_node:
            existing_node.add_child(to_insert)
        else:
            existing_node = to_insert
            existing_node.parent = self
        return existing_node

    def get_my_level(self):
        level = 1
        if self.parent:
            level += self.parent.get_my_level()
        return level

    def print_tree(self):
        prefix = "-" * self.get_my_level() * 4
        print(prefix + "|" + str(self.data))
        if self.left_child:
            self.left_child.print_tree()
        if self.right_child:
            self.right_child.print_tree()


def build_my_binary_tree():
    root = Binary_Tree(30)
    insert_array = [10, 20, 40, 50, 3, 70, 7, 12, 18]
    for arr in insert_array:
        root.add_child(Binary_Tree(arr))
    root.print_tree()
    return root


if __name__ == '__main__':
    root = build_my_binary_tree()
