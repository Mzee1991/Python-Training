class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        hashmap2 = {}
        for i in range(n):
            hashmap2[nums2[i]] = i
        indices = []
        for num in nums1:
            indices.append(hashmap2[num])
        from sortedcontainers import SortedList
        left, right = SortedList(), SortedList()
        leftCount, rightCount = [], []
        for i in range(n):
            leftCount.append(left.bisect_left(indices[i]))
            left.add(indices[i])
        for i in range(n - 1, -1, -1):
            rightCount.append(len(right) - right.bisect_right(indices[i]))
            right.add(indices[i])
        count = 0
        for i in range(n):
            count += leftCount[i] * rightCount[n - 1 - i]
        return count
