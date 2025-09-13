class Solution:
    def doesAliceWin(self, s: str) -> bool:
         VOWELS = 'aeiou'
         return any(c in VOWELS for c in s)
        