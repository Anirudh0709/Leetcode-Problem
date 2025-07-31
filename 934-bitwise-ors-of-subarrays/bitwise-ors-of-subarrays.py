class Solution:
    def subarrayBitwiseORs(self, arr):
        result = set()
        current = set()

        for num in arr:
            new_current = {num}
            for val in current:
                new_current.add(val | num)
            current = new_current
            result |= current

        return len(result)
