class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
            
solucion = Solution()
print(solucion.twoSum([2,7,11,15],9))
print(solucion.twoSum([3,2,4],6))