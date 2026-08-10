# Sort 0s, 1s, and 2s

## Problem

Given an array containing only `0`, `1`, and `2`, sort the array in ascending order.

For example:

Input:

[2, 0, 1, 2, 0]

Output:

[0, 0, 1, 2, 2]

## Approach

We use the Dutch National Flag algorithm.

Instead of using a normal sorting algorithm, we divide the array into four regions:

[ 0s | 1s | unknown | 2s ]

We use three pointers:

- `low` → boundary of the 0s region
- `mid` → current element being examined
- `high` → boundary of the 2s region

Initially:

```text
low = 0
mid = 0
high = n - 1
