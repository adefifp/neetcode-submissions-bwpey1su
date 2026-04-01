class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if not self.store[key]:
            return ans
        l = 0
        r = len(self.store[key]) - 1
        while l <= r:
            mid = l + (r - l) //2 
            if self.store[key][mid][1] <= timestamp:
                ans = self.store[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return ans
        
