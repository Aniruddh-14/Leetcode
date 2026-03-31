class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort() # Crucial for handling duplicates

        def backtrack(start, target, path):
            if target == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # If the current number is greater than the remaining target, 
                # no need to check further (since the array is sorted)
                if candidates[i] > target:
                    break
                
                # Skip duplicates: if the current element is the same as the 
                # previous one in the same recursive level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                # i + 1 because each number can be used only once
                backtrack(i + 1, target - candidates[i], path)
                path.pop() # Clean up for the next iteration

        backtrack(0, target, [])
        return res