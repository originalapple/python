def binary_search(A,key,low,high):
    if (low <= high):
        middle = (low + high)//2
        if key == A[middle] : return middle
        elif (key < A[middle]) : return binary_search(A,key,low,middle-1)
        else : binary_search(A,key,middle+1,high)
    return None

A = [1,2,3,4,5,6,7,8,9,10]
key =10
low = 0
high = len(A)-1
print(binary_search(A,key,low,high))
