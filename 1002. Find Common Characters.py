class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_count = {char: words[0].count(char) for char in set(words[0])}
        for word in words[1:]:
            word_count = {char: word.count(char) for char in set(word)}
            common_count = {char: min(common_count[char], word_count[char]) for char in common_count if char in word_count}
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)

        return result    
