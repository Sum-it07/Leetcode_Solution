class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        result = []

        for word in sentence.split():
            prefix = ''
            replaced = False
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in dictionary:
                    result.append(prefix)
                    replaced = True
                    break
            if not replaced:
                result.append(word)
                
        return ' '.join(result)
