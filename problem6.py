class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def non_overlapping_list(node):
    node_list = []
    while node is not None:
        node_list.append(node.value)
        node = node.next

    new_list = [*traverse_list(node_list)]
    linked_list = LinkedList()

    for i in new_list:
        linked_list.append(i)
    return linked_list

def traverse_list(node_list):
    store = {}

    for element in node_list:
        store[element] = 1
    return store

def union(llist_1, llist_2):
    llist_2_node = llist_2.head
    is_dupulicate = False

    while llist_2_node:
        llist_1_node = llist_1.head
        while llist_1_node:
            if llist_1_node.value == llist_2_node.value :
                is_dupulicate = True
                break
            else:
                llist_1_node = llist_1_node.next
        if is_dupulicate is False:
            llist_1.append(llist_2_node)
        else:
            is_dupulicate = False
        llist_2_node = llist_2_node.next
    return llist_1

def intersection(llist_1, llist_2):
    linked_list = LinkedList()
    llist_2_node = llist_2.head

    while llist_2_node:
        llist_1_node = llist_1.head
        while llist_1_node:
            if llist_1_node.value == llist_2_node.value:
                linked_list.append(Node(llist_1_node.value))
                break
            else:
                llist_1_node = llist_1_node.next
        llist_2_node = llist_2_node.next
    return linked_list

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(non_overlapping_list(linked_list_1.head),non_overlapping_list(linked_list_2.head)))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
print(intersection(non_overlapping_list(linked_list_1.head),non_overlapping_list(linked_list_2.head)))
# 6 -> 4 -> 21 ->

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(non_overlapping_list(linked_list_3.head),non_overlapping_list(linked_list_4.head)))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print(intersection(non_overlapping_list(linked_list_3.head),non_overlapping_list(linked_list_4.head)))
# no print

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(non_overlapping_list(linked_list_5.head),non_overlapping_list(linked_list_6.head)))
# no print
print(intersection(non_overlapping_list(linked_list_5.head),non_overlapping_list(linked_list_6.head)))
# no print