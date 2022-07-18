class Solution:
    def maximumGap(self, n: List[int]) -> int:
        
        if len(n) == 1: return 0
        n = sorted(n)
        tmp = n[0]
        dif = -1
        
        for i in range(1, len(n)):
            dif = n[i] - tmp if n[i] - tmp > dif else dif
            tmp = n[i]
        return dif
