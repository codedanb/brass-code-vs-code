import unittest

from src.data_structures import ListNode, TreeNode
from src.microsoft import MicrosoftSolutions, SeatManager


class TestMicrosoftSolutions(unittest.TestCase):
    def setUp(self):
        self.sol = MicrosoftSolutions()

    # --- Master List (topics.md) Tests 1-9 ---

    def test_largest_rectangle_area(self):
        self.assertEqual(self.sol.largest_rectangle_area([2, 1, 5, 6, 2, 3]), 10)

    def test_has_cycle(self):
        head = ListNode(3)
        head.next = ListNode(2)
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(-4)
        head.next.next.next.next = head.next
        self.assertTrue(self.sol.has_cycle(head))
        self.assertFalse(self.sol.has_cycle(ListNode(1)))

    def test_group_anagrams(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        res = self.sol.group_anagrams(strs)
        self.assertEqual(len(res), 3)

    def test_letter_combinations(self):
        self.assertEqual(
            set(self.sol.letter_combinations("23")),
            {"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"},
        )

    def test_is_valid_sudoku(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertTrue(self.sol.is_valid_sudoku(board))

    def test_word_search(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        self.assertTrue(self.sol.word_search(board, "ABCCED"))

    def test_min_depth(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(self.sol.min_depth(root), 2)

    def test_rotate_array(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        self.sol.rotate_array(nums, 3)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_longest_palindrome(self):
        self.assertEqual(self.sol.longest_palindrome("babad"), "bab")  # or search aba
        self.assertEqual(self.sol.longest_palindrome("cbbd"), "bb")

    # --- End Master List Tests ---

    # 1. Eval RPN
    def test_eval_rpn(self):
        self.assertEqual(self.sol.eval_rpn(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(self.sol.eval_rpn(["4", "13", "5", "/", "+"]), 6)

    # 2. Combination Sum III
    def test_combination_sum_3(self):
        res = self.sol.combination_sum_3(3, 7)
        self.assertEqual(res, [[1, 2, 4]])

    # 3. Bulls and Cows
    def test_get_hint(self):
        self.assertEqual(self.sol.get_hint("1807", "7810"), "1A3B")
        self.assertEqual(self.sol.get_hint("1123", "0111"), "1A1B")

    # 4. Rotate Function
    def test_rotate_function(self):
        self.assertEqual(self.sol.rotate_function([4, 3, 2, 6]), 26)

    # 5. Largest Divisible Subset
    def test_largest_divisible_subset(self):
        res = self.sol.largest_divisible_subset([1, 2, 3])
        self.assertTrue(res in [[1, 2], [1, 3]])  # Either is valid
        res2 = self.sol.largest_divisible_subset([1, 2, 4, 8])
        self.assertEqual(res2, [1, 2, 4, 8])

    # 6. Perfect Rectangle
    def test_is_rectangle_cover(self):
        rects = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
        self.assertTrue(self.sol.is_rectangle_cover(rects))
        rects_bad = [[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]
        self.assertFalse(self.sol.is_rectangle_cover(rects_bad))

    # 7. Course Schedule
    def test_can_finish(self):
        self.assertTrue(self.sol.can_finish(2, [[1, 0]]))
        self.assertFalse(self.sol.can_finish(2, [[1, 0], [0, 1]]))

    # 8. Most Profitable Path
    def test_most_profitable_path(self):
        edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
        bob = 3
        amount = [-2, 4, 2, -4, 6]
        self.assertEqual(self.sol.most_profitable_path(edges, bob, amount), 6)

    # 9. Number of Pairs Inequality
    def test_number_of_pairs(self):
        nums1 = [3, 2, 5]
        nums2 = [2, 2, 1]
        diff = 1
        self.assertEqual(self.sol.number_of_pairs(nums1, nums2, diff), 3)

    # 10. Shortest Unsorted Subarray
    def test_find_unsorted_subarray(self):
        self.assertEqual(self.sol.find_unsorted_subarray([2, 6, 4, 8, 10, 9, 15]), 5)
        self.assertEqual(self.sol.find_unsorted_subarray([1, 2, 3, 4]), 0)

    def test_count_paths(self):
        n = 7
        roads = [
            [0, 6, 7],
            [0, 1, 2],
            [1, 2, 3],
            [1, 3, 3],
            [6, 3, 3],
            [3, 5, 1],
            [6, 5, 1],
            [2, 5, 1],
            [0, 4, 5],
            [4, 6, 2],
        ]
        # 0->6 (7), 0->1->2->5->6 (2+3+1+1=7), 0->1->3->5->6 (2+3+1+1=7), 0->4->6 (5+2=7)
        # Wait, exact example from problem:
        # n=7, roads above.
        # Shortest time is 7.
        # Paths:
        # 0-6 (7)
        # 0-4-6 (7)
        # 0-1-2-5-6 (7)
        # 0-1-3-5-6 (7)
        self.assertEqual(self.sol.count_paths(n, roads), 4)

    def test_longest_prefix(self):
        self.assertEqual(self.sol.longest_prefix("level"), "l")
        self.assertEqual(self.sol.longest_prefix("ababab"), "abab")

    def test_seat_manager(self):
        sm = SeatManager(5)
        self.assertEqual(sm.reserve(), 1)
        self.assertEqual(sm.reserve(), 2)
        sm.unreserve(2)
        self.assertEqual(sm.reserve(), 2)
        self.assertEqual(sm.reserve(), 3)
        self.assertEqual(sm.reserve(), 4)
        self.assertEqual(sm.reserve(), 5)
        sm.unreserve(5)

    def test_rotate(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.sol.rotate(matrix)
        self.assertEqual(matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_nth_person(self):
        self.assertEqual(self.sol.nth_person_gets_nth_seat(1), 1.0)
        self.assertEqual(self.sol.nth_person_gets_nth_seat(2), 0.5)
        self.assertEqual(self.sol.nth_person_gets_nth_seat(100), 0.5)

    def test_combination_sum(self):
        self.assertEqual(self.sol.combination_sum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])

    def test_is_valid_palindrome(self):
        self.assertTrue(self.sol.is_valid_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(self.sol.is_valid_palindrome("race a car"))

    def test_delete_node(self):
        head = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
        # delete 5
        self.sol.delete_node(head.next)
        self.assertEqual(head.val, 4)
        self.assertEqual(head.next.val, 1)

    def test_max_profit(self):
        self.assertEqual(self.sol.max_profit([7, 1, 5, 3, 6, 4]), 5)

    def test_spiral_order(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.sol.spiral_order(matrix), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_right_side_view(self):
        root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
        self.assertEqual(self.sol.right_side_view(root), [1, 3, 4])


if __name__ == "__main__":
    unittest.main()
