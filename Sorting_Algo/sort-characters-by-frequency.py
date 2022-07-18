class Solution:
    def frequencySort(self, s: str) -> str:
        d = collections.Counter(s)
        items = sorted(d, key=d.get, reverse=True)
        #pritn(items)
        res = ''
        for c in items:
            res += c*d[c]
        return res
