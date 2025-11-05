class HashTableVisualizer:
    """Visualize hash tables and operations"""
    
    def visualize_chaining(self, hash_table, title="Hash Table with Chaining"):
        """Visualize hash table with separate chaining"""
        fig, ax = plt.subplots(figsize=(14, 10))
        
        box_width = 1.5
        box_height = 0.6
        chain_spacing = 1.8
        
        # Draw table slots
        for i in range(hash_table.size):
            y = hash_table.size - i - 1
            
            # Index box
            index_rect = Rectangle((0, y), box_width, box_height, 
                                   facecolor='lightblue', edgecolor='black', linewidth=2)
            ax.add_patch(index_rect)
            ax.text(box_width/2, y + box_height/2, f'[{i}]', 
                   ha='center', va='center', fontsize=10, fontweight='bold')
            
            # Chain
            current = hash_table.table[i]
            x_offset = 0
            node_count = 0
            
            while current:
                x = box_width + chain_spacing + x_offset
                
                # Node box
                node_rect = FancyBboxPatch((x, y), box_width, box_height,
                                          boxstyle="round,pad=0.05",
                                          facecolor='lightgreen', 
                                          edgecolor='black', linewidth=2)
                ax.add_patch(node_rect)
                
                # Key-value text
                text = f'{current.key}'
                if len(str(text)) > 8:
                    text = str(text)[:6] + '..'
                ax.text(x + box_width/2, y + box_height/2, text,
                       ha='center', va='center', fontsize=9, fontweight='bold')
                
                # Arrow to next
                if current.next:
                    arrow = FancyArrowPatch((x + box_width, y + box_height/2),
                                          (x + box_width + 0.6, y + box_height/2),
                                          arrowstyle='->', mutation_scale=20, 
                                          linewidth=2, color='black')
                    ax.add_patch(arrow)
                
                x_offset += chain_spacing
                node_count += 1
                current = current.next
            
            # Arrow from index to chain
            if hash_table.table[i]:
                arrow = FancyArrowPatch((box_width, y + box_height/2),
                                      (box_width + 0.8, y + box_height/2),
                                      arrowstyle='->', mutation_scale=20,
                                      linewidth=2, color='red')
                ax.add_patch(arrow)
            else:
                ax.text(box_width + 1, y + box_height/2, 'None',
                       ha='left', va='center', fontsize=9, style='italic', color='gray')
        
        # Statistics
        stats_text = f'Size: {hash_table.size} | Count: {hash_table.count} | ' \
                    f'Load Factor: {hash_table.load_factor():.2f} | Collisions: {hash_table.collisions}'
        ax.text(0, hash_table.size + 0.5, stats_text, fontsize=11, 
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        ax.set_xlim(-0.5, 12)
        ax.set_ylim(-0.5, hash_table.size + 1)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
        
        plt.tight_layout()
        plt.show()
    
    def visualize_open_addressing(self, hash_table, title="Hash Table with Open Addressing"):
        """Visualize hash table with open addressing"""
        fig, ax = plt.subplots(figsize=(12, 10))
        
        box_width = 2
        box_height = 0.6
        
        # Draw table slots
        for i in range(hash_table.size):
            y = hash_table.size - i - 1
            
            # Index box
            index_rect = Rectangle((0, y), 1, box_height,
                                   facecolor='lightblue', edgecolor='black', linewidth=2)
            ax.add_patch(index_rect)
            ax.text(0.5, y + box_height/2, f'[{i}]',
                   ha='center', va='center', fontsize=10, fontweight='bold')
            
            # Value box
            if hash_table.table[i] is None:
                color = 'white'
                text = 'None'
                text_color = 'gray'
            elif hash_table.table[i] is hash_table.DELETED:
                color = 'lightcoral'
                text = 'DELETED'
                text_color = 'darkred'
            else:
                key, value = hash_table.table[i]
                color = 'lightgreen'
                text = f'{key}: {value}'
                if len(str(text)) > 15:
                    text = str(text)[:13] + '..'
                text_color = 'black'
            
            value_rect = Rectangle((1.2, y), box_width, box_height,
                                   facecolor=color, edgecolor='black', linewidth=2)
            ax.add_patch(value_rect)
            ax.text(1.2 + box_width/2, y + box_height/2, text,
                   ha='center', va='center', fontsize=9, 
                   fontweight='bold', color=text_color)
        
        # Statistics
        stats_text = f'Probing: {hash_table.probing_method.capitalize()} | ' \
                    f'Size: {hash_table.size} | Count: {hash_table.count} | ' \
                    f'Load Factor: {hash_table.load_factor():.2f} | Collisions: {hash_table.collisions}'
        ax.text(0, hash_table.size + 0.5, stats_text, fontsize=10,
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        ax.set_xlim(-0.5, 4)
        ax.set_ylim(-0.5, hash_table.size + 1)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
        
        plt.tight_layout()
        plt.show()
    
    def compare_collision_methods(self, data):
        """Compare different collision handling methods"""
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('Collision Handling Comparison', fontsize=16, fontweight='bold')
        
        methods = [
            ('chaining', 'Separate Chaining'),
            ('linear', 'Linear Probing'),
            ('quadratic', 'Quadratic Probing'),
            ('double', 'Double Hashing')
        ]
        
        for idx, (method, title) in enumerate(methods):
            ax = axes[idx // 2, idx % 2]
            
            if method == 'chaining':
                ht = HashTableChaining(size=7)
            else:
                ht = HashTableOpenAddressing(size=7, probing=method)
            
            collisions = []
            for key, value in data:
                ht.insert(key, value)
                collisions.append(ht.collisions)
            
            ax.plot(range(len(collisions)), collisions, marker='o', linewidth=2)
            ax.set_xlabel('Number of Insertions', fontsize=10)
            ax.set_ylabel('Total Collisions', fontsize=10)
            ax.set_title(f'{title}\nFinal Collisions: {ht.collisions}', fontsize=11)
            ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
