__author__ = 'mad&pudding'


def insert_sort(nums: list[int]):
    """插入排序"""
    for i in range(1, len(nums)):
        j = i-1
        base = nums[i]
        while j >= 0 and nums[j] > base:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = base

