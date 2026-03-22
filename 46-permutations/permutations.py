class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])  # copy
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                # choose
                path.append(nums[i])
                used[i] = True
                
                # explore
                backtrack(path, used)
                
                # un-choose (backtrack)
                path.pop()
                used[i] = False
        
        backtrack([], [False] * len(nums))
        return res
