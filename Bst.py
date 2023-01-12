class Node:
     def __init__(self,val = None):
        self.left  = None
        self.right = None
        self.val = val

class BSTNode() :
    def __init__(self,val = None):
        self.root = None
    def insert(self,val):
        if self.root == val:
            return
        if not self.root :
            self.root = Node(val)
        else:
            cur = self.root
            while True:
                if val < cur.val:
                    if not cur.left:
                        # print(self.left)
                        cur.left = Node(val)
                        break
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = Node(val)
                        break
                    cur = cur.right 

l1 = list(map(int,input().split()))
bst = BSTNode()
for j in l1:
    bst.insert(j)


