class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in track:
                return [track[comp], i]
            track[num] = i
        return []