class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        track = {}
        most_count = 0
        for r in range(len(s)):
            track[s[r]] = track.get(s[r], 0) + 1
            most_count = max(most_count, track[s[r]])
            while (r - l + 1 - most_count) > k:
                track[s[l]] -= 1
                l += 1
        return (len(s) - l) 