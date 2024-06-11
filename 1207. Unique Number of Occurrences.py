class Solution(object):
    def uniqueOccurrences(self, arr):
        s = []
        for x in set(arr):
            s.append(arr.count(x))
        return len(set(s)) == len(s)
