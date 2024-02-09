class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


count = 0


def countRightLeaves(root):
    # base condition
    if not root:
        return

    countRightLeaves(root.left)
    if (root.right and root.right.right is None and root.right.left is None):
        global count
        count += 1
    countRightLeaves(root.right)


root = Node(3)
root_left = Node(5)
root_right = Node(7)
root.left = root_left
root.right = root_right

root_right_left = Node(6)
root_right.left = root_right_left

countRightLeaves(root)
print(count)

######## *****

# A = [1, 2]
# B = [-1, 4]
# C = [5, 6]
# D = [0, 0, 10]

# Integer arrays

# Target = 5

# A[i] + B[j] + C[k] + D[z] = target
# Count

# 1 <= n <= 10^3

A = [1, 2]
B = [-1, 4]
C = [5, 6]
D = [0, 0, 10]

target = 5


def preComputePossibleSum(A, B):
    possible_sum = {}
    for a in A:
        for b in B:
            if a + b in possible_sum:
                possible_sum[a + b] += 1
            else:
                possible_sum[a + b] = 1

    return possible_sum


def solve(A, B, C, D, target):
    count = 0
    possible_sum = preComputePossibleSum(C, D)
    for a in A:
        for b in B:
            rest_possible_sum = (target - (a + b))
            if rest_possible_sum in possible_sum:
                count += possible_sum[rest_possible_sum]

    return count


print(solve(A, B, C, D, target))



