# Find Median from Data Stream 🔴 Hard

**Tags**: `Heap`, `Design`, `Data Stream`

## Prerequisite Topics

| Topic | Difficulty | Relevance | Notes |
|-------|-----------|-----------|-------|
| Priority Queue (Heap) | 🟡 Medium | **Critical** | Maintaining sorted halves efficienty |
| Object-Oriented Design | 🟢 Easy | High | Class structure |

## The Challenge

Implement `MedianFinder` class to add numbers and find median efficiently.

### Strategic Analysis & Real-World Context

> [!NOTE]
> **Why this matters**: Analytics dashboards (P50 latency), Senor Data processing.

| Scenario | Preferred Approach | Why? |
|----------|--------------------|------|
| **Streaming** | **Two Heaps** | $O(\log N)$ Insert, $O(1)$ Read. Perfect for real-time. |
| **Fixed Range** | **Count Sort / Bucket** | If integers in range [0, 100], just count them. Partition-based selection is also option but slower for continuous queries. |

## Complexity Analysis

| Dimension | Complexity | Justification |
|-----------|-----------|---------------|
| Time | $O(\log N)$ | Heap push/pop. |
| Space | $O(N)$ | Storing all elements. |

## Solution

```python
class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap (inverted)
        self.large = []  # Min-heap

    def add_num(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
```
