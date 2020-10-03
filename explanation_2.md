# Finding Files

## About data structure
I used the List data structure to hold the data.

It also uses recursion to traverse directories.

## About Order complexity
$O(n log n)$
This is because it is sorted using python sorted.

Considering only traverse
$O(N)$
N = all directory size

Even if the recursive function is executed in the loop, it will be executed for the number of directories included.

## About Space complexity

- find_files
  - $O(n)$. The elements of the array are n because there are as many paths as the directory contains.
- traverse_path
  - $O(n^2)$. This is because it uses the traverse_path function recursively. No reference is shared as it returns a new array.
- search_prefix
  - $O(n)$. The names argument expects an array. The elements of the array are `n` because there are as many paths as the directory contains.

## About implementation
I use a recursive function to set the directory that exists in the argument.

I got all the file paths once and then searched for the extension.

This is because it can be reused when searching with other keywords.

