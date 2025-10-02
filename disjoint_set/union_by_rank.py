"""
In this module, we implement a version of the Disjoint Set (Union-Find) data structure.
But this time, we use union by rank to optimize the union operation.
"""


class DisjointSet:
    """
    A implementation of the Disjoint Set (Union-Find) data structure
    """

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

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

        # Union by Rank
        # Attach the smaller rank tree under the root of the higher rank tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y

        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        # If ranks are same, then make one as root of another and increment its rank by one
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1


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
