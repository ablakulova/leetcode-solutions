class Solution:
    def convertToBase7(self, num: int) -> str:
        sign = 1 if num < 0 else 0
        ans, num = "", abs(num)
        while(num):
            num, digit = divmod(num, 7)
            ans += str(digit)
        
        return "-"*sign + ans[::-1] if ans else "0"

