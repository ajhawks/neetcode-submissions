class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_list = set()
        for i in nums:
            if i in my_list:
                return True
            else:
                my_list.add(i)
        return False
        