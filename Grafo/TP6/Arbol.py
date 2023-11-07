import sys #Import library 'sys'
sys.path.append('/home/ms/Algoritmo_2023_MS/Cola') 
from colaClass import Cola

class BinaryTree:

    class __Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert_node(self, value):
        def __insert(root, value):
            if root is None:
                return BinaryTree.__Node(value)
            elif value < root.value:
                root.left = __insert(root.left, value)
            else:
                root.right = __insert(root.right, value)

            return root

        self.root = __insert(self.root, value)
        # balancear(arbol)
        # actualizar_altura(arbol)

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value)
                __preorden(root.left)
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        if self.root is not None:
            __inorden(self.root)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        if(self.root is not None):
            __postorden(self.root)

    def by_level(self):
        pendings = Cola()
        pendings.arrive(self.root)
        while not pendings.size == 0:
            node = pendings.atention()
            if node:
                print(node.value, node.left.value if node.left else None, node.right.value if node.right else None)
                if node.left:
                    pendings.arrive(node.left)
                if node.right:
                    pendings.arrive(node.right)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)
        aux = None
        if self.root is not None:
            aux = __search(self.root, key)
        return aux

    def delete_node(self, key):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, key):
            if root is not None:
                if key < root.value:
                    root.left, value = __delete(root.left, key)
                elif key > root.value:
                    root.right, value = __delete(root.right, key)
                else:
                    value = root.value
                    if root.left is None and root.right is not None:
                        return root.right, value
                    elif root.right is None and root.left is not None:
                        return root.left, value
                    elif root.left is None and root.right is None:
                        return None, value
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        return root, value
            return root, value
        deleted_value = None
        if self.root is not None:
            self.root, deleted_value = __delete(self.root, key)
            # actualizar_altura(arbol)
            # balancear(arbol)
        return deleted_value
