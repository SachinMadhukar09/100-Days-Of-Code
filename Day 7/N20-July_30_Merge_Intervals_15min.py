# Link = https://leetcode.com/problems/merge-intervals/

# 20-July 07:15Am-07:30AM 15 min Not Completed

# 56. Merge Intervals
# Medium

# 8363

# 403

# Add to List

# Share
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

intervals = [[1,3],[2,6],[8,10],[15,18]]
for i in range(len(intervals)):
    for j in range(len(intervals)):
        if( intervals[i][j+1]> intervals[i+1][j]):
            intervals[i][j+1]= intervals[i+1][j+1]
            intervals.remove(intervals[i+1])
            print(intervals)
            