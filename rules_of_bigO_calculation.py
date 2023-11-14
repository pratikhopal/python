# Rule 1: Any assignment statements and if statements are executed once 
#         hence the big O is O(1)
#
#Rule 2:  A simple for loop from O to N will have for loop as O(n)
#
#Rule 3:  A nested for loop will have the time complexity as O(n^2)
#
#Rule 4:  A loop with a controlled parameter which does divide and conqurer.
#
#Rule 5:  When dealing with multiple statements just add them ........... example below




from array import array


myarray = array('i',[1,2,3,7,5,6,4])

def find_biggest_number(myarray):
    biggest_number = myarray[0]                 #--------------> O(1)
    for i in range (1,len(myarray)-1):                #--------------> O(n)
        if biggest_number < myarray[i]:         #--------------> O(1)
            biggest_number=myarray[i]           #--------------> O(1)
    print(biggest_number)                       #--------------> O(1)

#therefore O(find_biggest_number) = O(1) + O(n) + O(1) + O(1) + O(1)
#                                 = O(1+n+1+1+1)
#                                 = O(3+n)
# as we can drop constants        = O(n)
find_biggest_number(myarray)

