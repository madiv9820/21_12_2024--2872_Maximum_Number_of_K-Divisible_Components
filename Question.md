# [2872. Maximum Number of K-Divisible Components](https://leetcode.com/problems/maximum-number-of-k-divisible-components)

**Type:** Hard <br>
**Topics:** Tree, Depth-First Search <br>
**Companies:** Google
<br>

There is an undirected tree with `n` nodes labeled from `0` to `n - 1`. You are given the integer `n` and a 2D integer array `edges` of length `n - 1`, where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is an edge between nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> in the tree.

You are also given a **0-indexed** integer array `values` of length `n`, where `values[i]` is the value associated with the <code>i<sup>th</sup></code> node, and an integer `k`.

A **valid split** of the tree is obtained by removing any set of edges, possibly empty, from the tree such that the resulting components all have values that are divisible by `k`, where the **value of a connected component** is the sum of the values of its nodes.

Return *the **maximum number of components** in any valid split*.
<hr>

### Examples
- **Example 1:** <br>
![](https://assets.leetcode.com/uploads/2023/08/07/example12-cropped2svg.jpg) <br>
**Input:** n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6 <br>
**Output:** 2 <br>
**Explanation:** We remove the edge connecting node 1 with 2. The resulting split is valid because: <br> - The value of the component containing nodes 1 and 3 is values[1] + values[3] = 12. <br> - The value of the component containing nodes 0, 2, and 4 is values[0] + values[2] + values[4] = 6. <br> It can be shown that no other valid split has more than 2 connected components.

- **Example 2:** <br>
![](https://assets.leetcode.com/uploads/2023/08/07/example21svg-1.jpg) <br>
**Input:** n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3 <br>
**Output:** 3 <br>
**Explanation:** We remove the edge connecting node 0 with 2, and the edge connecting node 0 with 1. The resulting split is valid because: <br> - The value of the component containing node 0 is values[0] = 3. <br> - The value of the component containing nodes 2, 5, and 6 is values[2] + values[5] + values[6] = 9. <br> - The value of the component containing nodes 1, 3, and 4 is values[1] + values[3] + values[4] = 6. <br> It can be shown that no other valid split has more than 3 connected components.
<hr>

### Constraints
- <code>1 <= n <= 3 * 10<sup>4</sup></code>
- `edges.length == n - 1`
- `edges[i].length == 2`
- <code>0 <= a<sub>i</sub>, b<sub>i</sub> < n</code>
- `values.length == n`
- <code>0 <= values[i] <= 10<sup>9</sup></code>
- <code>1 <= k <= 10<sup>9</sup></code>
- Sum of `values` is divisible by `k`.
- The input is generated such that `edges` represents a valid tree.
<hr>

### Hints
- Root the tree at node `0`.
- If a leaf node is not divisible by `k`, it must be in the same component as its parent node so we merge it with its parent node.
- If a leaf node is divisible by `k`, it will be in its own components so we separate it from its parent node.
- In each step, we either cut a leaf node down or merge a leaf node. The number of nodes on the tree reduces by one. Repeat this process until only one node is left.