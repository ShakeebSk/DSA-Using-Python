def subsets(nums):
    res = []
    def backtrack(index, path):
        res.append(path[:])
        for i in range(index, len(nums)):
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0,[])
    return res

# Test
assert subsets([1,2]) == [[],[1],[1,2],[2]]
assert len(subsets([1,2,3])) == 8[web:29][web:35]
