def permutations(nums):
    res = []
    def backtrack(path, remaining):
        if not remaining:
            res.append(path)
            return
        for i in range(len(remaining)):
            backtrack(path+[remaining[i]], remaining[:i]+remaining[i+1:])
    backtrack([], nums)
    return res

# Test
assert sorted(permutations([1,2,3])) == sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
assert len(permutations([1,2,3,4])) == 24[web:30][web:36]
