class Solution:
    def climbStairs(self, n: int) -> int:
        d={}
        def rec(n):
            if n<=2:
                return n
            if n in d:
                return d[n]
            temp= rec(n-1)+ rec(n-2)
            d[n]=temp
            return temp
        return rec(n)





        
      