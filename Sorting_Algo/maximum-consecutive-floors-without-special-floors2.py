class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        top += 1
        maximum = 0
        for s in special:
            if s - bottom > maximum:
                maximum = s - bottom
            bottom = s + 1
        if bottom < top:
            if top - bottom > maximum:
                maximum = top - bottom
        return maximum
