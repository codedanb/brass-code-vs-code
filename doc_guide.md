# FAANG DSA Problems - Prompt Requirements & Project Standards

## 📋 Document Purpose & Intent

This file is the **Master System Prompt** governing all updates to the FAANG DSA Course. It establishes:
- **Unified Coding Standards**: Enforce modern Python 3.12+ idioms across all solutions
- **Educational Clarity**: Prioritize learning outcomes through explanatory comments and trade-off analysis
- **Quality Assurance**: Ensure comprehensive testing, edge case handling, and robust code
- **Consistent Documentation**: Maintain high-quality README files with visual aids and prerequisite analysis

### Critical Rules

**NOTE 1**: Do not remove existing code or documentation unless explicitly asked.

**NOTE 2**: For every problem elaboration, include:
- A detailed **Prerequisite Topics Table** with difficulty levels and relevance scores
- Updated **README.md** files reflecting these topics
- Complexity analysis with visual diagrams

### Tooling Requirements

- **Code Formatting & Env Management**: `uv` for Python environments and dependencies
- **Linting & Code Quality**: `ruff` for linting, formatting, and error checking
- **Test Framework**: `pytest` with parametrized test cases
- **Initialization**: `uv init` in the project root (`FAANG_DSA_Course/`)
- **Project Path**: `/Users/a/Documents/GitHub/Multi-Agent-Testing/FAANG_DSA_Course/`


---

## 1. 🐍 Coding Standards (Modern Python 3.12+)

### Typing & Syntax
*   **Generics**: Use strict PEP 585 built-in generics.
    *   ✅ `list[int]`, `dict[str, int]`, `tuple[int, int]`
    *   ❌ `List[int]`, `Dict`, `Tuple` (from `typing`)
*   **Unions**: Use strict PEP 604 union operators.
    *   ✅ `TreeNode | None`, `int | float`
    *   ❌ `Optional[TreeNode]`, `Union[int, float]`
*   **Docstrings**: Use **Strict Google Style**.
    *   Must include `Summary`, `Args:`, and `Returns:`.
    *   Align indented descriptions clearly.

### Commenting Strategy
*   **Educational Comments**: Add single-line comments **above** nearly every logic step to teach the reader.
*   **Focus on 'Why' Not 'What'**:
    *   *Bad*: `# Increase i by 1` (Describes what code does, which is obvious)
    *   *Good*: `# Move left pointer inward to attempt finding a taller wall` (Explains algorithm intent)
    *   *Better*: `# Move left pointer inward; right wall is taller so left is limiting factor` (Explains decision logic)
*   **Complexity Annotations**: Tag lines with computational significance.
    *   Example: `# Sorting takes O(N log N); enables efficient lookup in subsequent loop`
*   **Pattern Explanations**: When using advanced patterns, explain the technique.
    ```python
    # Two-pointer approach: start from boundaries, work inward to explore all combinations in O(N) total time
    ```

### Code Organization & Structure
*   **Class-Based Organization**: All solutions must be methods within a class (e.g., `GoogleSolutions`, `MicrosoftSolutions`).
*   **Method Naming**: Use descriptive names that reflect the problem.
    *   ✅ `max_profit_stock_trading()`, `longest_substring_without_repeating()`
    *   ❌ `solve()`, `helper()`
*   **Section Separators**: Use visual separators between topics for clarity.
    ```python
    # =========================================================================
    # 🟢 TOPIC: ARRAYS & HASHING
    # =========================================================================
    # Problems in this section focus on efficient lookups, frequency tracking,
    # and array manipulation using hash-based data structures.
    ```
*   **Consistent Formatting**: Always run `ruff format .` and `ruff check --fix .` before committing

---

## 2. 📚 Documentation Standards (README.md)

### Content Requirements (Per Problem)

1.  **Header**: Problem Name with difficulty badge (🟢 Easy, 🟡 Medium, 🔴 Hard).
    - Tags: Comma-separated concepts (e.g., `Array`, `Hash Map`, `Two Pointers`)

2.  **Prerequisite Topics Table**: Required for problem understanding
    ```markdown
    | Topic | Difficulty | Relevance | Notes |
    |-------|-----------|-----------|-------|
    | Array Indexing | 🟢 Easy | High | Foundation for iteration |
    | Hash Maps | 🟡 Medium | Critical | O(1) lookups are key |
    ```

3.  **The Challenge**: 
    - Clear, concise problem statement
    - Explicit constraints (input size, value ranges, edge cases)
    - Example inputs/outputs with explanation

4.  **Algorithmic Analysis (The "Why")**:
    *   **Naive/Brute Force**: 
        - Explain intuitive approach
        - **Quantify failure**: "TLE on $N > 10^4$ because $O(N^2)$ = $10^8$ operations"
        - Show actual time complexity impact
    *   **Optimal Approach**: 
        - Step-by-step algorithm breakdown
        - Key insight that enables optimization
        - Why this approach works (correctness argument)
    *   **Trade-offs & Alternatives**: 
        - "Hash Map: $O(N)$ space, $O(1)$ access. Sorting: $O(1)$ space, $O(\log N)$ access."
        - "Choose Hash Map if memory plentiful; choose Sort if memory constrained."

5.  **Complexity Analysis Table**:
    ```markdown
    | Dimension | Complexity | Justification |
    |-----------|-----------|---------------|
    | Time | O(N log N) | Single pass with hash operations |
    | Space | O(N) | Hash map stores all elements |
    ```

6.  **Visual Walkthrough**: 
    - Mermaid diagram (or ASCII if simple) showing algorithm flow
    - Use dark theme palette (see Section 3)
    - Show state transitions with example data

7.  **Code Implementation**: 
    - Full solution with comprehensive comments
    - Input validation demonstrated
    - Edge cases handled

### Logical Separation
*   **Topic Grouping**: Organize problems by algorithmic concept.
    - Example structure: "01. Arrays & Hashing", "02. Two Pointers", "03. Sliding Window"
*   **Sub-topics**: Use Level 2 (##) for major topics, Level 3 (###) for problem subtypes
*   **Consistency**: Maintain same structure for every problem for predictable navigation

---

## 3. 🎨 Visual Style Guide (Dark Theme)

All Mermaid diagrams **MUST** use the following initialization and class definitions to ensure consistency with dark theme GitHub/VS Code viewers.

### Template (Copy-Paste)

```mermaid
%%{init: {'theme': 'dark'}}%%
graph TD
    classDef primary fill:#0ea5e9,stroke:#38bdf8,stroke-width:2px,color:#0f172a
    classDef success fill:#22c55e,stroke:#4ade80,stroke-width:2px,color:#0f172a
    classDef warning fill:#f59e0b,stroke:#fbbf24,stroke-width:2px,color:#0f172a
    classDef error fill:#ef4444,stroke:#f87171,stroke-width:2px,color:#ffffff
    classDef info fill:#6366f1,stroke:#818cf8,stroke-width:2px,color:#ffffff
    classDef secondary fill:#8b5cf6,stroke:#a78bfa,stroke-width:2px,color:#ffffff

    %% Note: Always wrap text in quotes if it contains [], (), or {}
    %% Example: NodeA["List: [1, 2, 3]"]
```

### Color Semantic Usage

| Color | Use Case | Example |
|-------|----------|----------|
| **Primary** (Blue) | Start, entry point, main flow | Loop start, function entry |
| **Secondary** (Purple) | Processing step, algorithm action | Pointer movement, comparison |
| **Success** (Green) | Found answer, valid state, goal reached | Solution found, condition met |
| **Warning** (Amber) | Boundary, edge case, transition | Array bounds, pivot selection |
| **Error** (Red) | Failure, invalid state, rejection | Input rejected, no solution |
| **Info** (Indigo) | Additional info, metadata, notes | Counter value, intermediate state |

---

## 4. 🧠 Strategic Analysis & Trade-offs (Code & Logic)

When writing explanations or analyzing trade-offs:

### ⚖️ Core Trade-offs
Always consider what we are gaining vs losing.
*   **Time vs Space**: "We spend $O(N)$ space for a Hash Map to get $O(1)$ access."
*   **Readability vs Performance**: "The iterative solution is $O(1)$ space but harder to read than the recursive one."
*   **Preprocessing vs Querying**: "Sorting takes time upfront but makes searching fast."

### 🔍 Scenario Analysis (Real-World Context)
Don't just state "It's $O(N \log N)$". Explain **when** it is good or bad.
*   **Scaling**: "Merge Sort is preferred for Linked Lists (no random access)."
*   **Constraints**: "Counting Sort is $O(N)$ only if range $K$ is small. If $K=10^9$, memory crashes."
*   **Input Nature**: "QuickSort degrades to $O(N^2)$ on sorted inputs without random pivots."

### 🛠 Data Structure Selection "Why?"
*   Why a **Set**? -> "We only care about existence, not frequency or order."
*   Why a **Heap**? -> "We need repeated access to the min/max element, not random access."
*   Why **Two Pointers**? -> "We can process from both ends to reduce $O(N^2)$ to $O(N)$."
    
### 🔧 Brute Force Analysis Framework
For every problem, explicitly address the naive approach:

*   **Why is it bad?** Quantify: "$O(N^2)$ on $N = 10^5$ = $10^{10}$ operations → TLE (1-2 sec timeout)"
*   **When is it okay?** Give thresholds: "$O(N^2)$ acceptable if $N \leq 5 \times 10^3$ (25M ops safe)"
*   **What fails first?** "Time limit on LeetCode ~2 sec; Memory limit ~256 MB. At $N=10^4$, $O(N^2)$ exceeds time."
*   **Path to optimization**: "Brute force reveals the hard part—repeated lookups. Hash map cuts lookup from $O(N)$ to $O(1)$."

---

## 5. 🧪 Testing & QA Standards

### Framework & Methodology
*   **Tool**: `pytest` (ONLY testing framework)
*   **Style**: Use `@pytest.mark.parametrize` for clean, data-driven test cases
*   **Organization**: Separate test file per solution (e.g., `test_two_sum.py`)
*   **Naming**: Test functions as `test_<problem_name>_<case_description>`

### Mandatory Test Coverage

Every solution **MUST** include these test categories:

| Category | Example | Purpose |
|----------|---------|---------|
| **Happy Path** | Standard example from problem | Verify core logic |
| **Empty/Null** | `[]`, `""`, `None` | Boundary condition |
| **Single Element** | `[1]`, `["a"]` | Minimal input |
| **Duplicates** | `[1, 1, 1]`, `"aaa"` | Frequency handling |
| **Extremes** | Min/max constraints, negatives | Scale robustness |
| **Already Solved** | Pre-sorted, already valid | Idempotency check |

### Code Robustness Checklist

*   **Input Validation**: Explicitly handle edge cases at function start
    ```python
    def solve(head):
        # Handle empty/single-node cases immediately
        if not head or not head.next:
            return head
        # Proceed with main logic
    ```
*   **Assertions**: Use type hints and docstrings; leverage `mypy` for static analysis
*   **Test Output**: Verify both correctness and efficiency (if applicable)

---

## 6. 🛡 Edge Case Checklist (Topic Specific)

Consult this list when implementing solutions to ensure robustness.

*   **Arrays/Strings**:
    *   Empty array/string.
    *   Array with 1 element.
    *   Duplicate values.
    *   All values same.
    *   Already sorted (ascending/descending).
*   **Linked Lists**:
    *   Head is `None`.
    *   Single node.
    *   Even vs Odd length (for middle finding).
    *   Cycles (if applicable).
*   **Trees**:
    *   Root is `None`.
    *   Unbalanced (skewed dict-like tree).
    *   Leaf nodes vs Internal nodes.
*   **Graphs**:
    *   Disconnected components.
    *   Self-loops.
    *   Cycles.
*   **Math/Numbers**:
    *   Negative numbers.
    *   Zero.
    *   Integer Overflow equivalents (though Python handles large ints, logic might fail).

---

## 8. 🔍 Code Review Checklist

Before finalizing any problem solution, verify:

### Correctness
- [ ] All test cases pass (basic, edge, extreme)
- [ ] Algorithm handles all constraints
- [ ] No off-by-one errors in loops/indexing
- [ ] Proper handling of empty/null inputs

### Code Quality
- [ ] Modern Python 3.12+ syntax (no `List`, `Dict`, `Optional`)
- [ ] Type hints on all functions and complex variables
- [ ] Google-style docstrings with Args/Returns
- [ ] Educational comments ("why", not "what")
- [ ] Passes `ruff check` and `ruff format`

### Documentation
- [ ] README updated with problem explanation
- [ ] Prerequisite topics table included
- [ ] Complexity analysis documented
- [ ] Mermaid diagram for visual walkthrough
- [ ] Trade-offs and alternatives discussed

### Performance
- [ ] Complexity analysis matches code behavior
- [ ] No unnecessary nested loops or redundant operations
- [ ] Appropriate data structures chosen
- [ ] Memory usage justified

---

## 9. 📋 Problem Template

Use this structure for consistency when adding new problems:

```markdown
## Problem XY: [Problem Name]

**Difficulty**: 🟡 Medium | **Tags**: `Array`, `Hash Map`, `Two Pointers`

### Prerequisite Topics

| Topic | Difficulty | Relevance | Notes |
|-------|-----------|-----------|-------|
| Hash Map Operations | 🟢 Easy | Critical | O(1) lookups essential |
| Array Iteration | 🟢 Easy | High | Foundation |

### The Challenge

[Clear problem statement]

**Constraints**:
- $1 \leq N \leq 10^5$
- $-10^9 \leq nums[i] \leq 10^9$

**Example**:
\`\`\`
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
\`\`\`

### Algorithmic Analysis

#### Brute Force Approach
[Explanation and why it fails]

#### Optimal Approach
[Detailed algorithm explanation]

### Complexity Analysis

| Dimension | Complexity | Justification |
|-----------|-----------|---------------|
| Time | O(N) | Single pass with hash lookups |
| Space | O(N) | Hash map stores elements |

### Solution

[Full code with comments]

### Tests

[Pytest parametrized test cases]
\`\`\`

---

## 7. 🛠 Tooling & Environment Setup

### Package Manager
*   **Primary**: `uv` (handles environments, dependencies, and virtual environments)
*   **Initialization**:
    ```bash
    cd /Users/a/Documents/GitHub/Multi-Agent-Testing/FAANG_DSA_Course/
    uv init
    uv sync  # Install dependencies from pyproject.toml
    ```

### Code Quality Tools

| Tool | Purpose | Command |
|------|---------|---------|
| `ruff` | Format & lint | `ruff check --fix .` |
| `ruff` | Format code | `ruff format .` |
| `pytest` | Run tests | `pytest tests/ -v` |
| `mypy` | Type checking | `mypy src/ --strict` |

### pyproject.toml Setup

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "faang-dsa-course"
version = "1.0.0"
description = "FAANG interview DSA solutions with educational focus"
requires-python = ">=3.12"
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "ruff>=0.1",
    "mypy>=1.0",
]

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
```

### Project Path & Structure

**Root Directory**: `/Users/a/Documents/GitHub/Multi-Agent-Testing/FAANG_DSA_Course/`

**Standard Folder Layout**:
```
FAANG_DSA_Problems/
├── pyproject.toml         # Dependencies and project config
├── README.md              # Main course overview
├── src/
│   └── solutions.py       # All solution implementations
├── tests/
│   ├── test_arrays.py
│   ├── test_trees.py
│   └── ...
└── docs/
    └── problem_details/   # Individual problem READMEs
```
