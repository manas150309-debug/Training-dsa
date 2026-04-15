class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # get height of the tree
        h = 0
        cur = root
        while cur.left:
            cur = cur.left
            h += 1

        # max number of leaves at last level
        maxi = 2**h

        # check if particular leaf at the last level exists; leaf is a number in [1..2^h]
        # O(logn)
        def exists(leaf: int) -> bool:
            cur = root
            l, r = 1, maxi
            while l < r:
                mid = (l + r) // 2
                if leaf > mid:
                    cur = cur.right
                    l = mid + 1
                else:
                    cur = cur.left
                    r = mid
            
            return cur is not None

        # binary search the number of leaves at last level
        # BS is O(logn), calling 'exists' on every step makes total TC O(logn * logn)
        l, r = 1, maxi
        while l <= r:
            mid = (l + r) // 2

            if exists(mid):
                l = mid + 1
            else:
                r = mid - 1

        # 2**h - 1 is the number of nodes in the tree without the last level
        # r is the number of leaves at the last level
        return 2**h - 1 + r