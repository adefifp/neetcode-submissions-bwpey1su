class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        track = set(nums)
        for num in track:
            if num-1 not in track:
                temp = 1
                start = num
                while (start + temp) in track:
                    temp+=1
                ans = max(ans, temp)
        return ans
