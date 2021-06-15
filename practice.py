def binary_search(arr, num):
    first = 0
    last = len(arr) -1
    middle = 0

    while first<=last:
        middle = (first+last)//2
        if arr[middle]==num: 
            return middle
        elif arr[middle]<num: 
            first = middle+1
        else: 
            last = middle -1
    return "Not found"

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

