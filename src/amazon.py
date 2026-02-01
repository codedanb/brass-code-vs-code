import heapq
from collections import Counter, deque

from src.data_structures import ListNode, TreeNode


class AmazonSolutions:
    """
    Solutions for Amazon DSA problems.
    """

    def min_distance(self, word1: str, word2: str) -> int:
        """
        Calculates the Levenshtein Distance (Edit Distance) between two words.

        Args:
            word1: First string.
            word2: Second string.

        Returns:
            The minimum number of operations (insert, delete, replace) to convert word1 to word2.
        """
        m, n = len(word1), len(word2)
        # DP table initialization
        # dp[i][j] represents min operations to convert word1[:i] to word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases: converting empty string to non-empty requires insertions
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # If chars match, no new operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # If mismatch, take min of:
                    # 1. Insert (dp[i][j-1])
                    # 2. Delete (dp[i-1][j])
                    # 3. Replace (dp[i-1][j-1])
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

        return dp[m][n]

    def reverse_list(self, head: ListNode | None) -> ListNode | None:
        """
        Reverses a singly linked list.

        Args:
            head: Head of the list.

        Returns:
            New head of the reversed list.
        """
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def trap(self, height: list[int]) -> int:
        """
        Computes how much water can be trapped after raining.

        Args:
            height: Elevation map (array of non-negative integers).

        Returns:
            Total amount of trapped water.
        """
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water

    def merge_k_lists(self, lists: list[ListNode | None]) -> ListNode | None:
        """
        Merges k sorted linked lists into one sorted linked list.

        Args:
            lists: List of k sorted linked lists.

        Returns:
            Head of the merged sorted list.
        """
        heap = []

        # Initialize heap with the head of each list
        # We store (val, idx, node) tuple. 'idx' acts as tie-breaker for same values
        # so we don't compare nodes directly (which would fail if not supporting <).
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next

    def is_valid(self, s: str) -> bool:
        """
        Validates parentheses.
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else "#"
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack

    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        """
        Returns the k most frequent elements.
        """
        # O(N) count
        count = Counter(nums)
        # O(N log K) heap
        return heapq.nlargest(k, count.keys(), key=count.get)

    def zigzag_level_order(self, root: TreeNode | None) -> list[list[int]]:
        """
        Returns the zigzag level order traversal of a binary tree.
        """
        if not root:
            return []

        results = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            current_level = deque()

            for _ in range(level_size):
                node = queue.popleft()

                if left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            results.append(list(current_level))
            left_to_right = not left_to_right

        return results

    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Finds the median of two sorted arrays.
        """
        # Ensure nums1 is the smaller array to minimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        start, end = 0, m

        while start <= end:
            partition1 = (start + end) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # If partition1 is 0 it means nothing is there on left side. Use -INF.
            # If partition1 is m it means nothing is there on right side. Use +INF.
            max_left1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float("inf") if partition1 == m else nums1[partition1]

            max_left2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float("inf") if partition2 == n else nums2[partition2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # We have partitioned array at correct place
                if (m + n) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                # We are too far on right side for partition1. Go on left side.
                end = partition1 - 1
            else:
                # We are too far on left side for partition1. Go on right side.
                start = partition1 + 1

        raise ValueError("Input arrays are not sorted")

    def is_subtree(self, root: TreeNode | None, sub_root: TreeNode | None) -> bool:
        """
        Determines if sub_root is a subtree of root.
        """
        if not root:
            return False
        if self._is_same_tree(root, sub_root):
            return True
        return self.is_subtree(root.left, sub_root) or self.is_subtree(root.right, sub_root)

    def _is_same_tree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self._is_same_tree(p.left, q.left) and self._is_same_tree(p.right, q.right)

    def is_palindrome(self, head: ListNode | None) -> bool:
        """
        Checks if a linked list is a palindrome.
        """
        # Edge case: empty or single node
        if not head or not head.next:
            return True

        # 1. Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 3. Compare halves
        left, right = head, prev
        while right:  # Only check right half length
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    def reorder_log_files(self, logs: list[str]) -> list[str]:
        """
        Reorders logs: Letter logs sorted by content then id. Digit logs maintain order.
        """
        letter_logs = []
        digit_logs = []

        for log in logs:
            # "id content..."
            # split(maxsplit=1) -> [id, content]
            id_, content = log.split(" ", 1)
            if content[0].isalpha():
                letter_logs.append((content, id_, log))
            else:
                digit_logs.append(log)

        # Sort letter logs by content, then id
        letter_logs.sort(key=lambda x: (x[0], x[1]))

        return [x[2] for x in letter_logs] + digit_logs

    def find_words(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Word Search II: Finds all words from dictionary in 2D board.
        """
        word_key = "$"
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[word_key] = word

        row_num, col_num = len(board), len(board[0])
        matched_words = []

        def backtracking(row, col, parent):
            letter = board[row][col]
            curr_node = parent[letter]

            # Check for match
            if word_key in curr_node:
                matched_words.append(curr_node[word_key])
                del curr_node[word_key]  # Prevent duplicate adds

            board[row][col] = "#"  # mark visited

            for r_offset, c_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = row + r_offset, col + c_offset
                if (
                    0 <= new_r < row_num
                    and 0 <= new_c < col_num
                    and board[new_r][new_c] in curr_node
                ):
                    backtracking(new_r, new_c, curr_node)

            board[row][col] = letter  # backtrack

            # Optimization: Prune empty nodes
            if not curr_node:
                del parent[letter]

        for r in range(row_num):
            for c in range(col_num):
                if board[r][c] in trie:
                    backtracking(r, c, trie)

        return matched_words

    def word_break(self, s: str, word_dict: list[str]) -> bool:
        """
        Determines if s can be segmented into a space-separated sequence of
        one or more dictionary words.
        """
        word_set = set(word_dict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]

    def int_to_roman(self, num: int) -> str:
        """
        Converts an integer to a roman numeral.
        """
        val_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        roman = []
        for val, symbol in val_map:
            while num >= val:
                roman.append(symbol)
                num -= val
        return "".join(roman)

    def is_substring(self, s: str, t: str) -> int:
        """
        Checks if t is a substring of s (str.find() implementation).
        """
        if not t:
            return 0
        n, m = len(s), len(t)
        for i in range(n - m + 1):
            if s[i : i + m] == t:
                return i
        return -1


class LRUCache:
    """
    LRU Cache implementation using Hash Map + Doubly Linked List.
    """

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # map key -> node
        # dummy head and tail
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = self.Node(key, value)
        self._add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]


class MedianFinder:
    """
    MedianFinder class to find the median from a data stream.
    """

    def __init__(self):
        """
        Initializes the MedianFinder object.
        """
        # Max-heap to store the smaller half of the numbers
        # We invert values to simulate max-heap with Python's min-heap
        self.small = []
        # Min-heap to store the larger half of the numbers
        self.large = []

    def add_num(self, num: int) -> None:
        """
        Adds the integer num from the data stream to the data structure.
        """
        # Allow small heap to grow first
        heapq.heappush(self.small, -num)

        # Ensure every element in small is <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance sizes: small can have at most 1 more element than large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def find_median(self) -> float:
        """
        Returns the median of all elements so far.
        """
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


class MinStack:
    """
    MinStack class to support push, pop, top, and retrieving the minimum element in constant time.
    """

    def __init__(self):
        """
        Initializes the stack.
        """
        # Primary stack stores all elements
        self.stack = []
        # Min stack stores the minimum value at each state
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        Pushes element val onto stack.
        """
        self.stack.append(val)
        # Update min_stack: push the current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Removes the element on the top of the stack.
        """
        if not self.stack:
            return
        val = self.stack.pop()
        # If the popped value is the current minimum, pop from min_stack too
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        """
        Gets the top element of the stack.
        """
        return self.stack[-1]

    def get_min(self) -> int:
        """
        Retrieves the minimum element in the stack.
        """
        return self.min_stack[-1]
