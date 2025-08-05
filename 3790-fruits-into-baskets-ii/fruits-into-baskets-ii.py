class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (self.n * 4)
        self.build(nums, 0, 0, self.n - 1)
    def build(self, nums, index, lo, hi):
        if lo == hi:
            self.tree[index] = nums[lo]
            return
        mid = (lo + hi) // 2
        self.build(nums, 2 * index + 1, lo, mid)
        self.build(nums, 2 * index + 2, mid + 1, hi)
        self.tree[index] = max(self.tree[2 * index + 1], self.tree[2 * index + 2])
    def update(self, i, val):
        self._update(0, 0, self.n - 1, i, val)
    def _update(self, index, lo, hi, i, val):
        if lo == hi:
            self.tree[index] = val
            return
        mid = (lo + hi) // 2
        if i <= mid:
            self._update(2 * index + 1, lo, mid, i, val)
        else:
            self._update(2 * index + 2, mid + 1, hi, i, val)
        self.tree[index] = max(self.tree[2 * index + 1], self.tree[2 * index + 2])
    def query_first(self, target):
        return self._query_first(0, 0, self.n - 1, target)
    def _query_first(self, index, lo, hi, target):
        if self.tree[index] < target:
            return -1
        if lo == hi:
            self.update(lo, -1)
            return lo
        mid = (lo + hi) // 2
        if self.tree[2 * index + 1] >= target:
            return self._query_first(2 * index + 1, lo, mid, target)
        else:
            return self._query_first(2 * index + 2, mid + 1, hi, target)
class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        ans = 0
        tree = SegmentTree(baskets)
        for fruit in fruits:
            if tree.query_first(fruit) == -1:
                ans += 1
        return ans
