class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for num, char in enumerate(s):
            if count[char] == 1: return num
        return -1