class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        res = 0
        special = sorted(special)
        for i,s in enumerate(special):
            res = max(res, s-bottom)
            bottom = s+1
            # print('i,s, res ', i,s,res)
        
        res = max(res, top - special[-1])
        return res
