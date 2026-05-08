class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
        if len(s)!=len(t):
            return False
        count={}
        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        for ch in t:
            if ch in count:
                return True
            else:
                return False
            
        