class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(a):
            if not a or len(a)==1:return 
            n=len(a)
            m=n//2
            L,R=a[:m],a[m:]
            merge(L)
            merge(R)
            i,j,k,m,n=0,0,0,len(L),len(R)
            count=0
            while i<m and j<n:
                #print(L,R,i,j,k)
                if L[i][0]>R[j][0]:
                    a[k]=R[j]
                    count+=1
                    j,k=j+1,k+1
                else:
                    _,idx=L[i]
                    a[k]=L[i]
                    ans[idx]+=count
                    i,k=i+1,k+1
            while i<m:
                _,idx=L[i]
                a[k]=L[i]
                ans[idx]+=count
                i,k=i+1,k+1
            while j<n:
                a[k]=R[j]
                count+=1
                j,k=j+1,k+1
            #print(L,R,ans,a)
            
        a=[(j,i) for i,j in enumerate(nums)]
        ans=[0]*len(nums)
        merge(a)
        return ans
