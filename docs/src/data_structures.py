class TreeNode:
    """Definition for a binary tree node."""

    def __init__(
        self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None
    ):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    """Definition for a singly-linked list node."""

    def __init__(self, val: int = 0, next_node: "ListNode | None" = None):
        self.val = val
        self.next = next_node
