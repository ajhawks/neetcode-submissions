class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            pointer1 = i+1
            pointer2 = len(nums) - 1
            while pointer1 < pointer2:
                target = 0 - nums[i]
                if nums[pointer1] + nums[pointer2] > target:
                    pointer2 -= 1
                elif nums[pointer1] + nums[pointer2] < target:
                    pointer1 += 1
                elif nums[pointer1] + nums[pointer2] == target and [nums[i], nums[pointer1], nums[pointer2]] not in res:
                    res.append([nums[i], nums[pointer1], nums[pointer2]])
                    pointer1 += 1
                    pointer2 -= 1
                else:
                    pointer1 += 1
                    pointer2 -= 1
        return res