class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 1
        last_index = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                for j in range(last_index, 0, -1):
                    print(j, i)
                    if nums[j] == nums[i]:
                        continue
                    tmp = nums[i] 
                    nums[i] = nums[j] 
                    nums[j] = tmp
                    
        print(nums)
        return counter
            
            
            
            
