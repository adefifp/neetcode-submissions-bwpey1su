class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        track1 = {}
        track2 = {}
        for char in s1:
            track1[char] = track1.get(char, 0) + 1
        l, r = 0, 0
        while r<len(s2):
            track2[s2[r]] = track2.get(s2[r], 0) + 1
            if (r - l + 1) > len(s1):
                track2[s2[l]] -= 1
                if track2[s2[l]] == 0:
                    del track2[s2[l]]
                l+=1
            if track1 == track2:
                return True
            r += 1
        return False