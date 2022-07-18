class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return self.mergesort(nums)[1]
    
    def mergesort(self, nums):
        if len(nums) <= 1:
            return nums,0
        m = len(nums)//2
        left, countl = self.mergesort(nums[:m])
        right,countr = self.mergesort(nums[m:])
        count = countl + countr
        for r in right:
            temp =len(left) - bisect.bisect(left, 2*r)
            if temp == 0:
                break
            count += temp
        return sorted(left+right),count
