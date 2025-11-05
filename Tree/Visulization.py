class TreeVisualizer:
    def __init__(self):
        self.fig, self.ax = None, None
    
    def get_positions(self, root, x=0, y=0, layer=1, pos=None, parent=None, offset=3):
        if pos is None:
            pos = {}
        if root:
            pos[id(root)] = (x, -y)
            offset_x = offset / (2 ** layer)
            if root.left:
                self.get_positions(root.left, x - offset_x, y + 1, layer + 1, pos, id(root), offset)
            if root.right:
                self.get_positions(root.right, x + offset_x, y + 1, layer + 1, pos, id(root), offset)
        return pos
    
    def visualize_tree(self, root, title="Tree Structure"):
        if not root:
            print("Empty tree")
            return
        
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        pos = self.get_positions(root)
        
        self._draw_tree(root, pos)
        
        self.ax.set_title(title, fontsize=16, fontweight='bold')
        self.ax.axis('off')
        plt.tight_layout()
        plt.show()
    
    def _draw_tree(self, root, pos, parent_pos=None):
        if not root:
            return
        
        x, y = pos[id(root)]
        
        if parent_pos:
            px, py = parent_pos
            self.ax.plot([px, x], [py, y], 'k-', linewidth=2, zorder=1)
        
        circle = Circle((x, y), 0.3, color='lightblue', ec='black', linewidth=2, zorder=2)
        self.ax.add_patch(circle)
        self.ax.text(x, y, str(root.val), ha='center', va='center', 
                    fontsize=12, fontweight='bold', zorder=3)
        
        if root.left:
            self._draw_tree(root.left, pos, (x, y))
        if root.right:
            self._draw_tree(root.right, pos, (x, y))
    
    def animate_traversal(self, root, traversal_type='inorder'):
        if not root:
            print("Empty tree")
            return
        
        traversal_order = []
        if traversal_type == 'inorder':
            self._inorder_animation(root, traversal_order)
        elif traversal_type == 'preorder':
            self._preorder_animation(root, traversal_order)
        elif traversal_type == 'postorder':
            self._postorder_animation(root, traversal_order)
        
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        pos = self.get_positions(root)
        
        def animate(frame):
            self.ax.clear()
            self.ax.set_title(f'{traversal_type.capitalize()} Traversal - Step {frame + 1}/{len(traversal_order)}',
                            fontsize=16, fontweight='bold')
            self.ax.axis('off')
            
            self._draw_tree_animation(root, pos, traversal_order[:frame + 1])
            
            visited_text = ' -> '.join(map(str, [n.val for n in traversal_order[:frame + 1]]))
            self.ax.text(0, max(p[1] for p in pos.values()) + 1.5, f'Visited: {visited_text}',
                        ha='center', fontsize=12, bbox=dict(boxstyle='round', facecolor='wheat'))
        
        anim = animation.FuncAnimation(self.fig, animate, frames=len(traversal_order),
                                      interval=1000, repeat=True)
        plt.tight_layout()
        plt.show()
    
    def _draw_tree_animation(self, root, pos, visited, parent_pos=None):
        if not root:
            return
        
        x, y = pos[id(root)]
        
        if parent_pos:
            px, py = parent_pos
            self.ax.plot([px, x], [py, y], 'k-', linewidth=2, zorder=1)
        
        color = 'lightgreen' if root in visited else 'lightgray'
        if visited and root == visited[-1]:
            color = 'yellow'
        
        circle = Circle((x, y), 0.3, color=color, ec='black', linewidth=2, zorder=2)
        self.ax.add_patch(circle)
        self.ax.text(x, y, str(root.val), ha='center', va='center',
                    fontsize=12, fontweight='bold', zorder=3)
        
        if root.left:
            self._draw_tree_animation(root.left, pos, visited, (x, y))
        if root.right:
            self._draw_tree_animation(root.right, pos, visited, (x, y))
    
    def _inorder_animation(self, node, order):
        if node:
            self._inorder_animation(node.left, order)
            order.append(node)
            self._inorder_animation(node.right, order)
    
    def _preorder_animation(self, node, order):
        if node:
            order.append(node)
            self._preorder_animation(node.left, order)
            self._preorder_animation(node.right, order)
    
    def _postorder_animation(self, node, order):
        if node:
            self._postorder_animation(node.left, order)
            self._postorder_animation(node.right, order)
            order.append(node)


# ============== DEMO EXAMPLES ==============
def demo_binary_tree():
    print("\n" + "="*50)
    print("BINARY TREE DEMO")
    print("="*50)
    
    bt = BinaryTree()
    values = [1, 2, 3, 4, 5, 6, 7]
    for val in values:
        bt.insert(val)
    
    print(f"Inorder: {bt.inorder(bt.root)}")
    print(f"Preorder: {bt.preorder(bt.root)}")
    print(f"Postorder: {bt.postorder(bt.root)}")
    print(f"Level Order: {bt.level_order()}")
    
    viz = TreeVisualizer()
    viz.visualize_tree(bt.root, "Binary Tree")
    viz.animate_traversal(bt.root, 'inorder')

def demo_bst():
    print("\n" + "="*50)
    print("BINARY SEARCH TREE DEMO")
    print("="*50)
    
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)
    
    print(f"Inorder (sorted): {bst.inorder(bst.root)}")
    print(f"Search 40: {'Found' if bst.search(40) else 'Not Found'}")
    print(f"Search 100: {'Found' if bst.search(100) else 'Not Found'}")
    
    viz = TreeVisualizer()
    viz.visualize_tree(bst.root, "Binary Search Tree")
    viz.animate_traversal(bst.root, 'preorder')

def demo_avl():
    print("\n" + "="*50)
    print("AVL TREE DEMO")
    print("="*50)
    
    avl = AVLTree()
    values = [10, 20, 30, 40, 50, 25]
    for val in values:
        avl.insert(val)
    
    print(f"Inorder: {avl.inorder(avl.root)}")
    
    viz = TreeVisualizer()
    viz.visualize_tree(avl.root, "AVL Tree (Self-Balancing)")

def demo_heap():
    print("\n" + "="*50)
    print("MIN HEAP DEMO")
    print("="*50)
    
    min_heap = MinHeap()
    values = [5, 3, 8, 1, 9, 2]
    for val in values:
        min_heap.insert(val)
    
    print(f"Heap array: {min_heap.heap}")
    print(f"Min element: {min_heap.get_min()}")
    print(f"Extract min: {min_heap.extract_min()}")
    print(f"Heap after extraction: {min_heap.heap}")

def demo_trie():
    print("\n" + "="*50)
    print("TRIE DEMO")
    print("="*50)
    
    trie = Trie()
    words = ["apple", "app", "application", "apply", "banana", "band"]
    for word in words:
        trie.insert(word)
    
    print(f"All words: {trie.get_all_words()}")
    print(f"Search 'app': {trie.search('app')}")
    print(f"Search 'appl': {trie.search('appl')}")
    print(f"Starts with 'app': {trie.starts_with('app')}")
    print(f"Starts with 'ban': {trie.starts_with('ban')}")

def demo_segment_tree():
    print("\n" + "="*50)
    print("SEGMENT TREE DEMO")
    print("="*50)
    
    arr = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTree(arr)
    
    print(f"Original array: {arr}")
    print(f"Sum of range [1, 3]: {seg_tree.query(1, 3)}")
    print(f"Sum of range [0, 5]: {seg_tree.query(0, 5)}")
    
    seg_tree.update(2, 10)
    print(f"After updating index 2 to 10")
    print(f"Sum of range [1, 3]: {seg_tree.query(1, 3)}")


