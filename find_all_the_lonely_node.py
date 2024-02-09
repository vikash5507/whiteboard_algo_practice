"""
Question - https://leetcode.ca/all/1469.html
https://leetcode.com/problems/find-all-the-lonely-nodes/

In a binary tree, a lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.

Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. Return the list in any order.

Input: root = [1,2,3,null,4]
Output: [4]
Explanation: Light blue node is the only lonely node.
Node 1 is the root and is not lonely.
Nodes 2 and 3 have the same parent and are not lonely.

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2]
Output: [6,2]
Explanation: Light blue nodes are lonely nodes.
Please remember that order doesn't matter, [2,6] is also an acceptable answer.

Input: root = [11,99,88,77,null,null,66,55,null,null,44,33,null,null,22]
Output: [77,55,33,66,44,22]
Explanation: Nodes 99 and 88 share the same parent. Node 11 is the root.

Input: root = [197]
Output: []

Input: root = [31,null,78,null,28]
Output: [78,28]

Constraints:

The number of nodes in the tree is in the range [1, 1000].
Each node's value is between [1, 10^6].
"""

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_lonely_nodes(root: Node, ans):
    if not root:
        return

    find_lonely_nodes(root.left, ans)
    find_lonely_nodes(root.right, ans)
    if root.left and not root.right:
        ans.append(root.left.val)
    elif root.right and not root.left:
        ans.append(root.right.val)



# root1 = [1,2,3,null,4]
root1 = Node(1, Node(2, None, Node(4)), Node(3))
ans1 = []
find_lonely_nodes(root1, ans1)
print(ans1)
assert ans1 == [4]


root2 = Node(7, Node(1, Node(6), None), Node(4, Node(5), Node(3, None, Node(2))))
ans2 = []
find_lonely_nodes(root2, ans2)
print(ans2)
assert ans2 == [6,2]


