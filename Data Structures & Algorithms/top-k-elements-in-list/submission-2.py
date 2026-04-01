class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        track = {}
        for num in nums:
            track[num] = track.get(num,0) + 1
        for num, count in track.items():
            heapq.heappush(min_heap, [count, num])
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(min_heap)[1])
        return ans

