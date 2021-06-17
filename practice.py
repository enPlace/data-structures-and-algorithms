def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j-1

    print(arr)


arr1 = [4,3,2,7,6,10,20,8,1]
insertion_sort(arr1)