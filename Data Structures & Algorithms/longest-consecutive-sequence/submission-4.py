class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        else:
            former = nums[0]
        longest = 0
        length = 1
        for i in nums[1:]:
            if i == former + 1:
                length += 1
            elif i == former:
                continue
            else:
                longest = max(length, longest)
                length = 1
            former = i                
        longest = max(length, longest)
        return longest

