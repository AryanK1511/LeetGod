
    if k <= 1:
        return 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product /= nums[left]
            left += 1

        number_of_subarrays += (right - left + 1)
    return number_of_subarrays