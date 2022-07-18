class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i=0
        for _ in range(len(nums)):
            if(nums[i]==2):
                nums.pop(i)
                nums.append(2)
            elif(nums[i]==0):
                nums.pop(i)
                nums.insert(0,0)
                i+=1
            else:
                i+=1
