# Linked List Cycle 🟢 Easy

**Tags**: `Linked List`, `Two Pointers`

## Prerequisite Topics

| Topic | Difficulty | Relevance | Notes |
|-------|-----------|-----------|-------|
| Two Pointers | 🟢 Easy | **Critical** | Floyd's Cycle-Finding Algorithm |

## The Challenge

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

**Constraints**:
- The number of nodes in the list is in the range $[0, 10^4]$.
- $-10^5 \leq Node.val \leq 10^5$

**Example**:
```python
Input: head = [3,2,0,-4], pos = 1 (cycle)
Output: True
```

## Algorithmic Analysis

### Optimal Approach (Floyd's Tortoise and Hare)
Use two pointers, `slow` and `fast`.
- `slow` moves 1 step.
- `fast` moves 2 steps.
- If they meet, there is a cycle. If `fast` reaches `None`, there isn't.

## Complexity Analysis

| Dimension | Complexity | Justification |
|-----------|-----------|---------------|
| Time | $O(N)$ | Fast pointer traverses at most 2N nodes. |
| Space | $O(1)$ | Constant extra space. |

## Visual Walkthrough

```mermaid
%%{init: {'theme': 'dark'}}%%
graph LR
    classDef primary fill:#0ea5e9,stroke:#38bdf8,stroke-width:2px,color:#0f172a
    
    A((3)) --> B((2))
    B --> C((0))
    C --> D((-4))
    D --> B
    
    S["Slow"] -.-> B
    F["Fast"] -.-> C
```

## Solution

```python
def has_cycle(self, head: ListNode | None) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```
