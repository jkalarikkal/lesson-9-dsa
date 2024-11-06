class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

root = Node(100)
root.left = Node(20)
root.right= Node(30)
root.left.left = Node(40)
root.left.right = Node(70)
root.right.right = Node(400)
root.right.left = Node(90)

print("Inorder traversal")

inorder(root)

#inorder - l, d, r
#40,20,70,100,90,30,400


