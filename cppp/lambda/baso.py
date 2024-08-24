class BSTNode:
    def __init__(self, key, name, price):
        self.key = key
        self.name = name
        self.price = price
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, name, price):
        new_node = BSTNode(key, name, price)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current_node, new_node):
        if new_node.key < current_node.key:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_recursive(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_recursive(current_node.right, new_node)

    def inorder_traversal(self):
        nodes = []
        self._inorder_recursive(self.root, nodes)
        return nodes

    def _inorder_recursive(self, current_node, nodes):
        if current_node is not None:
            self._inorder_recursive(current_node.left, nodes)
            nodes.append((current_node.key, current_node.name, current_node.price))
            self._inorder_recursive(current_node.right, nodes)

# Data dari tabel
data = [
    (115, "Mouse", 56000),
    (116, "Keyboard", 105000),
    (117, "Optical Drive", 150000),
    (119, "RAM", 750000),
    (120, "Prosesor Intel", 2500000),
    (121, "Mainboard", 920000),
    (122, "Harddisk", 656000),
    (125, "Sound Card", 250000),
    (126, "Nvidia Card", 445000)
]

# Membuat pohon BST dan memasukkan data
bst = BST()
for item in data:
    bst.insert(item[0], item[1], item[2])

# Menampilkan hasil traversal inorder (yang seharusnya terurut)
inorder_nodes = bst.inorder_traversal()
for node in inorder_nodes:
    print(f"KodeBarang: {node[0]}, Nama Barang: {node[1]}, Harga: {node[2]}")
