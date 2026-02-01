import heapq
from collections import Counter, deque

from src.data_structures import ListNode, TreeNode


class MicrosoftSolutions:
    """
    Solutions for Microsoft DSA problems.
    """

    # --- Master List (topics.md) Problems 1-9 ---

    def largest_rectangle_area(self, heights: list[int]) -> int:
        """
        Largest Rectangle in Histogram: Returns area of largest rectangle.
        """
        stack = [-1]
        max_area = 0
        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= h:
                curr_h = heights[stack.pop()]
                curr_w = i - stack[-1] - 1
                max_area = max(max_area, curr_h * curr_w)
            stack.append(i)

        while stack[-1] != -1:
            curr_h = heights[stack.pop()]
            curr_w = len(heights) - stack[-1] - 1
            max_area = max(max_area, curr_h * curr_w)
        return max_area

    def has_cycle(self, head: ListNode | None) -> bool:
        """
        Linked List Cycle: Determines if a list has a cycle using Floyd's.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Group Anagrams: Groups strings that are anagrams of each other.
        """
        anagrams = {}
        for s in strs:
            key = "".join(sorted(s))
            anagrams.setdefault(key, []).append(s)
        return list(anagrams.values())

    def letter_combinations(self, digits: str) -> list[str]:
        """
        Letter Combinations of a Phone Number: Returns all possible letter strings.
        """
        if not digits:
            return []
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtrack(index, path):
            if index == len(digits):
                res.append("".join(path))
                return
            for char in digit_map[digits[index]]:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return res

    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        """
        Valid Sudoku: Validates a 9x9 Sudoku board.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                box_idx = (r // 3) * 3 + (c // 3)
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
        return True

    def word_search(self, board: list[list[str]], word: str) -> bool:
        """
        Word Search: Finds if word exists in grid.
        """
        rows, cols = len(board), len(board[0])

        def dfs(r, c, k):
            if k == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[k]:
                return False
            temp = board[r][c]
            board[r][c] = "#"  # Visited
            res = (
                dfs(r + 1, c, k + 1)
                or dfs(r - 1, c, k + 1)
                or dfs(r, c + 1, k + 1)
                or dfs(r, c - 1, k + 1)
            )
            board[r][c] = temp
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False

    def min_depth(self, root: TreeNode | None) -> int:
        """
        Minimum Depth of Binary Tree: Returns shortest path to leaf.
        """
        if not root:
            return 0
        if not root.left:
            return self.min_depth(root.right) + 1
        if not root.right:
            return self.min_depth(root.left) + 1
        return min(self.min_depth(root.left), self.min_depth(root.right)) + 1

    def rotate_array(self, nums: list[int], k: int) -> None:
        """
        Rotate Array: Rotates array to the right by k steps in-place.
        """
        n = len(nums)
        k %= n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

    def longest_palindrome(self, s: str) -> str:
        """
        Largest Palindromic Substring: Returns the longest palindrome.
        """
        if not s:
            return ""

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        res = ""
        for i in range(len(s)):
            p1 = expand(i, i)
            if len(p1) > len(res):
                res = p1
            p2 = expand(i, i + 1)
            if len(p2) > len(res):
                res = p2
        return res

    # --- End Master List ---

    def eval_rpn(self, tokens: list[str]) -> int:
        """
        Evaluate Reverse Polish Notation.
        """
        stack: list[int] = []
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Python's // floor divides, but we need truncation towards zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]

    def combination_sum_3(self, k: int, n: int) -> list[list[int]]:
        """
        Find all valid combinations of k numbers that sum up to n.
        """
        results = []

        def backtrack(start: int, current_comb: list[int], current_sum: int):
            if len(current_comb) == k:
                if current_sum == n:
                    results.append(list(current_comb))
                return

            if current_sum > n:
                return

            for i in range(start, 10):
                current_comb.append(i)
                backtrack(i + 1, current_comb, current_sum + i)
                current_comb.pop()

        backtrack(1, [], 0)
        return results

    def get_hint(self, secret: str, guess: str) -> str:
        """
        Bulls and Cows game hint.
        """
        bulls = 0
        cows = 0
        secret_counts = Counter(secret)
        guess_counts = Counter(guess)

        # Calculate Bulls
        for s, g in zip(secret, guess, strict=False):
            if s == g:
                bulls += 1
                # Decrement counts for bulls so they aren't counted as cows
                secret_counts[s] -= 1
                guess_counts[g] -= 1

        # Calculate Cows
        for char, count in guess_counts.items():
            if char in secret_counts:
                # Cows is min of remaining available in secret vs guess
                cows += min(count, secret_counts[char])

        return f"{bulls}A{cows}B"

    def rotate_function(self, nums: list[int]) -> int:
        """
        Calculate maximum value of F(k) for rotation function.
        F(k) = 0*arr[0] + 1*arr[1] + ... + (n-1)*arr[n-1]
        """
        n = len(nums)
        s = sum(nums)
        f_0 = sum(i * num for i, num in enumerate(nums))

        max_f = f_0
        current_f = f_0

        # F(k) = F(k-1) + sum - n * nums[n-k]
        # Iterate k from 1 to n-1
        # The element moving from end to start is nums[n-k]
        for k in range(1, n):
            current_f = current_f + s - n * nums[n - k]
            max_f = max(max_f, current_f)

        return max_f

    def largest_divisible_subset(self, nums: list[int]) -> list[int]:
        """
        Returns largest subset where every pair (a, b) satisfies a % b == 0 or b % a == 0.
        """
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        # dp[i] stores the size of largest divisible subset ending at index i
        dp = [1] * n
        # prev[i] stores the index of the previous element in the subset
        prev = [-1] * n

        max_size = 1
        max_index = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i

        # Reconstruct path
        result = []
        curr = max_index
        while curr != -1:
            result.append(nums[curr])
            curr = prev[curr]

        return result[::-1]

    def is_rectangle_cover(self, rectangles: list[list[int]]) -> bool:
        """
        Check if all rectangles form an exact cover of a rectangular region.
        """
        area = 0
        corners = set()
        min_x, min_y = float("inf"), float("inf")
        max_x, max_y = float("-inf"), float("-inf")

        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            # XOR corners to cancel out internal overlaps
            # A corner is internal if it appears 2 or 4 times.
            # It's an outer corner if it appears 1 time (or 3, but 3 implies overlap/error usually).
            # We track "presence" with set logic:
            # if in set, remove it (even count), else add (odd count).
            # Actually proper way: count occurrences. But efficient way:
            current_corners = {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
            for c in current_corners:
                if c in corners:
                    corners.remove(c)
                else:
                    corners.add(c)

        # Check 1: Area match
        if area != (max_x - min_x) * (max_y - min_y):
            return False

        # Check 2: Exact 4 corners remaining
        if len(corners) != 4:
            return False

        # Check 3: The 4 corners must be the bounding box corners
        return corners == {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}

    def can_finish(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        """
        Course Schedule: Detect cycle in directed graph.
        """
        adj = [[] for _ in range(num_courses)]
        for course, pre in prerequisites:
            adj[pre].append(course)

        # 0: unvisited, 1: visiting (current path), 2: visited (safe)
        state = [0] * num_courses

        def has_cycle(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False

            state[node] = 1
            for neighbor in adj[node]:
                if has_cycle(neighbor):
                    return True
            state[node] = 2
            return False

        return all(not has_cycle(i) for i in range(num_courses))

    def most_profitable_path(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        """
        Find max net income for Alice traveling from 0 to leaf. Bob travels from 'bob' to 0.
        """
        n = len(amount)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 1. Find Bob's path and arrival times
        bob_time = {}  # node -> time
        visited = [False] * n
        visited[bob] = True

        # DFS to find path from Bob to 0 to record times
        # Actually DFS is better to map the exact path
        def find_bob_path(node, time):
            bob_time[node] = time
            if node == 0:
                return True

            for neighbor in adj[node]:
                if neighbor not in bob_time and find_bob_path(neighbor, time + 1):
                    return True
            del bob_time[node]
            return False

        find_bob_path(bob, 0)

        # 2. DFS for Alice
        max_profit = float("-inf")
        visited = [False] * n

        def alice_dfs(node, time, current_profit):
            nonlocal max_profit
            visited[node] = True

            # Calculate profit at this node
            node_profit = 0
            if node not in bob_time or time < bob_time[node]:
                node_profit = amount[node]
            elif time == bob_time[node]:
                node_profit = amount[node] // 2
            else:
                node_profit = 0

            current_profit += node_profit

            # Leaf check (excluding root unless it is isolated)
            is_leaf = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    is_leaf = False
                    alice_dfs(neighbor, time + 1, current_profit)

            if is_leaf:
                max_profit = max(max_profit, current_profit)

        alice_dfs(0, 0, 0)
        return int(max_profit)

    def number_of_pairs(self, nums1: list[int], nums2: list[int], diff: int) -> int:
        """
        Count pairs (i, j) where i < j and nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.
        Equivalent to: (nums1[i] - nums2[i]) <= (nums1[j] - nums2[j]) + diff.
        Let d[k] = nums1[k] - nums2[k]. Find i < j such that d[i] <= d[j] + diff.
        """
        d = [n1 - n2 for n1, n2 in zip(nums1, nums2, strict=False)]

        # Use Merge Sort to count valid pairs
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2
            left, left_count = merge_sort(arr[:mid])
            right, right_count = merge_sort(arr[mid:])

            count = left_count + right_count

            # Count pairs
            # For each x in left, find how many y in right satisfy x <= y + diff  =>  x - diff <= y
            # Since right is sorted, we can use two pointers or bisect
            r_idx = 0
            for x in left:
                while r_idx < len(right) and right[r_idx] < x - diff:
                    r_idx += 1
                # All elements from r_idx onwards satisfy right[k] >= x - diff
                count += len(right) - r_idx

            # Merge
            sorted_arr = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    sorted_arr.append(left[i])
                    i += 1
                else:
                    sorted_arr.append(right[j])
                    j += 1
            sorted_arr.extend(left[i:])
            sorted_arr.extend(right[j:])

            return sorted_arr, count

        _, total_pairs = merge_sort(d)
        return total_pairs

    def find_unsorted_subarray(self, nums: list[int]) -> int:
        """
        Find shortest continuous subarray that if sorted sorts the whole array.
        """
        n = len(nums)
        if n <= 1:
            return 0

        # Find minimum index 'start' where order breaks from left
        start = -1
        max_val = float("-inf")
        for i in range(n):
            if nums[i] < max_val:
                # Assuming simple case: comparing to sorted version?
                # Optimization: one pass logic
                pass
            max_val = max(max_val, nums[i])

        # Simpler O(N) approach:
        # Scan from left to find first element not matching sorted order
        # Scan from right to find first element not matching sorted order
        # Actually easier: Create sorted copy, compare ends. O(N log N).
        # Optimal O(N):
        # Find min element in the "unsorted candidate" range and max element.
        # Expand bounds.

        end = -2
        start = -1
        max_so_far = float("-inf")

        for i in range(n):
            max_so_far = max(max_so_far, nums[i])
            if nums[i] < max_so_far:
                end = i

        min_so_far = float("inf")
        for i in range(n - 1, -1, -1):
            min_so_far = min(min_so_far, nums[i])
            if nums[i] > min_so_far:
                start = i

        if end == -2:
            return 0
        return end - start + 1

    def count_paths(self, n: int, roads: list[list[int]]) -> int:
        """
        Number of Ways to Arrive at Destination with min time.
        Dijkstra + DP.
        """
        import heapq

        mod = 10**9 + 7

        adj = [[] for _ in range(n)]
        for u, v, t in roads:
            adj[u].append((v, t))
            adj[v].append((u, t))

        dist = [float("inf")] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        # (time, node)
        pq = [(0, 0)]

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, time in adj[u]:
                new_dist = d + time
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    ways[v] = ways[u]
                    heapq.heappush(pq, (new_dist, v))
                elif new_dist == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % mod

        return ways[n - 1]

    def longest_prefix(self, s: str) -> str:
        """
        Longest Happy Prefix: Prefix that is also Suffix (excluding itself).
        KMP Algorithm - LPS array last element.
        """
        n = len(s)
        lps = [0] * n
        length = 0
        i = 1

        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return s[: lps[n - 1]]

    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Rotate Image: Rotate n x n matrix 90 degrees clockwise in-place.
        """
        n = len(matrix)

        # 1. Transpose (swap matrix[i][j] with matrix[j][i])
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2. Reverse each row
        for i in range(n):
            matrix[i].reverse()

    def nth_person_gets_nth_seat(self, n: int) -> float:
        """
        Airplane Seat Assignment: Probability nth person gets nth seat.
        """
        if n == 1:
            return 1.0
        return 0.5

    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Finds all unique combinations in candidates where the numbers sum to target.
        """
        results = []

        def backtrack(remain, curr_comb, start):
            if remain == 0:
                results.append(list(curr_comb))
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= remain:
                    curr_comb.append(candidates[i])
                    # We can reuse elements, so pass i as start
                    backtrack(remain - candidates[i], curr_comb, i)
                    curr_comb.pop()

        candidates.sort()
        backtrack(target, [], 0)
        return results

    def is_valid_palindrome(self, s: str) -> bool:
        """
        Checks if a string is a palindrome after removing non-alphanumeric chars.
        """
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def delete_node(self, node: ListNode) -> None:
        """
        Deletes a node in a linked list given only access to that node.
        """
        # Copy next node's value and skip it
        node.val = node.next.val
        node.next = node.next.next

    def max_profit(self, prices: list[int]) -> int:
        """
        Best Time to Buy and Sell Stock: Finds max profit from one transaction.
        """
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

    def spiral_order(self, matrix: list[list[int]]) -> list[int]:
        """
        Spiral Matrix: Returns all elements of m x n matrix in spiral order.
        """
        if not matrix:
            return []
        res = []
        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows - 1, 0, cols - 1

        while len(res) < rows * cols:
            # Right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            # Down
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            # Left
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break
            # Up
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res

    def right_side_view(self, root: TreeNode | None) -> list[int]:
        """
        Binary Tree Right Side View: Returns values seen from the right side.
        """
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:  # Last element in current level
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result


class SeatManager:
    def __init__(self, n: int):
        self.seats = list(range(1, n + 1))
        heapq.heapify(self.seats)

    def reserve(self) -> int:
        return heapq.heappop(self.seats)

    def unreserve(self, seat_number: int) -> None:
        heapq.heappush(self.seats, seat_number)
