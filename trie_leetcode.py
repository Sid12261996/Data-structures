common_prefix = []


class Trie:
    def __init__(self):
        self.children = {}
        self.prefix = ''
        self.is_last = True

    def set_node(self, s: str, node) -> None:
        self.children[s] = node
        self.is_last = False

    def insert(self, s: str) -> None:
        self.inner_insert(s, 0)

    def inner_insert(self, s: str, index: int) -> None:
        if index == len(s):
            self.children['*'] = Trie()
            return
        current_str = s[index]
        node = self.get_node(current_str)
        if node is None:
            node = Trie()
            self.set_node(current_str, node)

        node.inner_insert(s, index + 1)

    def get_node(self, s: str):
        if s not in self.children.keys():
            return None
        return self.children[s]

    def find_longest_common_prefix(self):
        if len(self.children.keys()) == 1:
            for child in self.children.keys():
                print(self.children[child].is_last)
                # if self.children[child].is_last:
                #     return self.prefix
                self.prefix += child + self.children[child].find_longest_common_prefix()
        return self.prefix


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        trie = Trie()
        if len(strs) == 1:
            return strs[0]
        for s in strs:
            if s == "":
                return ""
            trie.insert(s)
        ans = trie.find_longest_common_prefix()
        return ans.replace('*', '')


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(['abs', 'abs', 'abs']))
