# coding quicksort for understanding

# german guy's video: https://www.youtube.com/watch?v=9KBwdDEwal8

# parameters
# arr is the list
# left is the beginning index
# right is the end index

def quickSort(arr, left, right):
    # checks if the array contains at least 2 elements
    if left < right:
        
        partitionPosition = partition(arr,left,right)
        # call quicksort on the left side and the right side of the array
        quickSort(arr, left, partitionPosition - 1)
        quickSort(arr, partitionPosition + 1, right)
def partition(arr, left, right):
    i = left
    j = right - 1
    # selecting last elem as pivot, random usually better
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            # this lets you swap without using a temp variable
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i

exampleArr = [22,11,88,66,55,77,33,44]

quickSort(exampleArr, 0, len(exampleArr) - 1)
print(exampleArr)