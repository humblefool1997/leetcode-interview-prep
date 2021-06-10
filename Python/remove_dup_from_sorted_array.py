# nums is the  sorted array 
# the array or list is sorted 
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
# Method is to traverse array from backwards and delete the elements if 2 consective elements are similar
nums = 0
def remove_dups_from_sorted_array(nums):
  for i in range(len(nums)-1.0,-1):
    if nums[i] == nums[i-1]:
      del nums[i]

    
