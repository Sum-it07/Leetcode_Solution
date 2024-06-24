class Solution:
    def clearDigits(self, s: str) -> str:
        new=['1','2','3','4','5','6','7','8','9','0']
        string=''
        for i in s:
            if i not in new:
                string+=i
            if i in new:
                string=string[:len(string)-1]
        return string
