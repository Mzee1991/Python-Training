class Solution:
    def maxConsecutive(self, x: int, y: int, a: List[int]) -> int:
        a.sort()
        r=max(a[0]-x,y-a[-1])
        for i in range(len(a)-1):
            a[i]=a[i+1]-a[i]
        a[-1]=0
        r=max(max(a)-1,r)
        return r
