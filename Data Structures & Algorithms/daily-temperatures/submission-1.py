class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while temps and temperatures[i] > temps[-1][0]:
                temp, index = temps.pop()
                result[index] = i - index
            temps.append((temperatures[i], i))
        return result


