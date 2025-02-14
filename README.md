# goit-algo2-hw-01

Homework 1. Design And Analysis of Algorithms at GoIT Neoversity

# Divide and Conquer: Algorithm Implementation

## Task 1: Finding Minimum and Maximum Elements

### Problem Description
This task requires finding both the minimum and maximum elements in an array using the **divide and conquer** approach.

### Requirements:
- The function must take an array of numbers of arbitrary length.
- A recursive approach must be used.
- The function should return a tuple `(min, max)`.
- The expected time complexity is **O(n)**.

### Solution Explanation:
1. **Base Cases:**
   - If the array contains only one element, it is both the minimum and maximum.
   - If the array contains two elements, return the smaller one as the minimum and the larger one as the maximum.

2. **Divide Step:**
   - Split the array into two halves and recursively find the min and max for both parts.

3. **Conquer Step:**
   - Combine results by taking the smaller of the two minimums and the larger of the two maximums.

### Complexity Analysis:
- The recursion splits the array in **O(log n)** steps.
- Comparing the min/max takes **O(n)**.
- Overall, the time complexity remains **O(n)**.

---

## Task 2: Finding the k-th Smallest Element

### Problem Description
This task requires implementing an algorithm to find the **k-th smallest element** in an **unsorted array** using the **Quick Select** approach.

### Requirements:
- The function must take an array of numbers and an integer `k`.
- The **pivot selection** strategy must be used.
- The array should **not** be fully sorted.
- The expected average-case time complexity is **O(n)**.

### Solution Explanation:
1. **Pivot Selection:**
   - Choose a **random pivot** to reduce the risk of worst-case complexity.
   
2. **Partitioning:**
   - Divide the array into three groups:
     - Elements smaller than the pivot.
     - Elements equal to the pivot.
     - Elements greater than the pivot.

3. **Recursive Search:**
   - If `k` falls in the left partition, continue searching in that partition.
   - If `k` falls in the middle partition, return the pivot.
   - If `k` falls in the right partition, continue searching in the right partition with an updated index.

### Complexity Analysis:
- **Average case:** **O(n)** (faster than full sorting).
- **Worst case:** **O(n²)** (if pivot selection is poor).
- **Best case:** **O(n)**.

### Why Quick Select?
- It avoids full sorting (`O(n log n)`) while still finding the k-th smallest element efficiently.

---

## Summary

| Task | Approach | Time Complexity |
|------|----------|----------------|
| Find Min/Max | Divide & Conquer | **O(n)** |
| Find k-th Smallest | Quick Select | **O(n) (average case)** |

Both tasks leverage the **divide and conquer** strategy, demonstrating its efficiency in finding key values within an array. 

---