class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = []
        maxright = []
        leftend, rightend = 0, 0
        v =0

        for i in range(len(height)):
            b = height[i]
            leftend = max(leftend, b)
            maxleft.append(leftend)
        
        for i in range(len(height)-1, -1, -1):
            b = height[i]
            rightend = max(rightend, b)
            maxright.append(rightend)

        for i in range(len(height)):
            v += min(maxleft[i], maxright[len(height) - 1 - i]) - height[i]
        return v