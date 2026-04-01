class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        track = {}
        n = len(nums)
        for num in nums:
            track[num] = track.get(num, 0) + 1
            if track[num] >= (n/2):
                return num
        