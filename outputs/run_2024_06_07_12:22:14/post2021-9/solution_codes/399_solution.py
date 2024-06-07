# Problem:

You are given an array consisting of all integers from $[l, r]$ inclusive. For example, if $l = 2$ and $r = 5$, the array would be $[2, 3, 4, 5]$. What's the minimum number of elements you can delete to make the bitwise AND of the array non-zero?

A bitwise AND is a binary operation that takes two equal-length binary representations and performs the AND operation on each pair of the corresponding bits.

-----Input-----

The first line contains one integer $t$ ($1 \leq t \leq 10^4$) — the number of test cases. Then $t$ cases follow.

For each test case:
- The first line contains two integers $l$ and $r$ ($1 \leq l \leq r \leq 2 \cdot 10^5$) — the description of the array.

-----Output-----

For each test case, output a single integer — the answer to the problem.

-----Examples-----

Input
5
1 2
2 8
4 5
1 5
100000 200000

Output
1
3
0
2
31072

-----Note-----

In the first test case, the array is $[1, 2]$. Currently, the bitwise AND is $0$, as $1\ \& \ 2 = 0$. However, after deleting $1$ (or $2$), the array becomes $[2]$ (or $[1]$), and the bitwise AND becomes $2$ (or $1$). This can be proven to be the optimal, so the answer is $1$.

In the second test case, the array is $[2, 3, 4, 5, 6, 7, 8]$. Currently, the bitwise AND is $0$. However, after deleting $4$, $5$, and $8$, the array becomes $[2, 3, 6, 7]$, and the bitwise AND becomes $2$. This can be proven to be the optimal, so the answer is $3$. Note that there may be other ways to delete $3$ elements.

# Knowledge-Aware Prompt:

1. Read t, the number of test cases.

2. Loop t times to read each test case.

3. Read l and r, the range of integers forming the array.

4. Calculate the bitwise AND of the array.

5. Initialize a counter for the number of elements deleted to make the bitwise AND non-zero.

6. Apply bitwise operations to identify the bits that need to be deleted to make the AND non-zero.

7. Print the minimum number of elements that need to be deleted.

8. End all loops.

# Let's now proceed and write the solution code: