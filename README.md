# rotatedBinarySearch
O(logN) search of rotated, sorted list.
Two functions: lookup and binlookup.
Both use "divide and conquer".  binlookup does simple binary search.  
lookup searches for a name by looking for the characteristics of rotation (higher index but lower value).
It finds an unrotated portion of the list that might contain the name and then calls binlookup.
