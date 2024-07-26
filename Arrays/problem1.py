from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            
            # Divide the array into two halves
            mid = len(nums) // 2
            leftHalf = nums[:mid]
            rightHalf = nums[mid:]
            
            # Recursively sort both halves
            leftSorted = mergeSort(leftHalf)
            rightSorted = mergeSort(rightHalf)
            
            # Merge the sorted halves
            return merge(leftSorted, rightSorted)

        def merge(left, right):
            sortedArray = []
            leftIndex = 0
            rightIndex = 0
            
            # Merge the two arrays while keeping the order
            while leftIndex < len(left) and rightIndex < len(right):
                if left[leftIndex] <= right[rightIndex]:
                    sortedArray.append(left[leftIndex])
                    leftIndex += 1
                else:
                    sortedArray.append(right[rightIndex])
                    rightIndex += 1
            
            # If there are remaining elements in the left array, add them
            while leftIndex < len(left):
                sortedArray.append(left[leftIndex])
                leftIndex += 1
            
            # If there are remaining elements in the right array, add them
            while rightIndex < len(right):
                sortedArray.append(right[rightIndex])
                rightIndex += 1
            
            return sortedArray
        
        # Call merge_sort to sort the array
        return mergeSort(nums)
