class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        max_fruits = window_start = total_fruits = 0

        for window_end, (position_j, fruits_at_j) in enumerate(fruits):
            total_fruits += fruits_at_j

            while (
                window_start <= window_end
                and position_j - fruits[window_start][0]
                + min(abs(startPos - fruits[window_start][0]), abs(startPos - position_j))
                > k
            ):
                total_fruits -= fruits[window_start][1]
                window_start += 1

            max_fruits = max(max_fruits, total_fruits)

        return max_fruits
