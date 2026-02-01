# Container With Most Water 🟡 Medium

**Tags**: `Array`, `Two Pointers`, `Greedy`

## Prerequisite Topics

| Topic | Difficulty | Relevance | Notes |
|-------|-----------|-----------|-------|
| Two Pointers | 🟢 Easy | **Critical** | Moving from both ends |
| Greedy Strategy | 🟡 Medium | High | Making local optimal choice |

## The Challenge

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the $i^{th}$ line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the *maximum amount of water* a container can store.

**Constraints**:
- $n == height.length$
- $2 \leq n \leq 10^5$
- $0 \leq height[i] \leq 10^4$

**Example**:
```python
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The max area is between index 1 (height 8) and index 8 (height 7). 
Width = 8 - 1 = 7. Height = min(8, 7) = 7. Area = 7 * 7 = 49.
```

## Algorithmic Analysis

### Naive Approach
Check every pair of lines.
- **Complexity**: $O(N^2)$.
- **Fail**: TLE for $N=10^5$.

### Optimal Approach (Two Pointers)
Start with the widest possible container (indices `0` and `N-1`) and shrink inwards.
- **Key Insight**: The area is determined by the *shorter* wall. 
    - `Area = (right - left) * min(height[left], height[right])`.
- **Strategy**:
    1. Initialize `left=0`, `right=N-1`.
    2. Calc area, update max.
    3. To potentially find a bigger area, we must find a higher wall. 
    4. **Greedy Choice**: Move the pointer pointing to the *shorter* wall. 
        - Why? Moving the taller wall can ONLY reduce area (width decreases, height is still limited by the short wall).
        - Moving the shorter wall gives a chance to find a taller one.
    5. Repeat until pointers meet.

## Complexity Analysis

| Dimension | Complexity | Justification |
|-----------|-----------|---------------|
| Time | $O(N)$ | Single pass from ends to center. |
| Space | $O(1)$ | Constant extra space. |

## Visual Walkthrough

Input: `[1, 8, 6, 2, 5, 4, 8, 3, 7]`

```mermaid
%%{init: {'theme': 'dark'}}%%
graph TD
    classDef primary fill:#0ea5e9,stroke:#38bdf8,stroke-width:2px,color:#0f172a
    classDef success fill:#22c55e,stroke:#4ade80,stroke-width:2px,color:#0f172a
    
    Init["L:0 (1), R:8 (7)"] --> Calc1["Area: 8*1 = 8 <br/> Move L (1 < 7)"]
    Calc1 --> Step2["L:1 (8), R:8 (7)"]
    
    Step2 --> Calc2["Area: 7*7 = 49 (Max) <br/> Move R (7 < 8)"]
    Calc2 --> Step3["L:1 (8), R:7 (3)"]
    class Calc2 success
    
    Step3 --> Calc3["Area: 6*3 = 18 <br/> Move R (3 < 8)"]
    Calc3 --> Step4["..."]
```

## Solution

```python
def max_area(self, height: list[int]) -> int:
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
```
