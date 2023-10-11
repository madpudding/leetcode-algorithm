__author__ = 'mad&pudding'


def selection_sort(nums: list[int]):
    """选择排序"""
    n = len(nums)
    for i in range(0, n):
        k = i
        for j in range(i+1, n):
            if nums[i] < nums[j]:
                k = j
        nums[i], nums[k] = nums[k], nums[i]
