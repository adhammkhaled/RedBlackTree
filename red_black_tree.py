class Node:
    def __init__(self, data, color='red'):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = color

class red_black_tree:
    def __init__(self):
        self.nil = Node(None, 'black')
        self.root = self.nil

    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.color = 'red'

        parent = None
        current = self.root

        while current != self.nil:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
        if new_node.parent==None:
            new_node.color='black'
            return
        if new_node.parent.parent==None:
            return


        self.insert_fixup(new_node)


    def insert_fixup(self, node):
        if node.parent == None:
            return
        if node.parent.parent == None:
            return
        uncle =  node.parent.parent.right  if node.parent == node.parent.parent.left else node.parent.parent.left
        if(node.parent.color=='red'):
            if uncle.color == 'red':
                self.recolor_node(node.parent)
                self.recolor_node(node.parent.parent)
                self.recolor_node(uncle)
                self.insert_fixup(node.parent.parent)
            else:

                    if self.on_the_same_line(node):
                        self.recolor_node(node.parent)
                        self.recolor_node(node.parent.parent)
                        self.rotate_node(node,node.parent.parent)

                    else:
                        self.rotate_node(node,node.parent)
                        if(node.left!=None and node.left.color=='red'):
                            self.insert_fixup(node.left)
                        elif(node.right!=None and node.right.color=='red'):
                            self.insert_fixup(node.right)


            self.root.color = 'black'

    def recolor_node(self,node):
        if(node == None):
            return
        node.color = 'black' if node.color=='red' else 'red'
    def on_the_same_line(self,node):
        if(node.parent.left==node and  node.parent.parent.left==node.parent):
            return True
        elif(node.parent.right==node  and node.parent.parent.right==node.parent):
            return True
        return False
    def rotate_node(self,node,node_rotated):
        if node.parent.left == node:
            self.right_rotate(node_rotated)
        elif node.parent.right == node:
            self.left_rotate(node_rotated)
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    def search(self,key):
        current_node = self.root
        while current_node.data!=key and current_node!= self.nil:
            if(key<current_node.data):
                current_node = current_node.left
            else:
                current_node = current_node.right
        if current_node.data==key:
            return True
        return False

    def get_tree_height(self):
        def _get_tree_height(node):
            if node == self.nil:
                return 0
            return max(1+_get_tree_height(node.left),1+_get_tree_height(node.right))
        return _get_tree_height(self.root)

    def get_tree_black_height(self):
        def _get_tree_black_height(node):
            if node == self.nil:
                return 0
            if node.color=='black':
                return max(1+_get_tree_black_height(node.left),1+_get_tree_black_height(node.right))
            else:
                return max(0 + _get_tree_black_height(node.left), 0 + _get_tree_black_height(node.right))
        return _get_tree_black_height(self.root)

    def get_tree_size(self):
        def _get_tree_size(node):
            if node == self.nil:
                return 0
            return 1+_get_tree_size(node.left)+_get_tree_size(node.right)
        return _get_tree_size(self.root)

    def inorder_traversal(self):
        def _inorder_traversal(node):
            if node != self.nil:
                _inorder_traversal(node.left)
                _inorder_traversal(node.right)
        _inorder_traversal(self.root)

if __name__ == "__main__":
    rbt = red_black_tree()

    # Insert some values into the tree
    values = [13, 7, 5, 11, 19, 2, 16, 3, 4, 17, 8, 1, 10, 15, 12, 20, 6, 9, 14, 18]
    for value in values:
        rbt.insert(value)
    print(rbt.search(5))
    print(rbt.search(11))
    # Perform an inorder traversal to see the sorted order of values in the tree
    print("Inorder Traversal of Red-Black Tree:")
    rbt.inorder_traversal()
    print()
    print(rbt.get_tree_height())
    print(rbt.get_tree_black_height())
    print(rbt.get_tree_size())