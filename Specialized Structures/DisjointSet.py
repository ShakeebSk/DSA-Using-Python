class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return False  # Cycle detected
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1
        return True

# Test
dsu = DisjointSet(5)
assert dsu.union(0,1)
assert dsu.union(1,2)
assert dsu.find(0) == dsu.find(2)
assert not dsu.union(0,2)  # Cycle (already connected)[web:2][web:3][web:4][web:13]
