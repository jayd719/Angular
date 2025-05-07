


def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """

    if len(nums) <= k:
        return sum(nums) / len(nums)

    max_average = sum(nums[:k]) / k
    for i in range(len(nums) - k):
        j = i + k
        curr_average = sum(nums[i:j]) / k
        if curr_average > max_average:
            max_average = curr_average
    return max_average

arr = [1,12,-5,-6,50,3]
print(findMaxAverage(arr,4))