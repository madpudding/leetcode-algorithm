__author__ = 'mad&pudding'


def bubble_sort(nums: list[int]):
    """冒泡排序"""
    n = len(nums)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]

