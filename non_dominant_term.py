#non dominant term

def non_dominant_term(n):
    for i in range(n):       #--> O(n)
        for j in range(n):   #--> O(n)
            print(i,j)       #--> therefore the time complexity is O(n^2)

    for k in range(n):       #-->O(n)
        print(k)
                             #therefore the time complexity of this function is O(n^2+n), 
                             #but since the n^2 is the higher value (dominant term) 
                             #we can ignore the n. therefore the final time complexity of the 
                             #fumction is O(n^2). 
print(non_dominant_term(5))