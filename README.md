# python

Big O 


Big O is the metric used to guage the efficiancy of the code



Run time complexities



<h1>Constant time complexity O(1)</h1>
It is when the time required to run the operation is constant.


<h1>N time complexities O(n) linear time complexity</h1>
as the numner of input grows the time complexity also grows proportionately.

<h1>Drop constant complexity</h1>.
Now considering the function has 2 loops with each loop with time complexity of O(n)
so the time complexity for the function will O(n)+O(n) = O(2n).
but we need to drop the constant as it wont affect In algorithm analysis and "big O" notation, 
constants are typically not included because the purpose of big O notation is 
to describe the upper bound of an algorithm's time complexity in a 
simplified and asymptotic way. 
Constant factors and lower-order terms are often ignored because 
they don't provide meaningful information about the algorithm's scalability and efficiency 
as the input size grows to infinity

<h1><b>Quadratic time complexity</b></h1>
the quadratic time complexity refers to the time complexity for nested loops 
or any program that's time complexity increase by square to the input.