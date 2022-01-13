''' 
Program to find the element in a list using Binary Search(Iterative Method).
Developed by:SRIJITH R
RegisterNumber: 21004191
'''
def binarySearchIter(array, k, low, high):
    while(low<=high):
        mid=low+(high-low)//2
        if array[mid]==k:
            return mid
        elif array[mid]<k:
            low=mid+1
        else:
            high=mid+1
    return -1
array=eval(input())
#sort the array
array.sort()
print(array)
#k-item to be searched
k=eval(input()) 
low=0
high= len(array)-1
# use the binary search function to find the item in the list
result=binarySearchIter(array, k, low, high)
# use if-else to print sorted array and "Element not found" if the item is not present in the list otherwise print sorted array and "Element found at index: ", result
if result>=0:
    print("Element found at index: ",result)
else:
    print("Element not found")