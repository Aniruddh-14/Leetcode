class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backtrack(curr: str, open_count: int, close_count: int):
            if len(curr) == 2 * n:
                ans.append(curr)
                return

            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return ans