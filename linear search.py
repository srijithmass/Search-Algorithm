''' 
Program for linear search method to match the item in a list
Developed by: SRIJITH R
RegisterNumber: 21004191
'''
def linearSearch(array,n,k):
    for i in range(0,n):
        if array[i]==k:
            return i
    return -1
array = eval(input())
# sort the array
array.sort()
print(array)
# k-item to be seared for
k = eval(input()) 
# get the length of array and store in the variable n
n=len(array)
# use the function for linear search
result=linearSearch(array,n,k)
# use if-else to print sorted array and "Element not found" if the item is not present in the list otherwise print sorted array and "Element found at index: ", result
if result>=0:
    print("Element found at index: ",result)
else:
    print("Element not found")