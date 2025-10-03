"""
In this module, we solve the challenge of Tower of Hanoi
"""


def tower_of_hanoi(n, a, b, c) -> None:
    """
    Solve the Tower of Hanoi problem.
    """

    # Base case
    if n == 1:
        print(f"Move disk 1 from {a} to {c}")
        return

    # Move n-1 disks from A to B using C as auxiliary
    tower_of_hanoi(n - 1, a, c, b)

    # Move the nth disk from A to C
    print(f"Move disk {n} from {a} to {c}")

    # Move the n-1 disks from B to C using A as auxiliary
    tower_of_hanoi(n - 1, b, a, c)


N = 3 # Number of disks
tower_of_hanoi(N, 'A', 'B', 'C')

# Time complexity: O(2^N)
# Space complexity: O(N) (due to recursion stack)
