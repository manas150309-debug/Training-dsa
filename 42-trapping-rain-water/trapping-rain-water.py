
class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        size = len(h)

        leftMax = [0] * size
        rightMax = [0] * size

        leftMax[0] = h[0]
        rightMax[size - 1] = h[size - 1]

        for index in range(1, size):
            leftMax[index] = max(leftMax[index - 1], h[index])

        for index in range(size - 2, -1, -1):
            rightMax[index] = max(rightMax[index + 1], h[index])

        ans = 0
        for index in range(size):
            ans += min(leftMax[index], rightMax[index]) - h[index]

        return ans