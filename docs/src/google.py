import heapq
from collections import deque

from src.data_structures import ListNode, TreeNode


class GoogleSolutions:
    """
    Solutions for Google DSA problems.

    Each method corresponds to a specific interview problem, implemented with
    educational comments and optimal complexity.
    """

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """
        Finds indices of two numbers in `nums` that add up to `target`.

        Args:
            nums: List of integers (input array).
            target: The integer value to reach by summing two elements.

        Returns:
            A list containing the two indices [i, j] such that nums[i] + nums[j] == target.
            Returns empty list if no solution found (though problem guarantees one).
        """
        # Dictionary to store mapping: value -> index
        # This allows O(1) lookups to check if the complement exists.
        seen: dict[int, int] = {}

        # O(N) Loop: Iterate through the array once
        for i, num in enumerate(nums):
            # Calculate the number needed to reach the target
            complement = target - num

            # Check if the complement is already in our hash map
            if complement in seen:
                # Found the pair! Return current index and the complement's stored index
                return [seen[complement], i]

            # Store the current number and its index for future checks
            seen[num] = i

        # If no solution is found (logic shouldn't reach here per constraints)
        return []

    def level_order(self, root: "TreeNode | None") -> list[list[int]]:
        """
        Returns the level order traversal of a binary tree's nodes.

        Args:
            root: The root node of the binary tree.

        Returns:
            A list of lists, where each inner list contains the values of nodes
            at that level, from left to right.
        """
        # Handle edge case: empty tree
        if not root:
            return []

        results: list[list[int]] = []
        # Queue for BFS: stores nodes to visit (FIFO)
        # Initialize with root
        queue: deque[TreeNode] = deque([root])

        while queue:
            level_values: list[int] = []
            # Calculate number of nodes at the current level
            # This is critical: we must process exactly this many nodes
            # to keep levels separate in the output.
            level_size = len(queue)

            for _ in range(level_size):
                # Pop from left (FIFO)
                node = queue.popleft()
                level_values.append(node.val)

                # Add children to queue for next level processing
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add the current level's values to the result
            results.append(level_values)

        return results

    def length_of_longest_substring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Args:
            s: The input string.

        Returns:
            The length of the longest substring containing unique characters.
        """
        # Dictionary to store the last seen index of each character
        char_index_map: dict[str, int] = {}
        max_length = 0
        left = 0  # Left boundary of the sliding window

        for right, char in enumerate(s):
            # If the character is already in the window, move the left pointer
            # We move it to the right of the last occurrence to exclude the duplicate
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1

            # Update the last seen index of the character
            char_index_map[char] = right

            # Update the maximum length found so far
            # Window size is (right - left + 1)
            max_length = max(max_length, right - left + 1)

        return max_length

    def find_kth_largest(self, nums: list[int], k: int) -> int:
        """
        Finds the kth largest element in an array.

        Args:
            nums: List of integers.
            k: The rank of the largest element to find.

        Returns:
            The kth largest element.
        """
        # Min-Heap Approach
        # We maintain a min-heap of size k.
        # The heap will store the k largest elements seen so far.
        # The root of the heap (smallest element in the heap) will be the kth largest.

        heap: list[int] = []

        for num in nums:
            # Push current number to heap
            heapq.heappush(heap, num)

            # If heap size exceeds k, remove the smallest element
            # This ensures only the k largest elements remain
            if len(heap) > k:
                heapq.heappop(heap)

        # The top of the min-heap is the smallest of the k largest elements,
        # which is exactly the kth largest element.
        return heap[0]

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Merges all overlapping intervals.

        Args:
            intervals: A list of intervals where each interval is [start, end].

        Returns:
            A list of non-overlapping intervals that cover all the input intervals.
        """
        # Edge case: empty list
        if not intervals:
            return []

        # Sort intervals by their start time.
        # This is critical: it allows us to merge in a single linear pass.
        # Time Complexity of sort: O(N log N)
        intervals.sort(key=lambda x: x[0])

        merged: list[list[int]] = []

        for interval in intervals:
            # If the list of merged intervals is empty
            # or if the current interval does not overlap with the previous one,
            # simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Otherwise, there is an overlap, so we merge the current and previous
                # intervals. We do this by updating the end of the previous interval
                # if the current interval ends later.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

    def search(self, nums: list[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array.

        Args:
            nums: The rotated sorted array.
            target: The value to search for.

        Returns:
            The index of the target if found, otherwise -1.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Determine which side is sorted
            # If left side is sorted...
            if nums[left] <= nums[mid]:
                # Check if target is in the left sorted portion
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    # Target must be in the right side
                    left = mid + 1
            # Otherwise, the right side is sorted
            else:
                # Check if target is in the right sorted portion
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    # Target must be in the left side
                    right = mid - 1

        return -1

    def is_valid_parentheses(self, s: str) -> bool:
        """
        Determines if the input string has valid parentheses.

        Args:
            s: String containing '(', ')', '{', '}', '[', ']'.

        Returns:
            True if the parentheses are valid, False otherwise.
        """
        stack: list[str] = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                # Closing bracket: check if matches top of stack
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                # Opening bracket: push to stack
                stack.append(char)

        # If stack is empty, all brackets were matched
        return not stack

    def ladder_length(self, begin_word: str, end_word: str, word_list: list[str]) -> int:
        """
        Finds the length of the shortest transformation sequence from begin_word to end_word.

        Args:
            begin_word: The starting word.
            end_word: The target word.
            word_list: List of available words for transformation.

        Returns:
            The number of words in the shortest sequence (including begin_word).
            Returns 0 if no such sequence exists.
        """
        word_set = set(word_list)
        if end_word not in word_set:
            return 0

        # BFS Queue: stores (current_word, level)
        queue: deque[tuple[str, int]] = deque([(begin_word, 1)])

        # Visited set to prevent cycles
        visited = {begin_word}

        while queue:
            current_word, level = queue.popleft()

            if current_word == end_word:
                return level

            # Try changing each character of the word
            for i in range(len(current_word)):
                original_char = current_word[i]

                # Check all 26 lowercase letters
                for c in range(ord("a"), ord("z") + 1):
                    char = chr(c)
                    if char == original_char:
                        continue

                    # Create new word combination
                    new_word = current_word[:i] + char + current_word[i + 1 :]

                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, level + 1))

        return 0

    def max_area(self, height: list[int]) -> int:
        """
        Finds the maximum area of water a container can store.

        Args:
            height: List of non-negative integers representing wall heights.

        Returns:
            The maximum area.
        """
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            max_water = max(max_water, width * current_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

    def subsets_with_dup(self, nums: list[int]) -> list[list[int]]:
        """
        Returns all possible subsets (the power set) of a collection of integers with duplicates.

        Args:
            nums: List of integers (potentially containing duplicates).

        Returns:
            A list of all unique subsets.
        """
        results: list[list[int]] = []
        nums.sort()

        def backtrack(start_index: int, current_subset: list[int]) -> None:
            results.append(list(current_subset))

            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i - 1]:
                    continue

                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()

        backtrack(0, [])
        return results

    def min_window(self, s: str, t: str) -> str:
        """
        Finds the minimum window substring of s that contains all characters in t.

        Args:
            s: The source string.
            t: The target string containing characters to be matched.

        Returns:
            The empty string "" if no such window exists, or the minimum window.
        """
        if not t or not s:
            return ""

        # Dictionary to keep a count of all the unique characters in t.
        dict_t: dict[str, int] = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        required = len(dict_t)

        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
        # (Optimization not strictly necessary but helpful for sparse s).
        # We'll stick to standard sliding window for clarity.

        left, r = 0, 0

        # formed is used to keep track of how many unique characters in t
        # are present in the current window in its desired frequency.
        formed = 0
        window_counts: dict[str, int] = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the
            # desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while left <= r and formed == required:
                character = s[left]

                # Save the smallest window until now.
                if r - left + 1 < ans[0]:
                    ans = (r - left + 1, left, r)

                # The character at the position pointed by the
                # `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                left += 1

            # Keep expanding the window once we are done contracting.
            r += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

    def reverse_k_group(self, head: ListNode | None, k: int) -> ListNode | None:
        """
        Reverses nodes of a linked list k at a time.

        Args:
            head: The head of the linked list.
            k: The size of the group to reverse.

        Returns:
            The head of the modified linked list.
        """
        if not head or k == 1:
            return head

        # Check if there are at least k nodes left
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1

        if count < k:
            return head

        # Reverse k nodes
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Recursive call for the rest of the list
        # head is now the tail of the reversed group, so head.next should point
        # to the result of recursion on the rest
        if head:
            head.next = self.reverse_k_group(curr, k)

        return prev

    def find_min(self, nums: list[int]) -> int:
        """
        Finds the minimum element in a rotated sorted array.

        Args:
            nums: The rotated sorted array.

        Returns:
            The minimum value.
        """
        left, right = 0, len(nums) - 1

        # If the array is not rotated (or we found the sorted segment)
        if nums[left] <= nums[right]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2

            # If mid element is greater than right element,
            # the minimum must be to the right of mid
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise, the minimum is at mid or to the left
                right = mid

        return nums[left]


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
