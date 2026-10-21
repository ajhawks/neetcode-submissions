class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashed = dict()
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in hashed.keys():
                return [hashed.get(complement)+1, i+1]
            hashed[numbers[i]] = i
