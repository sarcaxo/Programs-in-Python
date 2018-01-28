def kadane(A):
    max_sum = max_global =  A[0]
    for i in range(1,len(A)):
        max_sum = max(A[i], max_sum + A[i])
        if max_sum > max_global:
            max_global = max_sum
    return max_global



#driver program

size = int(input("Enter the size of the array\n"))
A = list()
print("\n ENter the array elements one by one : \n")
for i in range(0,size):
    A.append(input())

print(" The Max Sum Array is : " , str(kadane(A)))
        
