
# Problem:
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Description:
Objective:
Given an array of integers "nums", your task is to sort the array in ascending order and return the sorted array.

Constraints:

1- You must solve this problem without using any built-in sorting functions.
2- The algorithm must have a time complexity of 𝑂(𝑛log𝑛)
3- The solution should use the smallest space complexity possible.

# Example:
Input: nums = [5, 2, 9, 1, 5, 6]
Output: [1, 2, 5, 5, 6, 9]

# Approach:
To meet the O(nlogn) time complexity requirement, you can use sorting algorithms such as Merge Sort or Quick Sort. Both algorithms typically achieve the desired time complexity, but they differ in space complexity and implementation details.

1- Merge Sort:

Time Complexity: O(nlogn)
Space Complexity: O(n)

Description: Merge Sort is a stable, comparison-based sorting algorithm. It works by dividing the array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together.

2- Quick Sort:

Time Complexity: O(nlogn) on average
Space Complexity: O(logn) with in-place partitioning

Description: Quick Sort is a comparison-based sorting algorithm that uses a divide-and-conquer approach. It works by selecting a 'pivot' element and partitioning the array around the pivot such that elements less than the pivot are on the left, and elements greater than the pivot are on the right. It then recursively sorts the partitions.

