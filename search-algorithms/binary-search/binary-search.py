def binary_search(arr, x): 
    low = 0
    mid = 0
    high = len(arr) -1
    while low<=high: 
        mid = (low+high)//2
        if x>arr[mid]: 
            low = mid+1
        elif x<arr[mid]: 
            high = mid-1
        else: 
            return mid
    return None
    
arr1 = [ 1, 2, 3, 4, 7, 40 ]
x = 4

arr2 = [ 2, 3, 4, 10, 40, 45, 80 ]
y = 2

arr3 = [ 2, 3, 4, 10, 40 ]
z = 40
a=70

print(binary_search(arr1,x))#3
print(binary_search(arr2,y))#0
print(binary_search(arr3,z))#4
print(binary_search(arr3,a))#None