class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        sumDiff = n*(n+1)//2 - sum(nums)
        quadDiff = n*(n+1)*(2*n+1)//6 - sum(i*i for i in nums)

        duplicate = (quadDiff - sumDiff*sumDiff)//2//sumDiff
        missing = (quadDiff + sumDiff*sumDiff)//2//sumDiff

        return [duplicate, missing]