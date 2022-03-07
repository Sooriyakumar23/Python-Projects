# 1. Bubble sort
### Time complexity = O(n2) <----- (n-1)n/2

#arr1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
arr1 = [20, 30, 50, 10, 40, 90, 60, 70, 80, 100]
#arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

count1 = 0
count2 = 0

for i in range(len(arr1)-1):
    for j in range(len(arr1)-i-1):
        #print (i,j)
        count1 += 1
        if arr1[j] > arr1[j+1]:
            count2 += 1
            arr1[j], arr1[j+1] = arr1[j+1], arr1[j]

n = len(arr1)
print ("Length of the array:", n)
print ("Worst case scenario iterations:", (n-1)*n//2)

print ("\nSorted array is", arr1)

print ("\nNumber of iterations:", count1)
print ("Number of times fall under condition:", count2, "\n")

if count2==count1:
    print ("Worst case scenario")
elif count2 == 0:
    print ("Best case scenario")
else:
    print ("Average case scenario")
    

# 2. Insertion sort

# 3. Selection sort

# 4. Merge sort

# 5. Heap sort

# 6. Quick sort
