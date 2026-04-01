class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap = []
        track = {}
        for num in nums:
            track[num] = track.get(num,0) +1
        for num, count in track.items():
            heapq.heappush(minheap, (track[num], num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(minheap)[1])
        return ans
