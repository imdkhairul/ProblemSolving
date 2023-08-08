def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 1:
            return [0]
        prod = [1 for i in range(n)]
        temp = 1
        i = 1

        for i in range(n):
            prod[i] = prod[i] * temp
            temp = temp * nums[i]

        temp = 1

        for i in range(n-1, -1, -1):
            prod[i] = prod[i] * temp
            temp = temp * nums[i]

        return prod

print(productExceptSelf([1,2,3,4]))