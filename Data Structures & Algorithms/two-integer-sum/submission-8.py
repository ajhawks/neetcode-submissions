class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort();
        a, b = 0, len(nums) - 1;

        while A[a][0] + A[b][0] != target:
            if A[a][0] + A[b][0] > target:
                b -= 1;
            else:
                a += 1;
        return [min(A[a][1], A[b][1]), max(A[a][1], A[b][1])];
