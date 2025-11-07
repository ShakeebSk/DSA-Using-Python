class SuffixTreeNode:
    def __init__(self):
        self.children = {}

class SuffixTree:
    def __init__(self, text):
        self.root = SuffixTreeNode()
        for i in range(len(text)):
            self._insert_suffix(text[i:])

    def _insert_suffix(self, suffix):
        node = self.root
        for char in suffix:
            if char not in node.children:
                node.children[char] = SuffixTreeNode()
            node = node.children[char]

    # Basic search for substring
    def search(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Test
stree = SuffixTree("banana")
assert stree.search("ana")
assert not stree.search("apple")[web:8][web:16][web:19]
