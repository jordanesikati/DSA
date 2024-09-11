# Data Structures and Algorithms (DSA)

## Table of Contents
1. [Introduction](#introduction)
2. [Big-O Notation](#big-o-notation)
3. [Data Structures](#data-structures)
   - [Arrays](#arrays)
   - [Linked Lists](#linked-lists)
   - [Stacks](#stacks)
   - [Queues](#queues)
   - [Trees](#trees)
   - [Graphs](#graphs)
   - [Hash Tables](#hash-tables)
4. [Algorithms](#algorithms)
   - [Sorting Algorithms](#sorting-algorithms)
   - [Searching Algorithms](#searching-algorithms)
   - [Recursion](#recursion)
   - [Greedy Algorithms](#greedy-algorithms)
   - [Dynamic Programming](#dynamic-programming)
5. [Practice Problems](#practice-problems)
6. [References](#references)

---

## Introduction
Data Structures and Algorithms (DSA) are the foundation of efficient problem solving in computer science. This document provides an overview of key DSA concepts, their implementations, and associated algorithms.

---

## Big-O Notation
Big-O notation describes the performance of an algorithm, especially its worst-case scenario. Common time complexities include:
- O(1): Constant time
- O(n): Linear time
- O(n^2): Quadratic time
- O(log n): Logarithmic time
- O(n log n): Log-linear time

---

## Data Structures

### Arrays
- **Definition:** A collection of elements stored at contiguous memory locations.
- **Operations:** Insertion, Deletion, Traversal.
- **Time Complexity:**
  - Access: O(1)
  - Search: O(n)
  - Insert/Delete: O(n)

### Linked Lists
- **Definition:** A sequence of nodes where each node contains data and a reference to the next node.
- **Types:** Singly Linked List, Doubly Linked List, Circular Linked List.
- **Operations:** Insertion, Deletion, Traversal.
- **Time Complexity:**
  - Access: O(n)
  - Insert/Delete: O(1) at the head

### Stacks
- **Definition:** A linear data structure following LIFO (Last In, First Out) principle.
- **Operations:** Push, Pop, Peek.
- **Time Complexity:** O(1) for push/pop.

### Queues
- **Definition:** A linear data structure following FIFO (First In, First Out) principle.
- **Operations:** Enqueue, Dequeue.
- **Time Complexity:** O(1) for enqueue/dequeue.

### Trees
- **Definition:** A hierarchical data structure with nodes connected by edges.
- **Types:** Binary Tree, Binary Search Tree (BST), AVL Tree, B-Tree.
- **Time Complexity:**
  - Access/Search: O(log n) for balanced trees
  - Insert/Delete: O(log n) for balanced trees

### Graphs
- **Definition:** A collection of nodes (vertices) connected by edges.
- **Types:** Directed, Undirected, Weighted, Unweighted.
- **Common Algorithms:** BFS, DFS, Dijkstra’s Algorithm.
- **Time Complexity:**
  - BFS/DFS: O(V + E) where V is vertices and E is edges

### Hash Tables
- **Definition:** A data structure that maps keys to values for efficient lookups.
- **Operations:** Insert, Delete, Search.
- **Time Complexity:** O(1) on average, O(n) in worst case.

---

## Algorithms

### Sorting Algorithms
- **Bubble Sort:** O(n^2)
- **Selection Sort:** O(n^2)
- **Insertion Sort:** O(n^2)
- **Merge Sort:** O(n log n)
- **Quick Sort:** O(n log n) on average, O(n^2) in worst case
- **Heap Sort:** O(n log n)

### Searching Algorithms
- **Linear Search:** O(n)
- **Binary Search:** O(log n) (works on sorted arrays)

### Recursion
- **Definition:** A function that calls itself to solve subproblems.
- **Example:** Factorial, Fibonacci sequence.
- **Time Complexity:** Depends on the problem; often involves O(2^n) or O(n).

### Greedy Algorithms
- **Definition:** Solves problems by choosing the best option at each step.
- **Examples:** Kruskal’s Algorithm, Prim’s Algorithm, Huffman Coding.
- **Time Complexity:** Problem-dependent.

### Dynamic Programming
- **Definition:** Solves problems by breaking them down into subproblems and solving each subproblem just once.
- **Examples:** Fibonacci series, Knapsack problem, Longest Common Subsequence.
- **Time Complexity:** O(n^2) for many common DP problems.

---

## Practice Problems
1. Implement a binary search algorithm.
2. Solve the knapsack problem using dynamic programming.
3. Implement a stack using an array.
4. Find the shortest path in a graph using Dijkstra’s algorithm.

---

## References
- "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein.
- GeeksforGeeks: [Data Structures and Algorithms](https://www.geeksforgeeks.org/data-structures/)
- W3Schools: [DSA](https://www.w3schools.com/dsa/index.php)
- LeetCode: [DSA Practice](https://leetcode.com)
