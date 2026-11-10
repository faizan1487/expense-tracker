class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # if i minus each element from k
        # i will know what to add in each element to make it equal to k
        # i will need to remember if i saw that sum before
        previous_sums = {}
        previous_sums[0] = 1
        subarray_count = 0
        running_sum = 0
        for i in nums:
            running_sum += i
            print("running_sum", running_sum)
            remaining_sum = running_sum - k
            print("remaining_sum", remaining_sum)
            print("previous_sums", previous_sums)
            if remaining_sum in previous_sums:
                subarray_count += previous_sums[remaining_sum]
                previous_sums[remaining_sum] += 1

            if running_sum in previous_sums:
                previous_sums[running_sum] += 1
            else:
                previous_sums[running_sum] = 1
            print("previous_sums", previous_sums)
            print("-------")

        return subarray_count


sol = Solution()
nums = [1,2,3]
k = 3
print(sol.subarraySum(nums, k))
