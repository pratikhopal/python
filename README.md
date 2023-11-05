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


<h1>Non Dominant term</h1>
If we have a time complexity of O(n^2+n), in that case the dominant value is n^2 here 
we can ignore/drop the less or non dominant term and consider the time complexity to be
O(n^2).


<h1>Logarithmic time complexity</h1>
In algorithmic analysis, a time complexity of O(log n) is often referred to as "logarithmic time complexity." Algorithms with logarithmic time complexity are highly efficient because their running time increases very slowly as the input size, denoted by "n," grows. As "n" increases, the running time grows logarithmically rather than linearly or quadratically.

Logarithmic time complexity is typically associated with algorithms that divide the input into smaller and smaller portions, commonly by employing a divide-and-conquer approach. Binary search is a classic example of an algorithm with O(log n) time complexity. In binary search, the input is repeatedly divided in half, and the algorithm quickly narrows down the search space to find the desired element.

Logarithmic time complexity is much more desirable than linear (O(n)) or quadratic (O(n^2)) time complexities for large input sizes because it signifies efficient performance that doesn't significantly degrade as the input size grows.