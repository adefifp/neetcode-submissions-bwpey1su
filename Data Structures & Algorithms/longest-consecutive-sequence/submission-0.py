class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        track = set(nums)
        for num in nums:
            if (num - 1) not in track:
                length = 1
                curr = num
                while (curr + 1) in track:
                    length += 1
                    curr = curr + 1
                ans = max(length, ans)
        return ans