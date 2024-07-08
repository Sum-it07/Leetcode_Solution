class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans=""
        for i in range(len(words)):
            if words[i]==words[i][::-1]:
                ans=words[i]
                break
        return ans
