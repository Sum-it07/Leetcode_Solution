class Solution:
    def romanToInt(self, s: str) -> int:
        
        hash={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        out=0
        for i in range(len(s) - 1):
            if hash[s[i]] < hash[s[i + 1]]:
                out -= hash[s[i]]
            else:
                out += hash[s[i]]
        out += hash[s[-1]]
        return out
            
