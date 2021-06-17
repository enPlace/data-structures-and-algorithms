def insertion_sort(arr):
    print(arr, "initial array")
    for i in range(1, len(arr)):
        j = i
        while arr[j]<arr[j-1] and j>0:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1
            print(arr)
        

arr1 = [4,3,2,7,6]
insertion_sort(arr1)
