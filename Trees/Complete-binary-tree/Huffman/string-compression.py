class Solution:
    def compress(self, chars: List[str]) -> int:
        cur_c = None
        cur_len = 0
        
        pos = 0
        for c in chars + ['##']:
            if c == cur_c:
                cur_len += 1
            else:
                if cur_len > 0:
                    chars[pos] = cur_c
                    pos += 1
                if cur_len >= 2:
                    digits = []
                    while cur_len > 0:
                        digits.append(cur_len % 10)
                        cur_len //= 10
                    
                    while digits:
                        d = digits.pop()
                        chars[pos] = str(d)
                        pos += 1

                cur_c = c
                cur_len = 1
        return pos
