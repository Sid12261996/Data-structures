class Tree:

    def __init__(self, data):
        self.parent = None
        self.children = []
        self.data = data

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_my_level(self):
        level = 1
        if self.parent:
            level += self.parent.get_my_level()
        return level

    def print_tree(self):
        prefix = "-" * self.get_my_level() * 4
        print(prefix + "|" + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_my_tree():
    sumit = Tree("Sumit Gupta")
    sid = Tree("Sid")
    harsh = Tree("Harsh")
    neetan = Tree("Neetan")
    sumit.add_child(sid)
    sumit.add_child(harsh)
    sumit.add_child(neetan)
    intern1 = Tree("Intern1")
    sid.add_child(intern1)
    harsh.add_child(Tree("Intern2"))
    sumit.print_tree()
    return sumit


if __name__ == '__main__':
    root = build_my_tree()
    # print(root.get_my_level())
