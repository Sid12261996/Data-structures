
class Trie:
    def __init__(self):
        self.children: dict = {}
        self.common_prefix = ''

    def get_node(self, s: str) -> {}:
        # print('range:' + s)
        if s not in self.children.keys():
            return None
        return self.children[s]

    def set_node(self, s: str, node: {}) -> None:
        self.children[s] = node

    def add_node(self, s: str) -> None:
        self.inner_add_node(s, 0)

    def inner_add_node(self, s: str, index: int) -> None:
        if len(s) is index:
            self.children['*'] = Trie()
            return
        current = s[index]
        child = self.get_node(current)
        if child is None:
            child = Trie()
            self.set_node(current, child)

        child.inner_add_node(s, index + 1)

    def print_node(self):
        # print('Nodes: {}'.format(self.children.keys()))
        for child in self.children.keys():
            print('Nodes--> {}'.format(child))
            self.children[child].print_node()

    def find_longest_common_prefix(self):
        if len(self.children.keys()) == 1:
            for child in self.children.keys():
                self.common_prefix += child + self.children[child].find_longest_common_prefix()
                # print(child)

        return self.common_prefix


def build_my_trie():
    trie = Trie()
    trie.add_node('abs')
    trie.add_node('abs')
    # trie.add_node('ab')
    # trie.add_node('fcuk')
    # trie.print_node()
    prefix = trie.find_longest_common_prefix()
    print(prefix)


if __name__ == '__main__':
    build_my_trie()
