""""
Question - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""
class Node:
    def __init__(self, val=0):
        self.left = None
        self.right = None
        self.val = val

def find_lca(root, p, q):
    if root == p or root == q:
        return root

    _left, _right = None, None
    if root.left:
        _left = find_lca(root.left, p, q)
    if root.right:
        _right = find_lca(root.right, p, q)

    if _left and _right:
        return root
    else:
        return _left or _right


def find_path(root, target, path):
    if not root:
        return []

    if root == target:
        return path + [root]

    return find_path(root.left, target, path + [root]) + find_path(root.right, target, path + [root])


if __name__ == "__main__":
    '''

                    5
                   /  \
                  8    10
                /  \  /  \
               13  23 25  30
              / \  /
            32  40 50
        '''

    root = Node(5)
    root.left = Node(8)
    root.right = Node(10)
    root.left.left = Node(13)
    root.left.right = Node(23)
    p = Node(25)
    root.right.left = p
    root.right.right = Node(30)
    root.left.left.left = Node(32)
    q = Node(40)
    root.left.left.right = q
    root.left.right.left = Node(50)

    lca_ans = find_lca(root, p, q)
    print(lca_ans.val)

    ## other solution using path
    p_path = find_path(root, p, [])
    q_path = find_path(root, q, [])

    i = 0
    ans = None
    while i < min(len(p_path), len(q_path)):
        if p_path[i] == q_path[i]:
            ans = p_path[i]
        i += 1

    print(ans.val)