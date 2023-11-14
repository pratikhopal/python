#Adding the time complexity O(A+B)

def add_complexity(a,b):
    for i in range(a):  #time complexity is O(a)
        print(a)

    for j in range(b):  #time complexity is O(b)
        print(b)
                        #therefore since the input is where O(b) runs 
                        # after O(a) hence 
                        #the time comoplexity will be O(a+b) 
add_complexity(5,10)


#Adding the time complexity O(A*B)
def multply_complexity(a,b):
    for i in range(1,a):      #time complexity is O(a)
        for j in range(1,b):  #time complexity is O(b)
            print(i,j)        #therefore since the input is where O(b) runs inside O(a) 
                              #the time comoplexity will be O(a*b) 

multply_complexity(5,6)