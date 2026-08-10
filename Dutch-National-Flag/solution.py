class Solution:
    def array(self,arr):
        # Three pointers divide the array into three regions:
        # 0s on the left, unknown elements in the middle,
        # and 2s on the right.
        low=0 
        mid=0
        high=len(arr)-1

        # Process elements while the unknown region exists.
        while(high>mid):

            # Move 2 to the right side.
            if arr[mid]==2:
                arr[mid],arr[high]=arr[high],arr[mid]
                high-=1
                
            # Move 0 to the left side.
            elif arr[mid]==0:
                arr[mid],arr[low]=arr[low],arr[mid]
                mid+=1
                low+=1
                
            # 1 is already in its correct region.
            elif arr[mid]==1:
                mid+=1
                
     
        return arr 
                    
