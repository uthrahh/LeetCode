class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }     

        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                sum -= roman[a]
            else:
                sum += roman[a]
        
        return sum + roman[s[-1]]

