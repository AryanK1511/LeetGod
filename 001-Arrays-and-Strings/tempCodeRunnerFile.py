class NumArray:
#     def __init__(self, nums):
#         self.nums = nums

#     def sum_range(self, left, right):
#         ps_arr = self.create_prefix_sum_arr()
#         print(ps_arr)
#         return ps_arr[right] - ps_arr[left - 1] + self.nums[left]

#     def create_prefix_sum_arr(self):
#         prefix_sum_arr = []
#         if len(self.nums) > 0:
#             prefix_sum_arr.append(self.nums[0])
#             for i in range(1, len(self.nums)):
#                 prefix_sum_arr.append(self.nums[i] + prefix_sum_arr[len(prefix_sum_arr) - 1])
#         return prefix_sum_arr