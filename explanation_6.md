# Union and Intersection of Two Linked Lists

## About data structure
- LinkedList
  - I am using the one provided in the template.

## About Order complexity

We loop through each LinkedList and compare the values. Therefore, the amount of calculation is $O(n ^ 2)$.


## About implementation
First remove the duplicates from each LinkedList.

In "union", if there is a duplicate, change the flag to "True" and proceed to the next loop.

In "intersection", if there is a duplicate, it is added as a new Node.
