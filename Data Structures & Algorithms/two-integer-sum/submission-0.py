class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        note = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in note:
                return [note[complement], i]

            else:
                note[num] = i
        