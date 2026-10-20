class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        indicator = 0
        for i in nums:
            if i != 0:
                total *= i
            else:
                indicator += 1
        res = [int(total / x) if indicator == 0 else total if x == 0 and indicator == 1 else 0 for x in nums]
        return res
            