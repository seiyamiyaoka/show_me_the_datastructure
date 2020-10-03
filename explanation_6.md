# Union and Intersection of Two Linked Lists

## About data structure
- LinkedList
  - I am using the one provided in the template.

## About Order complexity

We loop through each LinkedList and compare the values. Therefore, the amount of calculation is $O(n ^ 2)$.

## About Space complexity
- Node
  - __init__
    - $O(1)$
- LinkedList
  - __init__
    - $O(1)$
  - append
    - $O(1)$. This is because it is constantly overwriting the node variable.
  - size
    - $O(1)$. This is because the size variable is incremented, but as a result, the variable is overwritten.
- non_overlapping_list
  - $O(n)$. This is because the value is added to the node_list variable while the node exists.
- traverse_list
  - $O(n)$.
- union
  - $O(n)$. This is because at most one node_list element is added.
- intersection
  - $O(n)$. This is because at most one node_list element is added.
## About implementation
First remove the duplicates from each LinkedList.

In "union", if there is a duplicate, change the flag to "True" and proceed to the next loop.

In "intersection", if there is a duplicate, it is added as a new Node.
