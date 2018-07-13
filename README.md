# rotatedBinarySearch
O(logN) search of rotated, sorted list.
Two functions: lookup and binlookup.
Both use "divide and conquer".  binlookup does simple binary search.  
lookup searches for a name by looking for the characteristics of rotation (higher index but lower value).
It finds an unrotated portion of the list that might contain the name and then calls binlookup.

Because is stops looking for the pivot point once it has a segment of the list that is continuously increasing and may contain the desigred name, it may be faster than the solution at GeeksforGeeks:

     https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
