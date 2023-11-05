Big O 


Big O is the metric used to guage the efficiancy of the code



Run time complexities



Constant time complexity O(1)
It is when the time required to run the operation is constant.


N time complexities O(n) linear time complexity
as the numner of input grows the time complexity also grows proportionately.

Drop constant complexity.
#Now considering the function has 2 loops with each loop with time complexity of O(n)
#so the time complexity for the function will O(n)+O(n) = O(2n).
# but we need to drop the constant as it wont affect In algorithm analysis and "big O" notation, 
# constants are typically not included because the purpose of big O notation is 
# to describe the upper bound of an algorithm's time complexity in a 
# simplified and asymptotic way. 
# Constant factors and lower-order terms are often ignored because 
# they don't provide meaningful information about the algorithm's scalability and efficiency 
# as the input size grows to infinity