from bst import BiTreeNode, BST

class AVLNode(BiTreeNode):
    def __init__(self, data):
        self.data = data
        BiTreeNode.__init__(data)
        self.bf = 0

class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    def rotate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p

        c.lchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p

        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right_left(self, p, c):
        g = c.lchild

        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else: # s1, s2, s3, s4 all empty, insert g
            p.bf = 0
            c.bf = 0
        return g

    def rotate_left_right(self, p, c):
        g = c.rchild

        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        if g.bf < 0:
            c.bf = 0
            p.bf = 1
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:
            p.bf = 0
            c.bf = 0
        return g


    def insert_no_rec(self, val):
        # 1. sams as BST, insert first
        p = self.root
        if not p:
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild   #inserted node
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else:  # val = p.data
                return

        # 2. update bf
        while node.parent:  # node.parent valid
            if node.parent.lchild == node:  # node comes from left, bf = -1
                # update node.parent.bf -= 1
                if node.parent.bf < 0:   # previously -1, now -2
                    # look at node
                    g = node.parent.parent  # connect node to parent
                    x = node.parent
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                    # connect node to parent
                elif node.parent.bf > 0:  # 1 -1 = 0
                    node.parent.bf = 0
                    break
                else:   # 0 - (-1) = -1
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else: # node comes from right, bf = 1
                # updated node.parent.bf += 1
                if node.parent.bf > 0: # bf = 2
                    g = node.parent.parent
                    x = node.parent
                    if node.bf > 0:
                        n = self.rotate_left(node.parent, node)
                    else:
                        n = self.rotate_right_left(node.parent, node)
                elif node.parent.bf < 0:
                    node.parent.bf = 0
                    break
                else:
                    node.parent.bf = 1
                    node = node.parent
                    continue

            # connect rotated tree
            n.parent = g
            if g:
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break


tree = AVLTree([9,8,7,6,5,4,3,2,1])

tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)


