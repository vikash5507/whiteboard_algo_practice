"""
Given a level-order sorted complete binary tree, the task is to check whether a key exists in it or not. A complete binary tree has every level except possibly the last, completely filled, with all nodes as far left as possible.

e.g
             7
          /     \
         10      15
       /   \    /  \
      17   20  30  35
     / \   /     
    40 41 50      

Input: Node = 3
Output: No

Input: Node = 7
Output: Yes

Input: Node = 30
Output: Yes
"""

## Code
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def binarySearch(level_nodes, K):
    size = len(level_nodes)
    l, r = 0, size-1
    
    while l < r:
        mid = (l+r)//2
        if level_nodes[mid].val == K:
            return True
        elif level_nodes[mid].val < K:
            l = mid+1
        else:
            r = mid
    
    return False
            

def generateGrayBitCode(n):
    pass

def findLevel(node, K):
    #if K is less than root node - not possible to find K
    if K < node.val:
        return -1
        
    if node.val == K: #actually found Key K on that levelmost -> terminate as no need to do binarySearch
        return -2

    curr = node
    level = 0
    while curr:
        level += 1
        curr = curr.left
        
        if curr.val == K:
            return -2
            
        if curr.val < K and (not curr.left or curr.left.val > K):
            return level
        
    return level
    
def findKey(root: Node, K: int):
    if not Node:
        return False
    """
        1. Search on Left node of all levels - to find most probable level
        2. Do Binary Search on that level - but how to iterate nodes on that level
    """
    level = findLevel(root, K)
    print(level)

    if level == -2: #if left most node of any level values was equal to K
        return True
    
    if level == -1: # if K is less than root node val 
        return False
    
    

# Driver code
if __name__ == "__main__":
 
    # Consider the following level
    # order sorted tree
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
    root.right.left = Node(25)
    root.right.right = Node(30)
    root.left.left.left = Node(32)
    root.left.left.right = Node(40)
    root.left.right.left = Node(50)
 
    # Keys to be searched
    arr = [ 5, 8, 9, 23, 40 ]
    n = len(arr)
 
    for i in range(n):
        if (findKey(root, arr[i])):
            print("Yes")
        else:
            print("No")