class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _update_height(self, node):
        if node is None:
            return
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self._update_height(z)
        self._update_height(y)

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        self._update_height(z)
        self._update_height(y)

        return y

    def _rebalance(self, node):
        self._update_height(node)

        balance = self._get_balance(node)

        if balance > 1:
            if self._get_balance(node.left) < 0:  # Left-Right case
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            if self._get_balance(node.right) > 0:  # Right-Left case
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _insert_recursive(self, node, key, value):
        if node is None:
            return AVLNode(key, value)

        if key < node.key:
            node.left = self._insert_recursive(node.left, key, value)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, value)
        else:
            node.value = value

        return self._rebalance(node)

    def insert(self, key, value):
        self.root = self._insert_recursive(self.root, key, value)

    def _get_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._get_min_node(node.right)
                node.key = min_node.key
                node.value = min_node.value
                node.right = self._delete_recursive(node.right, min_node.key)

        return self._rebalance(node)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def search(self, key):
        node = self._search_recursive(self.root, key)
        return node.value if node else None
