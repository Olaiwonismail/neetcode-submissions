class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []  # indices, temperatures decreasing
        for n, item in enumerate(temperatures):
            while stack and item > temperatures[stack[-1]]:
                i = stack.pop()
                output[i] = n - i
            stack.append(n)
        return output