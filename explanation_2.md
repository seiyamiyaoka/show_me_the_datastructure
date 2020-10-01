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

## About implementation
I use a recursive function to set the directory that exists in the argument.

I got all the file paths once and then searched for the extension.

This is because it can be reused when searching with other keywords.

