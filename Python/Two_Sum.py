class Solution(object):
    def twoSum(self,arr,target):
        high=len(arr)
        
        if(high<=0):
            return -1
        for i in range(0,high):
            for j in range(i+1,high):
                tar=arr[i]+arr[j]
                if(tar==target):
                    return[i,j]
