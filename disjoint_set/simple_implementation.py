"""
In this module, we implement a simple version of the Disjoint Set (Union-Find) data structure.
"""


class DisjointSet:
    """
    A simple implementation of the Disjoint Set (Union-Find) data structure
    """

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        """
        Find the root parent of x
        """
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def union(self, x, y):
        """
        Union the sets that contain x and y
        """

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        self.parent[root_y] = root_x


# Example Usage

# Create a Disjoint Set with 5 elements
ds = DisjointSet(5)

# Print the initial parent array
print(ds.parent)
# [0, 1, 2, 3, 4]

# Call method union to join sets
ds.union(0, 1)

# Print the parent array after union
print(ds.parent)
# [0, 0, 2, 3, 4]
