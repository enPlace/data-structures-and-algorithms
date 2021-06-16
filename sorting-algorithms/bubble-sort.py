def bubble_sort(arr):
    print(arr) 
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] >arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                print(arr)


arr1 = [4,3,2,1]
bubble_sort(arr1)

