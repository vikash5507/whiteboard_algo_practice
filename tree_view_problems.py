"""
Tree View Problems (Unbalanced tree): https://leetcode.com/discuss/general-discussion/1094690/views-and-traversal-of-binary-tree-important-topics-must-read
- Right View -  Level order traversal , add element of End of element of each level (BFS)
- Left View -  Level order traversal, add element of First element of each level (BFS)
- Top View - using Horizontal Distance from root (left of root negate by 1, right of root increase by one) - Add value in a Map if first encountered for that Horizontal Distance (for top view, inverse in case of bottom view)
- Bottom View -  similar to top view, just update map always so that last updated will be of bottom for that Horizontal distance
- Boundary View (Anticlock wise) - find leftView, leafNodes, rightView in this order

"""


class Node:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val


def right_left_view_tree_using_bfs(root):
    if not root:
        return
    right_view_values, left_view_values = [], []

    queue = [root]

    while queue:
        size = len(queue)

        for i in range(size):
            q = queue.pop(0)

            if i == size - 1:
                right_view_values.append(q)
            if i == 0:
                left_view_values.append(q)

            if q.left:
                queue.append(q.left)
            if q.right:
                queue.append(q.right)

    left_view_values_print = [q.val for q in left_view_values]
    print("left_view_values_print: ")
    print(left_view_values_print)
    right_view_values_print = [q.val for q in right_view_values]
    print("right_view_values_print: ")
    print(right_view_values_print)


left_view_max_level = 0
left_view_values = []
def left_view_tree_dfs(root, level):
    if not root:
        return

    global left_view_values
    global left_view_max_level
    if level > left_view_max_level:
        left_view_values.append(root.val)
        left_view_max_level = level

    left_view_tree_dfs(root.left, level+1)  # not here we need to left first (PRE ORDER)
    left_view_tree_dfs(root.right, level+1)


right_view_max_level = 0
right_view_values = []

def right_view_tree_dfs(root, level):
    if not root:
        return

    global right_view_values
    global right_view_max_level
    if level > right_view_max_level:
        right_view_values.append(root.val)
        right_view_max_level = level

    right_view_tree_dfs(root.right, level+1)  # not here we need to right first (POST ORDER)
    right_view_tree_dfs(root.left, level+1)

"""
    Solve using Horizontal Distance (start with 0 at root, negate by 1 on moving left, increase by 1 on moving right
    Maintain Map of <HorizontalDistance, Value> ~ store at first horizontal distance find
"""
def top_level_view_tree_using_dfs(root, horizontal_distance, hd_map):
    if not root:
        return
    if horizontal_distance not in hd_map:
        hd_map[horizontal_distance] = root.val
    if root.left:
        if horizontal_distance-1 not in hd_map:
            hd_map[horizontal_distance-1] = root.left.val

    if root.right:
        if horizontal_distance+1 not in hd_map:
            hd_map[horizontal_distance+1] = root.right.val

    top_level_view_tree_using_dfs(root.left, horizontal_distance - 1, hd_map)
    top_level_view_tree_using_dfs(root.right, horizontal_distance+1, hd_map)

"""
    Similar logic as top view, but keep on updating values so that last depth values are updated in map
"""
def bottom_level_view_tree_using_dfs(root, horizontal_distance, hd_map):
    if not root:
        return
    hd_map[horizontal_distance] = root.val

    bottom_level_view_tree_using_dfs(root.left, horizontal_distance - 1, hd_map)
    bottom_level_view_tree_using_dfs(root.right, horizontal_distance + 1, hd_map)


def top_level_view_tree_using_bfs(root):
    if not root:
        return []
    horizontal_distance = 0
    horizontal_distance_map = {}
    queue = [(root, horizontal_distance)]

    while queue:
        # iterate layer (here max only 2 possible - binary tree)
        q, hd = queue.pop(0)
        if hd not in horizontal_distance_map:
            horizontal_distance_map[hd] = q.val
        if q.left:
            queue.append((q.left, hd-1))
        if q.right:
            queue.append((q.right, hd+1))

    return horizontal_distance_map.values()

def bottom_level_view_tree_using_bfs(root):
    if not root:
        return []
    horizontal_distance = 0
    horizontal_distance_map = {}
    queue = [(root, horizontal_distance)]

    while queue:
        # iterate layer (here max only 2 possible - binary tree)
        q, hd = queue.pop(0)
        # if hd not in horizontal_distance_map:
        horizontal_distance_map[hd] = q.val # always update
        if q.left:
            queue.append((q.left, hd-1))
        if q.right:
            queue.append((q.right, hd+1))

    return horizontal_distance_map

def leaf_nodes_of_tree_bfs(root):
    if not root:
        return []
    queue = [root]
    leaf_nodes_values = []
    while queue:
        q = queue.pop(0)
        if not q.left and not q.right:
            leaf_nodes_values.append(q.val)
        if q.left:
            queue.append(q.left)
        if q.right:
            queue.append(q.right)

    return leaf_nodes_values

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
    root = Node(Node(Node(val=20), Node(None, Node(val=45), 25), 10), Node(Node(val=30), Node(val=35), 15), 5)

    ## Right and Left View using BFS and DFS
    # ****************** LEFT AND RIGHT LEVEL VIEW *********************** #
    right_left_view_tree_using_bfs(root)

    left_view_tree_dfs(root, 1)
    print("Left View DFS Approach : ")
    print(left_view_values)

    right_view_tree_dfs(root, 1)
    print("Right View DFS Approach : ")
    print(right_view_values)

    ## Top and Bottom View using DFS
    # ****************** TOP LEVEL VIEW *********************** #
    top_view_horizontal_distance_map = {}
    to_view_horizontal_distance = 0
    top_level_view_tree_using_dfs(root, to_view_horizontal_distance, top_view_horizontal_distance_map)
    print("Top View Values using DFS")
    print(top_view_horizontal_distance_map.values())

    print("Top View Values using BFS")
    print(top_level_view_tree_using_bfs(root))

    root2 = Node(Node(Node(None, Node(Node(Node(val=10), None, 9), None, 7), 4), Node(val=5), 2),
                 Node(None, Node(Node(None, Node(val=11), 8), None, 6), 3), 1)
    top_view_horizontal_distance_map2 = {}
    top_view_horizontal_distance2 = 0
    top_level_view_tree_using_dfs(root2, top_view_horizontal_distance2, top_view_horizontal_distance_map2)
    print("Top View Values2 using DFS")
    print(top_view_horizontal_distance_map2.values())

    print("Top View Values using BFS")
    print(top_level_view_tree_using_bfs(root2))

    # ****************** BOTTOM LEVEL VIEW *********************** #
    bottom_view_horizontal_distance_map = {}
    bottom_view_horizontal_distance = 0
    bottom_level_view_tree_using_dfs(root, bottom_view_horizontal_distance, bottom_view_horizontal_distance_map)
    print("Bottom View Values")
    print(bottom_view_horizontal_distance_map)

    print("Bottom View Values using BFS")
    print(bottom_level_view_tree_using_bfs(root))

    bottom_view_horizontal_distance_map2 = {}
    bottom_view_horizontal_distance2 = 0
    bottom_level_view_tree_using_dfs(root2, bottom_view_horizontal_distance2, bottom_view_horizontal_distance_map2)
    print("Bottom View Values2")
    print(bottom_view_horizontal_distance_map2) # todo -> not correct

    print("Bottom View Values using BFS")
    print(bottom_level_view_tree_using_bfs(root2))

    # ****************** BOUNDARY VIEW *********************** #
    # boundary includes left boundary, leaves, and right boundary in order without duplicate nodes (ANTI-CLOCKWISE)

    print("BOUNDARY VIEW values: ")
    print(boundary_view_anticlockwise(root))

    print("BOUNDARY VIEW values2: ")
    print(boundary_view_anticlockwise(root2))

    root3 = Node(Node(Node(None,Node(None,Node(val=45),5),10), Node(val=30),20), Node(Node(None,Node(val=55),50),Node(val=70),60),40)
    print("BOUNDARY VIEW values3: ")
    print(boundary_view_anticlockwise(root3))
