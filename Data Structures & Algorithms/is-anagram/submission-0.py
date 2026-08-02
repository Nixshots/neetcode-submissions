class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m=[]
        c=[]
        for i in s:
            m.append(i)
        for x in t:
            c.append(x)
        m.sort()
        c.sort()
        if m==c:
            return True
        else:
            return False
