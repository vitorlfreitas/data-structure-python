# Array 

## Introduction

Arrays are ordered collections of elements stored in memory. Each element can be accessed by its numeric index (usually 0-based), which lets you read or write any element in constant time.

Syntax in Python example

```python
# creation
arr = [10, 20, 30]

# access by index
first = arr[0]        # 10

# append (amortized O(1))
arr.append(40)        # [10, 20, 30, 40]

# remove in middle (O(n))
del arr[1]            # [10, 30, 40]

# iterate
for x in arr:
    print(x)
```

Syntax in Java

```java

// Create arrays
int[] arr = {10, 20, 30}; // literal initialization
int[] allocated = new int[3]; // allocated with default zeros

allocated[0] = 10;
allocated[1] = 20;
allocated[2] = 30;

// Access and metadata
int first = arr[0]; // 10
int len = arr.length; // length (3)

// Modify
arr[1] = 25 // change middle element

// Iterate
for (int i = 0; i < arr.length; i++) {
    System.out.println("index " + i + " = " + arr[i]);
}
for (int v : arr) {
    System.out.println(v);
}

// Arrays utility
System.out.println(java.util.Arrays.toString(arr)); // [10, 25, 30]

// "Append" (arrays are fixed-size) using copyOf
arr = java.util.Arrays.copyOf(arr, arr.length + 1);
arr[arr.length - 1] = 40; // now [10, 25, 30, 40]

// Remove element at index 1 (shift left then shrink)
int removeIdx = 1;
for (int i = removeIdx; i < arr.length - 1; i++) {
    arr[i] = arr[i + 1];
}
arr = java.util.Arrays.copyOf(arr, arr.length - 1);

// Copying arrays
int[] dest = new int[5];
System.arraycopy(arr, 0, dest, 0, arr.length); // fast native copy

// Multi-dimensional arrays
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6}
};
int center = matrix[1][1] // 5
System.out.println(java.util.Arrays.deepToString(matrix));

```

## Array Types

There are two types of Arrays, Dynamics and Fixed. 
In programming languages such as Java, and C++, the arrays are fixed, and in Python and JavaScript, they are native dynamic. The Key difference is that, once declared, fixed arrays cannot change its length. On the other hand, dynamic arrays can resize themselves according to elements are added.

However, many languages has introduced their own dynamic array. For example, in java, there is the ArrayList.

ArrayList are arrays under the hood, which will resize its length by creating a new array with a larger capacity, then copies the previous array. After that, the Garbage collection will remove the old array. 

Example of ArrayList in java
```java

// Declaring the ArrayList
ArrayList<Integer> al = new ArrayList<>();

// Adding 10 to the list
al.add(10);

// Printing on the console
System.out.println(al.get(0)); // Output: 10

```

## Operations in Arrays

To find an element in a Array, and the array is not sorted, we need to loop through the array until find the element

```java
var myArray = [1, 2, 3, 4];

for (int i = 0; i < myArray.length; i++) {
    if (myArray[i] == target)
        return i; // Return the index 
}
return -1; // Not in the array
```

Time Complexity for insert is O(n)


Let's see more operations:

- Access by index
    - Description: Read or write element at a known index.
    - Complexity: O(1)
    - Example (Python): `x = arr[i]` / `arr[i] = v`
    - Example (Java): `int x = arr[i]; arr[i] = v;`

- Insert at end (append)
    - Description: For dynamic arrays, append adds to the end; may trigger resize.
    - Complexity: Amortized O(1); worst-case O(n) when resizing (copying to bigger buffer).
    - Example (Python): `arr.append(42)`
    - Example (Java with arrays): use Arrays.copyOf or use ArrayList:
        ```java
        // with ArrayList (recommended)
        ArrayList<Integer> al = new ArrayList<>();
        al.add(42); // amortized O(1)
        ```

- Insert at arbitrary index
    - Description: Shift subsequent elements to make room, then write new value.
    - Complexity: O(n) (shift cost)
    - Example (Python):
        ```python
        arr.insert(i, 99)  # O(n)
        ```
    - Example (manual in Java arrays):
        ```java
        // ensure capacity first, then shift
        for (int j = len - 1; j >= i; j--) arr[j+1] = arr[j];
        arr[i] = value;
        ```

- Remove at end (pop)
    - Description: Remove last element; for dynamic arrays this is O(1).
    - Complexity: O(1)
    - Example (Python): `arr.pop()`

- Remove at arbitrary index
    - Description: Shift subsequent elements left to fill gap; optionally shrink capacity.
    - Complexity: O(n) (shift cost)
    - Example (Python):
        ```python
        del arr[i]  # O(n)
        ```
    - Example (manual in Java arrays):
        ```java
        for (int j = i; j < len - 1; j++) arr[j] = arr[j+1];
        // optionally reduce logical length or copy to smaller array
        ```

- Copying / resizing
    - Description: Creating a new array and copying elements (used in resizing and many operations).
    - Complexity: O(n)
    - Notes: Dynamic arrays choose growth factor (commonly 1.5x–2x) so amortized append remains O(1).

- Slicing / subarray
    - Description: Create a view or copy of a contiguous range.
    - Complexity: O(k) to copy k elements; some languages offer O(1) view.
    - Example (Python): `sub = arr[a:b]` (creates new list, O(b-a))

- Concatenation
    - Description: Join two arrays into a new array.
    - Complexity: O(n + m) to allocate and copy both arrays.

## Conclusion

Now that we have covered the basics, let's solve a few problems using arrays!

Many Thanks!!
