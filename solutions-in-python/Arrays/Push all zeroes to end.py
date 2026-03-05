#Operations must be performed in place without using extra memory
class Solution:
	def pushZerosToEnd(self, arr):
	    start=0
	    n=len(arr)
    
    	for i in range(n):               #Loop through array
    	    if arr[i]!=0:                #If element is not 0 then add it to array from the start index then increment the index
    	        arr[start]=arr[i]
    	        start+=1
    	while start<n:                  #After inserting all non-zeroes to the array if more space is left (compared to original), then they are zeroes.
    	     arr[start]=0               #fill the extra space with zeroes until original length of array is reached
    	     start+=1
    	return arr        #This returns the array with all non-zeroes at the front and zeroes at the end.
