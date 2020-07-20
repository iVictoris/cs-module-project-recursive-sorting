# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr:list, target, start, end):
    # Your code here
    middle = start + end // 2

    if len(arr) == 0 or len(arr) == 1 and target != arr[middle]:
        return -1

    if target == arr[middle]:
        return middle

    target_is_less_than_middle = target < arr[middle]
    start = start if target_is_less_than_middle else middle + 1
    end = middle - 1 if target_is_less_than_middle else end

    return binary_search(arr, target, start, end)



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
