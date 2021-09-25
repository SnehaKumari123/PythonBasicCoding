def bubbleSort(arr):
    n = len(arr)
 
    # Traversel of all array elements
    for i in range(n):
 
        # Biggest number is at place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(j,i)
            print(arr)
 
# Driver code to test the solution
arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)
 
print ("Sorted array is:")
print(arr)
