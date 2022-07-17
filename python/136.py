class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xOr = 0
        
        for num in nums:
            xOr ^= num
        return xOr