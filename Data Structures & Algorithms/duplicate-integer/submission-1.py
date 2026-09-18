class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hist = {}

        for i, num in enumerate(nums):
            if num in hist:
                return True
            else:
                hist[num] = i

        return False
        