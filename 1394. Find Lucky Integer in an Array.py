class Solution:
    def findLucky(self, arr: List[int]) -> int:
        store=[]
        only=list(set(arr))
        for i in range(len(only)):
            if only[i]==arr.count(only[i]):
                store.append(only[i])
        if len(store)==0:
            return -1
        if len(store)==1:
            return store[0]
        res=store[0]
        for i in range(1,len(store)):
            if arr.count(store[i])>arr.count(store[i-1]):
                res=store[i]
        return res
        


