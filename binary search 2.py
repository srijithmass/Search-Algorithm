''' 
Program to find the element in a list using Binary Search (recursive Method).
Developed by: SRIJITH R
RegisterNumber:21004191
'''
def BinarySearch(arr, k, low, high):
    if high>=low:
        mid=low+(high-low)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]<k:
            return BinarySearch(arr,k,mid+1,high)
        else:
            return BinarySearch(arr,k,low,mid+1)
    return -1
arr = eval(input())
#sort the array
arr.sort()
print(arr)
# k is the element to be searched for
k = eval(input()) 
low=0
high=len(arr)-1
# use the binary search function to find the result
result=BinarySearch(arr, k, low, high)
# use if-else to print sorted array and "Element not found" if the item is not present in the list otherwise print sorted array and "Element found at index: ", result
if result>=0:
    print("Element found at index: ",result)
else:
    print("Element not found")