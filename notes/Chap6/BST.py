class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value == node.value:
            return
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)


    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._find_min_node(node.right)
                node.value = min_node.value
                node.right = self._delete_recursive(node.right, min_node.value)

        return node

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def minimum(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def maximum(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def in_order(self):
        if self.root is None:
            return []
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        if node is not None:
            self._in_order_recursive(node.left, result)
            result.append(node.value)
            self._in_order_recursive(node.right, result)

    def pre_order(self):
        if self.root is None:
            return []
        result = []
        self._pre_order_recursive(self.root, result)
        return result

    def _pre_order_recursive(self, node, result):
        if node is not None:
            result.append(node.value)
            self._pre_order_recursive(node.left, result)
            self._pre_order_recursive(node.right, result)


# ---------- Implement map using BST ----------

class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BSTMap:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self._put_recursive(self.root, key, value)

    def _put_recursive(self, node, key, value):
        if key == node.key:
            node.value = value
        elif key < node.key:
            if node.left is None:
                node.left = TreeNode(key, value)
            else:
                self._put_recursive(node.left, key, value)
        else:
            if node.right is None:
                node.right = TreeNode(key, value)
            else:
                self._put_recursive(node.right, key, value)

    def get(self, key):
        return self._get_recursive(self.root, key)

    def _get_recursive(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._get_recursive(node.left, key)
        else:
            return self._get_recursive(node.right, key)

    def remove(self, key):
        self.root = self._remove_recursive(self.root, key)

    def _remove_recursive(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._remove_recursive(node.left, key)
        elif key > node.key:
            node.right = self._remove_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_min_node(node.right)
                node.key = successor.key
                node.value = successor.value
                node.right = self._remove_recursive(node.right, successor.key)
        return node

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)
