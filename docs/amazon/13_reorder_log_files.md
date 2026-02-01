# Reorder Data in Log Files 🟡 Medium

**Tags**: `String`, `Sorting`

## Prerequisite Topics

| Topic | Difficulty | Relevance | Notes |
|-------|-----------|-----------|-------|
| Sorting with Keys | 🟢 Easy | **Critical** | Custom comparator logic |
| String Manipulation | 🟢 Easy | High | Parsing identifiers |

## The Challenge

You are given an array of `logs`. Each log is a space-delimited string of words, where the first word is the **identifier**.

There are two types of logs:
1. **Letter-logs**: All words (except the identifier) consist of lowercase English letters.
2. **Digit-logs**: All words (except the identifier) consist of digits.

Reorder these logs so that:
1. The **letter-logs** come before all **digit-logs**.
2. The **letter-logs** are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
3. The **digit-logs** maintain their relative ordering.

**Constraints**:
- $1 \leq logs.length \leq 100$
- $3 \leq logs[i].length \leq 100$

**Example**:
```python
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
```

## Algorithmic Analysis

### Optimal Approach (Custom Sort Key)
Python's `sort` is stable, which helps with digit logs if we processed them together, but splitting them is easier.
- **Strategy**:
    1. Separate `letter` and `digit` logs.
    2. Sort `letter` logs.
        - Key: `(content, identifier)`.
    3. Concatenate `sorted_letter + digit`.

### Strategic Analysis & Real-World Context

> [!NOTE]
> **Why this matters**: Log aggregation systems (Splunk/ELK), sorting prioritized tasks.

| Scenario | Preferred Approach | Why? |
|----------|--------------------|------|
| **Standard** | **Split & Sort** | $O(N \log N)$. Easiest to read and maintain. |
| **In-place** | **Partition** | Like QuickSort partition (move letters to front), then sort front. Harder to implement stability for digits. |

## Complexity Analysis

| Dimension | Complexity | Justification |
|-----------|-----------|---------------|
| Time | $O(N \cdot M \cdot \log N)$ | Sort N logs of max length M. Comparison takes O(M). |
| Space | $O(N \cdot M)$ | Storage for split lists. |

## Solution

```python
def reorder_log_files(self, logs: list[str]) -> list[str]:
    letter_logs = []
    digit_logs = []
    
    for log in logs:
        # split(maxsplit=1) -> [id, content]
        id_, content = log.split(" ", 1)
        if content[0].isalpha():
            letter_logs.append((content, id_, log))
        else:
            digit_logs.append(log)
    
    # Sort letter logs by content, then id
    letter_logs.sort(key=lambda x: (x[0], x[1]))
    
    return [x[2] for x in letter_logs] + digit_logs
```
