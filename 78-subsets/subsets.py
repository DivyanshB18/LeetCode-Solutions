class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def solve(ind, subset):
            if ind >= len(nums):
                result.append(subset[:])
                return

            subset.append(nums[ind])
            solve(ind + 1, subset)

            subset.pop()

            solve(ind + 1, subset)

        solve(0, [])
        return result