# Largest Palindromic Substring 🟡 Medium

**Tags**: `String`, `Dynamic Programming`

## Prerequisite Topics

| Topic | Difficulty | Relevance | Notes |
|-------|-----------|-----------|-------|
| Palindrome Logic | 🟢 Easy | **Critical** | Symmetry detection |

## The Challenge

Given a string `s`, return the longest palindromic substring in `s`.

**Constraints**:
- $1 \leq s.length \leq 1000$

**Example**:
```python
Input: s = "babad"
Output: "bab" (or "aba")
```

## Algorithmic Analysis

### Optimal Approach (Expand Around Center)
For each character (and each gap between characters), treat it as a potential center of a palindrome and expand outwards.
- **Logic**: A palindrome of length $N$ has a palindrome of length $N-2$ inside it.

## Complexity Analysis

| Dimension | Complexity | Justification |
|-----------|-----------|---------------|
| Time | $O(N^2)$ | $N$ centers, each expanding up to $N/2$. |
| Space | $O(1)$ | No extra space beyond result. |

## Visual Walkthrough

```mermaid
%%{init: {'theme': 'dark'}}%%
graph LR
    classDef primary fill:#0ea5e9,stroke:#38bdf8,stroke-width:2px,color:#0f172a
    
    Center["Center 'b' at idx 2"] --> E1["Check 'a'=='a'? Yes."]
    E1 --> E2["Check 'b'=='d'? No."]
    E2 --> Res["Palindrome: 'aba'"]
    class Res primary
```

## Solution

```python
def longest_palindrome(self, s: str) -> str:
    if not s: return ""
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1; right += 1
        return s[left+1 : right]
    res = ""
    for i in range(len(s)):
        p1 = expand(i, i)
        if len(p1) > len(res): res = p1
        p2 = expand(i, i + 1)
        if len(p2) > len(res): res = p2
    return res
```
