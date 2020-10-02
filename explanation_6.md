# Union and Intersection of Two Linked Lists

## About data structure
- LinkedList
  - I am using the one provided in the template.

## About Order complexity

We loop through each LinkedList and compare the values. Therefore, the amount of calculation is $O(n ^ 2)$.

## About Space complexity

In the non_overlapping_list function

- node_list => empty list => 72byte
Loop through the number of nodes and add the value
- node_list + (loop count * 8)
traverse_list function returns dictionary
new_list => dictionary => 248byte

therefore node_list + (loop count * 8) + new_list

In the union function
- llist_2_node => Node instance => 64bytes
- is_dupulicate = 28bytes
- llist_1_node = 64bytes

The maximum amount of calculation is obtained when all are not duplicated.

therefore llist_1_node + (llist_2 all node size * 8) + is_dupulicate + llist_node_2

In the intersection function
- linked_list => LinkedList instance => 64bytes
- llist_2_node => Node instance => 64bytes
- llist_1_node => Node instance => 64bytes
The data in the linked_list grows when the data matches.
therefore linked_list + (llist_1 all node size * 8) + llist_2_node + llist_1_node

## About implementation
First remove the duplicates from each LinkedList.

In "union", if there is a duplicate, change the flag to "True" and proceed to the next loop.

In "intersection", if there is a duplicate, it is added as a new Node.
