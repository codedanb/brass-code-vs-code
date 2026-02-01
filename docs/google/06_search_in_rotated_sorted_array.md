# Search in Rotated Sorted Array 🟡 Medium

**Tags**: `Array`, `Binary Search`

## Prerequisite Topics

| Topic | Difficulty | Relevance | Notes |
|-------|-----------|-----------|-------|
| Binary Search | 🟢 Easy | **Critical** | Core logic is modified binary search |
| Array Indexing | 🟢 Easy | High | Handling rotated indices |

## The Challenge

There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is **rotated** at an unknown pivot index `k` ($1 \leq k < nums.length$) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`.

Given the array `nums` and an integer `target`, return the *index* of `target` if it is in `nums`, or `-1` if it is not.

You must write an algorithm with $O(\log n)$ runtime complexity.

**Constraints**:
- $1 \leq nums.length \leq 5000$
- $-10^4 \leq nums[i] \leq 10^4$
- All values of `nums` are **unique**.
- `nums` is an ascending array that is possibly rotated.

**Example**:
```python
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

## Algorithmic Analysis

### Naive Approach
Linear search through the list.
- **Complexity**: $O(N)$.
- **Issues**: Fails the $O(\log N)$ requirement.

### Optimal Approach (Modified Binary Search)
Even though the array is rotated, one half of the array (relative to the midpoint) will always be **sorted**.
- **Logic**:
    1. Calculate `mid`.
    2. Check if `nums[left] <= nums[mid]`.
        - If **True**: Left side `[left, mid]` is sorted.
            - Check if `target` is in range `[nums[left], nums[mid])`.
            - If yes, search left (`right = mid - 1`).
            - Else, search right (`left = mid + 1`).
        - If **False**: Right side `[mid, right]` is sorted.
            - Check if `target` is in range `(nums[mid], nums[right]]`.
            - If yes, search right (`left = mid + 1`).
            - Else, search left (`right = mid - 1`).
- **Key Insight**: We use the sorted half to determine if the target *could* be there. If not, we eliminate that half.

## Complexity Analysis

| Dimension | Complexity | Justification |
|-----------|-----------|---------------|
| Time | $O(\log N)$ | Standard binary search halving the search space. |
| Space | $O(1)$ | No extra storage needed. |

## Visual Walkthrough

Input: `[4, 5, 6, 7, 0, 1, 2]`, `Target = 0`

```mermaid
%%{init: {'theme': 'dark'}}%%
graph TD
    classDef primary fill:#0ea5e9,stroke:#38bdf8,stroke-width:2px,color:#0f172a
    classDef success fill:#22c55e,stroke:#4ade80,stroke-width:2px,color:#0f172a
    classDef warning fill:#f59e0b,stroke:#fbbf24,stroke-width:2px,color:#0f172a
    
    Init["Left: 0, Right: 6, Mid: 3 (Val 7)"] --> Check{"Target 0 == 7?"}
    Check -- No --> Sorted{"Is Left (4) <= Mid (7)?"}
    
    Sorted -- Yes --> Range{"Target 0 inside [4, 7]?"}
    class Sorted primary
    
    Range -- No --> Update1["Target must be in right half <br/> Left = Mid + 1 = 4"]
    class Range warning
    
    Update1 --> Step2["Left: 4, Right: 6, Mid: 5 (Val 1)"]
    Step2 --> Check2{"Target 0 == 1?"}
    Check2 -- No --> Sorted2{"Is Left (0) <= Mid (1)?"}
    
    Sorted2 -- Yes --> Range2{"Target 0 inside [0, 1]?"}
    Range2 -- Yes --> Update2["Right = Mid - 1 = 4"]
    
    Update2 --> Step3["Left: 4, Right: 4, Mid: 4 (Val 0)"]
    Step3 --> Found["Target Found at 4"]
    class Found success
```

## Solution

```python
def search(self, nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # If left side is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # If right side is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1
```
