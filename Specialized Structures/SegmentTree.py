class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0]*(2*self.n)
        for i in range(self.n):
            self.tree[self.n+i] = arr[i]
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, index, value):
        i = index+self.n
        self.tree[i] = value
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def query(self, left, right):
        left += self.n
        right += self.n
        res = 0
        while left < right:
            if left & 1:
                res += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                res += self.tree[right]
            left //= 2
            right //= 2
        return res

# Test
arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)
assert st.query(1,4) == 15
st.update(2, 10)
assert st.query(1,4) == 20[web:7][web:15]
