class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        for x in nums:
            if x != nums[k - 1]:
                nums[k] = x
                k += 1
        return k