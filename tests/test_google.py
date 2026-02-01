import unittest

from src.data_structures import ListNode, TreeNode
from src.google import GoogleSolutions, MedianFinder


class TestGoogleSolutions(unittest.TestCase):
    def setUp(self):
        self.sol = GoogleSolutions()

    # 1. Two Sum
    def test_two_sum(self):
        self.assertEqual(self.sol.two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(self.sol.two_sum([3, 2, 4], 6), [1, 2])

    # 2. Binary Tree Level Order
    def test_level_order(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(self.sol.level_order(root), [[3], [9, 20], [15, 7]])

    # 3. Longest Substring No Repeats
    def test_length_of_longest_substring(self):
        self.assertEqual(self.sol.length_of_longest_substring("abcabcbb"), 3)
        self.assertEqual(self.sol.length_of_longest_substring("bbbbb"), 1)

    # 4. Kth Largest
    def test_find_kth_largest(self):
        self.assertEqual(self.sol.find_kth_largest([3, 2, 1, 5, 6, 4], 2), 5)

    # 5. Merge Intervals
    def test_merge(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(self.sol.merge(intervals), expected)

    # 6. Search Rotated Sorted
    def test_search(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(self.sol.search(nums, 0), 4)
        self.assertEqual(self.sol.search(nums, 3), -1)

    # 7. Valid Parentheses
    def test_is_valid_parentheses(self):
        self.assertTrue(self.sol.is_valid_parentheses("()[]{}"))
        self.assertFalse(self.sol.is_valid_parentheses("(]"))

    # 8. Word Ladder
    def test_ladder_length(self):
        begin = "hit"
        end = "cog"
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        self.assertEqual(self.sol.ladder_length(begin, end, word_list), 5)

    # 9. Container Most Water
    def test_max_area(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(self.sol.max_area(height), 49)

    # 10. Subset Sum II
    def test_subsets_with_dup(self):
        nums = [1, 2, 2]
        result = self.sol.subsets_with_dup(nums)
        # Convert inner lists to tuples for set comparison
        result_set = {tuple(sorted(sub)) for sub in result}
        expected_set = {(), (1,), (2,), (1, 2), (2, 2), (1, 2, 2)}
        self.assertEqual(result_set, expected_set)

    # 11. Median Finder
    def test_median_finder(self):
        mf = MedianFinder()
        mf.add_num(1)
        mf.add_num(2)
        self.assertEqual(mf.find_median(), 1.5)
        mf.add_num(3)
        self.assertEqual(mf.find_median(), 2.0)

    # 12. Min Window Substring
    def test_min_window(self):
        self.assertEqual(self.sol.min_window("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(self.sol.min_window("a", "aa"), "")

    # 13. Reverse K Group
    def test_reverse_k_group(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        # k=2 -> 2-1-4-3-5
        new_head = self.sol.reverse_k_group(head, 2)
        vals = []
        curr = new_head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        self.assertEqual(vals, [2, 1, 4, 3, 5])

    # 14. Find Min Rotated
    def test_find_min(self):
        self.assertEqual(self.sol.find_min([3, 4, 5, 1, 2]), 1)
        self.assertEqual(self.sol.find_min([11, 13, 15, 17]), 11)


if __name__ == "__main__":
    unittest.main()
