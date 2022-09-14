def bubbleSort(array):
    n = len(arr)
    
    for i in range(n):
        sortert = False
        
        for j in range(0, n -i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sortert = True
                
        if sortert == False:
            break
                
arr = [1,3,5,86,20,0,22,66,46]

bubbleSort(arr)

print("Sorted array is: ")
for i in range(len(arr)):
    print("%d" %arr[i], end=" ")
            
