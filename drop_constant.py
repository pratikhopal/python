#drop constant



def drop_constant(n):
    for i in range(n):
        print(i*5)
    print("End of the first for loop which has the time coplexity of O(n)")
    for j in range(n):
        print(j*5)
    print("End of the second for loop which has a time complexity of O(n)")

drop_constant(11)

    #Now considering the function has 2 loops with each loop with time complexity of O(n)
    #so the time complexity for the function will O(n)+O(n) = O(2n).
    # but we need to drop the constant as it wont affect In algorithm analysis and "big O" notation, 
    # constants are typically not included because the purpose of big O notation is 
    # to describe the upper bound of an algorithm's time complexity in a 
    # simplified and asymptotic way. 
    # Constant factors and lower-order terms are often ignored because 
    # they don't provide meaningful information about the algorithm's scalability and efficiency 
    # as the input size grows to infinity
    