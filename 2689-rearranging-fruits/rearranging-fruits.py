from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        fruit_counter = Counter()
        for fruit_type_a, fruit_type_b in zip(basket1, basket2):
            fruit_counter[fruit_type_a] += 1
            fruit_counter[fruit_type_b] -= 1

        min_fruit_type = min(fruit_counter)
        exchange_list = []

        for fruit_type, count in fruit_counter.items():
            if count % 2:
                return -1
            exchange_list.extend([fruit_type] * (abs(count) // 2))

        exchange_list.sort()
        mid_point = len(exchange_list) // 2
        return sum(min(fruit_type, min_fruit_type * 2) for fruit_type in exchange_list[:mid_point])

        