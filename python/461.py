class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        num = x ^ y

        while(num):
            if(num %2 != 0): count+=1
            num >>=1

        return count