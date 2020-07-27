# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA: list, arrB: list):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    for index in range(len(merged_arr)):
        first, second = arrA.pop(0) if len(arrA) else None, arrB.pop(0) if len(arrB) else None

        if first is None:
            merged_arr[index] = second
        elif second is None:
            merged_arr[index] = first
        elif first < second:
            merged_arr[index] = first
            arrB = [second] + arrB
        elif second < first:
            merged_arr[index] = second
            arrA = [first] + arrA
        else:
            # both are the same
            merged_arr[index] = first
            arrB = [second] + arrB

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        return arr
    
    half_array = len(arr) // 2
    left, right = arr[:half_array], arr[half_array:]

    return merge(merge_sort(left), merge_sort(right))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

