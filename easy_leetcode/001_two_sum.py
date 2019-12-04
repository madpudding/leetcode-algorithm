__author__ = 'mad&pudding'

# 题目描述(CN)：给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# https://leetcode.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution.
# Maintain a mapping from each number to its index.
# Check if target - num has already been found.
# Time - O(n)
# Space - O(n) for the dictionary


class Solution:
    @staticmethod
    def two_sum(nums, target):
        num_index = dict()
        for index, num in enumerate(nums):
            if target - num in num_index:
                return [num_index[target-num], index]
            num_index[num] = index
        return []
