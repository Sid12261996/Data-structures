from typing import Tuple


class Node:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


def get_to_the_end_of_list(node: Node) -> Node:
    while node and node.next:
        node = node.next
    return node


def insert(elements: list, head: Node = Node(0), length: int = 0) -> Tuple[Node, int]:
    dummy = get_to_the_end_of_list(head)
    ptr = dummy
    for element in elements:
        ptr.next = Node(element)
        ptr = ptr.next
        length += 1
    return head, length


def print_nodes(node: Node):
    # node = node.next
    while node and node.next:
        print(str(node.val) + '->', end='')
        node = node.next

    if node:
        print(node.val)
    else:
        'Empty List!'


def length(start: Node) -> int:
    node_size = 0
    while start:
        start = start.next
        node_size += 1
    return node_size


class LinkedList:
    def __init__(self, head: Node = Node(0)):
        self.head = head
        self.currentNode = head
        self.length = 0

    def append(self, elements: list) -> Node:
        self.head, self.length = insert(elements, self.head, self.length)
        return self.head

    def sort(self) -> Node:
        return self.inner_sort(self.head.next)

    def inner_sort(self, start) -> Node:
        if start and start.next:
            mid = self.get_node_at(start, (length(start) // 2)-1)
            next_to_mid = mid.next
            mid.next = None
            left = self.inner_sort(start)
            right = self.inner_sort(next_to_mid)
            merged_list = self.merge_list(left, right)
            return merged_list
        return start

    def get_node_at(self, node: Node, position: int) -> Node:
        current_node = node
        for i in range(position):
            current_node = current_node.next

        return current_node

    def merge_list(self, left, right) -> Node:
        result = None
        if left:
            return right
        elif right:
            return left

        if left.val <= right.val:
            result = left
            result.next = self.merge_list(left.next, right)
        else:
            result = right
            result.next = self.merge_list(left, right.next)

        return result

    def print_list(self):
        print_nodes(self.head.next)


def build_my_linked_list():
    linked_list = LinkedList()
    linked_list.append([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    list = linked_list.sort()
    print_nodes(list)
    linked_list.print_list()
    # print('length of list is: ' + str(linked_list.length))


if __name__ == '__main__':
    build_my_linked_list()
