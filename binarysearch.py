class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left        # left child tree
        self.right = right      # right child tree
    def __str__(self):
        return str(self.value)

def preTraverse(root: Node):
    if root == None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)

def midTraverse(root: Node):
    if root == None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)

def afterTraverse(root: Node):
    if root == None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value)

def reverseTree(root: Node):
    if root == None:
        return
    node = root.left
    root.left = root.right
    root.right = node

    reverseTree(root.left)
    reverseTree(root.right)

def queryBinaryTree(root: Node, val):
    boolLeft = True
    if root == None:
        print('not found')
        return None
    if root.value == val:
        print('Query value found.')
        return root
    #if root.left != None:
    queryBinaryTree(root.left, val)
    #if root.right != None:
    queryBinaryTree(root.right, val)


if __name__ == '__main__':
    nodeA = Node('A')
    nodeC = Node('C')
    nodeF = Node('F')
    nodeB = Node('B', nodeA, nodeC)
    nodeG = Node('G', nodeF, None)
    nodeE = Node('E', None, nodeG)
    nodeD = Node('D', nodeB, nodeE)

    preTraverse(nodeD)
    #midTraverse(nodeD)
    #afterTraverse(nodeD)
    print('------')
    reverseTree(nodeD)
    preTraverse(nodeD)

    queryBinaryTree(nodeD, 'G')