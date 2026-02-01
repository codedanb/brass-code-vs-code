import unittest

from src.amazon import AmazonSolutions, LRUCache, MedianFinder, MinStack
from src.data_structures import ListNode, TreeNode


class TestAmazonSolutions(unittest.TestCase):
    def setUp(self):
        self.sol = AmazonSolutions()

    # 1. Edit Distance
    def test_min_distance(self):
        self.assertEqual(self.sol.min_distance("horse", "ros"), 3)
        self.assertEqual(self.sol.min_distance("intention", "execution"), 5)

    # 2. Reverse Linked List
    def test_reverse_list(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        reversed_head = self.sol.reverse_list(head)
        self.assertEqual(reversed_head.val, 3)
        self.assertEqual(reversed_head.next.val, 2)
        self.assertEqual(reversed_head.next.next.val, 1)

    # 3. Trapping Rain Water
    def test_trap(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(self.sol.trap(height), 6)

    # 4. Merge K Sorted Lists
    def test_merge_k_lists(self):
        l1 = ListNode(1, ListNode(4, ListNode(5)))
        l2 = ListNode(1, ListNode(3, ListNode(4)))
        l3 = ListNode(2, ListNode(6))
        merged = self.sol.merge_k_lists([l1, l2, l3])
        vals = []
        while merged:
            vals.append(merged.val)
            merged = merged.next
        self.assertEqual(vals, [1, 1, 2, 3, 4, 4, 5, 6])

    # 5. Valid Parentheses
    def test_is_valid(self):
        self.assertTrue(self.sol.is_valid("()[]{}"))
        self.assertFalse(self.sol.is_valid("(]"))

    # 6. LRU Cache
    def test_lru_cache(self):
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(2, 2)
        self.assertEqual(lru.get(1), 1)
        lru.put(3, 3)  # evicts 2
        self.assertEqual(lru.get(2), -1)
        lru.put(4, 4)  # evicts 1
        self.assertEqual(lru.get(1), -1)
        self.assertEqual(lru.get(3), 3)
        self.assertEqual(lru.get(4), 4)

    # 7. Top K Frequent
    def test_top_k_frequent(self):
        nums = [1, 1, 1, 2, 2, 3]
        result = self.sol.top_k_frequent(nums, 2)
        self.assertTrue(set(result) == {1, 2})

    # 8. Zigzag Level Order
    def test_zigzag_level_order(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(self.sol.zigzag_level_order(root), [[3], [20, 9], [15, 7]])

    # 9. Median of Two Sorted Arrays
    def test_find_median_sorted_arrays(self):
        self.assertEqual(self.sol.find_median_sorted_arrays([1, 3], [2]), 2.0)
        self.assertEqual(self.sol.find_median_sorted_arrays([1, 2], [3, 4]), 2.5)

    # 10. Find Median Data Stream
    def test_median_finder(self):
        mf = MedianFinder()
        mf.add_num(1)
        mf.add_num(2)
        self.assertEqual(mf.find_median(), 1.5)
        mf.add_num(3)
        self.assertEqual(mf.find_median(), 2.0)

    # 11. Subtree of Another Tree
    def test_is_subtree(self):
        root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
        sub = TreeNode(4, TreeNode(1), TreeNode(2))
        self.assertTrue(self.sol.is_subtree(root, sub))
        root.left.right.val = 0
        self.assertFalse(self.sol.is_subtree(root, sub))

    # 12. Palindrome Linked List
    def test_is_palindrome(self):
        head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
        self.assertTrue(self.sol.is_palindrome(head))
        head.val = 3
        self.assertFalse(self.sol.is_palindrome(head))

    # 13. Reorder Data in Log Files
    def test_reorder_log_files(self):
        logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
        expected = ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
        self.assertEqual(self.sol.reorder_log_files(logs), expected)

    # 14. Word Search II
    def test_find_words(self):
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        words = ["oath", "pea", "eat", "rain"]
        result = self.sol.find_words(board, words)
        self.assertTrue(set(result) == {"eat", "oath"})

    # 15. Word Break
    def test_word_break(self):
        s = "leetcode"
        word_dict = ["leet", "code"]
        self.assertTrue(self.sol.word_break(s, word_dict))

        s = "applepenapple"
        word_dict = ["apple", "pen"]
        self.assertTrue(self.sol.word_break(s, word_dict))

        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(self.sol.word_break(s, word_dict))

    # 10. Integer to Roman
    def test_int_to_roman(self):
        self.assertEqual(self.sol.int_to_roman(3), "III")
        self.assertEqual(self.sol.int_to_roman(58), "LVIII")
        self.assertEqual(self.sol.int_to_roman(1994), "MCMXCIV")

    # 14. Is Substring
    def test_is_substring(self):
        self.assertEqual(self.sol.is_substring("sadbutsad", "sad"), 0)
        self.assertEqual(self.sol.is_substring("leetcode", "leeto"), -1)

    # 9. Min Stack
    def test_min_stack(self):
        ms = MinStack()
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        self.assertEqual(ms.get_min(), -3)
        ms.pop()
        self.assertEqual(ms.top(), 0)
        self.assertEqual(ms.get_min(), -2)


if __name__ == "__main__":
    unittest.main()
