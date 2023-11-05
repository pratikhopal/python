def quadratic_time_complexity(n):
    for i in range(n):        #-------> O(n) is time complexity for this loop
        for j in range (n):   #-------> O(n) is also the time complexity for this loop
                              #-------> as the second is a nested the time complexity is O(n*n)
                              #-------> or O(n^2) also called as quadratic time complexity. the worst
            print(i,j)

print(quadratic_time_complexity(4))