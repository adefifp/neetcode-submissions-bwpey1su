class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in track:
                return [track[comp], i]
            track[nums[i]] = i
        return []