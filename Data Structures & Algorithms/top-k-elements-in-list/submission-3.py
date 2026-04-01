class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        track = {}
        for num in nums:
            track[num] = track.get(num, 0) + 1
        for num, count in track.items():
            bucket[count].append(num)
        ans = []
        for i in range(len(nums), -1, -1):
            for j in range(len(bucket[i])):
                ans.append(bucket[i][j])
                if len(ans) == k:
                    return ans
        return ans


