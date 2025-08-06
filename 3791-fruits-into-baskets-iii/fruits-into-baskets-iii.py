class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(fruits)
        segment_tree = [0] * (4 * n + 1)

        def update_node(index):
            segment_tree[index] = max(segment_tree[index << 1], segment_tree[index << 1 | 1])

        def build_tree(node_index, left, right):
            if left == right:
                segment_tree[node_index] = baskets[left]
                return
            mid = (left + right) >> 1
            build_tree(node_index << 1, left, mid)
            build_tree(node_index << 1 | 1, mid + 1, right)
            update_node(node_index)

        def assign_value(target_index, value, node_index, left, right):
            if target_index < left or target_index > right:
                return
            if left == right:
                segment_tree[node_index] = value
                return
            mid = (left + right) >> 1
            assign_value(target_index, value, node_index << 1, left, mid)
            assign_value(target_index, value, node_index << 1 | 1, mid + 1, right)
            update_node(node_index)

        def find_first_valid_index(value, node_index, left, right):
            if segment_tree[node_index] < value:
                return right + 1
            if left == right:
                return right
            mid = (left + right) >> 1
            result = find_first_valid_index(value, node_index << 1, left, mid)
            if result <= mid:
                return result
            return find_first_valid_index(value, node_index << 1 | 1, mid + 1, right)

        build_tree(1, 0, n - 1)
        unplaced_fruits = 0

        for fruit_size in fruits:
            position = find_first_valid_index(fruit_size, 1, 0, n - 1)
            if position == n:
                unplaced_fruits += 1
            else:
                assign_value(position, 0, 1, 0, n - 1)

        return unplaced_fruits
