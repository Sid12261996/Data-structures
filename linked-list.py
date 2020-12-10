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
    node = node.next
    while node and node.next:
        print(str(node.val) + '->', end='')
        node = node.next

    if node:
        print(node.val)
    else:
        'Empty List!'


class LinkedList:
    def __init__(self, head: Node = Node(0)):
        self.head = head
        self.currentNode = head
        self.length = 0

    def append(self, elements: list) -> Node:
        self.head, self.length = insert(elements, self.head, self.length)
        return self.head

    def sort(self, start) -> Node:
        linked_list = LinkedList(start)
        print(linked_list.length)
        middle = linked_list.get_node_at(linked_list.length // 2 + 1)
        right = linked_list.sort(middle.next)
        middle.next = None
        left = self.sort(start)
        return self.sortedList(left, right)

    def get_node_at(self, position: int) -> Node:
        current_node = self.head
        for i in range(position):
            current_node = current_node.next

        return current_node

    def sortedList(self, left, right) -> Node:
        result = None
        if left:
            return right
        elif right:
            return left

        if left.val <= right.val:
            result = left
            result.next = self.sortedList(left.next, right)
        else:
            result = right
            result.next = self.sortedList(left, right.next)

        return result


def build_my_linked_list():
    linked_list = LinkedList()
    linked_list.append([8, 7, 3, 6, 2, 5, 7, 3, 7])
    linked_list.sort(linked_list.head)
    print_nodes(linked_list.head)
    # print('length of list is: ' + str(linked_list.length))


if __name__ == '__main__':
    build_my_linked_list()
