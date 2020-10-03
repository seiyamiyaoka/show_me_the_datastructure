# Active Directory

## About data structure
- hashmap
  - I created a hashmap with the user name as the key.
## About Order complexity
$O(1)$
The user's data is stored in an array.

Processing in a loop requires $O(n)$ complexity, but by converting the data to hashmap, the complexity is $O(1)$.

## About Space complexity
- is_user_in_group
  - $O(n)$. This is because all the user's data is stored in an array.

## About implementation

I use hashmap to check if a user belongs to a group.
You can check if the specified key exists by creating a dictionary from the array.

The amount of calculation required to acquire data by this conversion is $O(1)$.

It's efficient.
