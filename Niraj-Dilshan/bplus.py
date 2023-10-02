class BPlusTree:
    def __init__(self, order):
        self.root = Node()
        self.order = order

    def search(self, key):
        return self.root.search(key)

    def insert(self, key, value):
        if self.root.is_full():
            new_root = Node()
            new_root.children.append(self.root)
            new_root.split_child(0)
            self.root = new_root
        self.root.insert(key, value)

class Node:
    def __init__(self, is_leaf=True):
        self.keys = []
        self.values = []
        self.children = []
        self.is_leaf = is_leaf

    def is_full(self):
        return len(self.keys) == 2 * tree.order - 1

    def split_child(self, i):
        new_node = Node(is_leaf=self.children[i].is_leaf)
        split_key = self.children[i].keys[tree.order - 1]

        self.keys.insert(i, split_key)
        self.values.insert(i, self.children[i].values[tree.order - 1])
        self.children.insert(i + 1, new_node)

        new_node.keys = self.children[i].keys[tree.order:]
        new_node.values = self.children[i].values[tree.order:]
        self.children[i].keys = self.children[i].keys[:tree.order - 1]
        self.children[i].values = self.children[i].values[:tree.order - 1]

    def insert(self, key, value):
        i = len(self.keys) - 1
        if self.is_leaf:
            self.keys.append(None)
            self.values.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                self.values[i + 1] = self.values[i]
                i -= 1
            self.keys[i + 1] = key
            self.values[i + 1] = value
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if self.children[i].is_full():
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert(key, value)

    def search(self, key):
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1
        if i < len(self.keys) and key == self.keys[i]:
            return self.values[i]
        elif self.is_leaf:
            return None
        else:
            return self.children[i].search(key)

if __name__ == "__main__":
    tree = BPlusTree(order=3)

    # Inserting values into the B+ tree
    tree.insert(10, "Value 10")
    tree.insert(20, "Value 20")
    tree.insert(5, "Value 5")

    # Searching for a value in the B+ tree
    result = tree.search(10)
    if result:
        print("Key 10 found with value:", result)
    else:
        print("Key 10 not found")
