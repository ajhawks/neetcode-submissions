class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        p1 = 0
        p2 = length-1
        while True:
            if numbers[p1] + numbers[p2] > target:
                p2 -= 1
            if numbers[p1] + numbers[p2] < target:
                p1 += 1
            if numbers[p1] + numbers[p2] == target:
                return [p1+1, p2+1]