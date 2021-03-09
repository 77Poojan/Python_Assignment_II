class py_solution:
    def threeSum(self, nums):
        tempList=[]
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                for z in nums[y+1:]:
                    if(nums[x]+nums[y]+z) == 0:
                        tempList.append([nums[x], nums[y], z])
        return tempList

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))