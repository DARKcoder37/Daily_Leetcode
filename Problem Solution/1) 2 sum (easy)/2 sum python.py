1) Brute force
class Solution(object):
    def twoSum(self, nums, target):
        #Using Two pointers P1 and P2 to represent every possible pairs of the array.
        for p1 in range(len(nums)):           
             for p2 in range(p1+1, len(nums)): 
                #If one of those pairs add together equal to the target return the answer else return None.
                 if nums[p1] + nums[p2] == target:    
                    return [p1, p2]              
        return 'None' 
