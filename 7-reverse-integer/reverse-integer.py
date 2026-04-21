class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        flag = False
        if x < 0:
            flag = True
            x = -x
        while x:
            rem = x % 10
            rev = rev * 10 + rem
            x = x // 10
        if flag:
            rev = -rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        return rev