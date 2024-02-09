'''// There is a binary tree, where each node has sugar.
// An ant which is going around the tree to eat the sugar and traveling in anti-clockwise direction.
// It can only eat sugar at the boundary.
// Write a program which prints the node visited by the ant.


     4
  3    6
2    1    8


// 4 -> 3 -> 2 -> 1 -> 8 -> 6

        1
     2    3
   5  6  7  8
     9
// 1 -> 2 -> 5 -> 9 -> 7 -> 8 -> 3

left view - 1,2,5,9
right view - 1, 3, 8, 9

        P

        1
     2    3
P  5  6  7  8   P
     9
   11 12
 14     13
    15
  16
       P

// 1 -> 2-> 5. 9 -> 11 -> 14 -> 15 -> 16 -> 13 -> 12 -> 7 -> 8 -> 3

# leftview - 1 -> 2-> 5. 9 -> 11 -> 14 -> 15 -> 16
# rightview - 1,3,8,9,12,13,15,16
# bottomview - 16,13,7,8

# ans = [1, 2, 5, ]
# queue [(1, yes)]

# pop 1
# [2, 3]

# pop 2
# [3, 5, 6]

# pop 3


'''


class Node:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val


# queue = [root]
# left_view_nodes, right_view_nodes, bottom_view_nodes = [], [], []
#
#
# def bfs_helper(root):
#     if not root:
#         return
#
#     queue_size = len(queue)
#     for i in range(queue_size):
#         q = queue.pop()
#         if i == 0:
#             left_view_nodes.append(q)
#         if i == queue_size - 1:
#             right_view_nodes.append(q)
#
#         if not q.left and not q.right:
#             bottom_view_nodes.append(q)
#
#         if q.left:
#             queue.append(q.left)
#         if q.right:
#             queue.append(q.right)

def boundary_view_anticlockwise(root):
    if not root:
        return []
    boundary_view_anticlockwise_values = [root.val]
    if not root.left and not root.right:
        return boundary_view_anticlockwise_values

    # leftview -> it does not include the left most boundary node value
    curr = root.left
    left_view_queue = [curr]
    while left_view_queue:
        q = left_view_queue.pop(0)
        if q.left:
            boundary_view_anticlockwise_values.append(q.val)
            left_view_queue.append(q.left)
        elif q.right:
            boundary_view_anticlockwise_values.append(q.val)
            left_view_queue.append(q.right)

    # leafview
    curr = root
    leaf_nodes_queue = [curr]
    while leaf_nodes_queue:
        q = leaf_nodes_queue.pop()  # stack solution
        if not q.left and not q.right:
            boundary_view_anticlockwise_values.append(q.val)

        if q.right:
            leaf_nodes_queue.append(q.right)
        if q.left:
            leaf_nodes_queue.append(q.left)

    # rightview (bottom to top)
    curr = root.right
    right_nodes_queue = [curr]
    right_nodes_queue_values = []
    while right_nodes_queue:
        q = right_nodes_queue.pop(0)
        if q.right:
            right_nodes_queue_values.append(q.val)
            right_nodes_queue.append(q.right)
        elif q.left:
            right_nodes_queue_values.append(q.val)
            right_nodes_queue.append(q.left)
        # right_nodes_stack_values.append(q.val)

    print(right_nodes_queue_values)
    boundary_view_anticlockwise_values.extend(right_nodes_queue_values[::-1]) # need to reverse for bottom to top

    return boundary_view_anticlockwise_values


if __name__ == "__main__":
    root = Node(Node(Node(val=5),Node(Node(val=9),None,6),2), Node(Node(val=7),Node(val=8),3),1)
    print(boundary_view_anticlockwise(root))
"""
        1
     2    3
   5  6  7  8
     9
// 1 -> 2 -> 5 -> 9 -> 7 -> 8 -> 3
queue = [1]
lv, rv, bv = [], [], []

Level 1 -> for 1 -> queue_size = 1, q = 1
queue = [1] -> [2,3]
lv, rv, bv = [1], [1], []

Level2 -> for 2 -> queue_size = 2, q = 2
queue = [1] -> [2,3] -> [3, 5, 6]
lv, rv, bv = [1,2], [1], []

  for 3 -> queue_size = 2, q = 3
  queue = [1] -> [2,3] -> [3, 5, 6] -> [5, 6, 7, 8]
  lv, rv, bv = [1,2], [1, 3], []

Level3 -> for 5 -> queue_size = 4, q = 5
   queue = [1] -> [2,3] -> [3, 5, 6] -> [5, 6, 7, 8] -> [6, 7 , 8]
	 lv, rv, bv = [1,2, 5], [1, 3], [5]

   for 6, queue_size = 4, q = 6
   queue = [1] -> [2,3] -> [3, 5, 6] -> [5, 6, 7, 8] -> [6, 7 , 8] -> [7 , 8, 9]
	 lv, rv, bv = [1,2, 5], [1, 3], [5]

   for 7, queue_size = 4, q = 7
  queue = [1] -> [2,3] -> [3, 5, 6] -> [5, 6, 7, 8] -> [6, 7 , 8] -> [7 , 8, 9] -> [8, 9]
	 lv, rv, bv = [1,2, 5], [1, 3], [5, 7]

   for 8, queue_size = 4, q = 8
  queue = [1] -> [2,3] -> [3, 5, 6] -> [5, 6, 7, 8] -> [6, 7 , 8] -> [7 , 8, 9] -> [8, 9] -> [9]
	 lv, rv, bv = [1,2, 5], [1, 3, 8], [5, 7, 8]

Level 4:
	for 9, queue_size = 1, q = 9
  queue = [1] -> [2,3] -> [3, 5, 6] -> [5, 6, 7, 8] -> [6, 7 , 8] -> [7 , 8, 9] -> [8, 9] -> [9] -> []
	 lv, rv, bv = [1,2, 5, 9], [1, 3, 8, 9], [5, 7, 8, 9]
"""
























