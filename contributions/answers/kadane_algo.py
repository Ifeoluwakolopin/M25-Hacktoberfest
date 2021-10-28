def maxSubArraySum(a,size:int):
    """
    This code helps to find thhe maximum sum of a subarray
    within the larger array 'a'
    """
    max_so_far = a[0]
    max_ending_here = 0
      
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0  
    return max_so_far