class FenwickTree:
    def __init__(self, n):
        self.tree = [0]*(n+1)

    def update(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def prefix_sum(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

# Test
ft = FenwickTree(5)
ft.update(1,4)
ft.update(3,7)
assert ft.prefix_sum(1) == 4
assert ft.prefix_sum(3) == 11[web:11][web:18]
