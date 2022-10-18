#----------------------Timing and profiling code-----------------------#
'''
In this chapter, you will learn how to gather and compare runtimes between different coding 
approaches. You'll practice using the line_profiler and memory_profiler packages to profile 
your code base and spot bottlenecks. Then, you'll put your learnings to practice by replacing 
these bottlenecks with efficient Python code.'''

#----------------------Examining runtime-----------------------#
#----------------------Using %timeit: your turn!-----------------------#
'''
You'd like to create a list of integers from 0 to 50 using the range() function. However, you 
are unsure whether using list comprehension or unpacking the range object into a list is faster. 
Let's use %timeit to find the best implementation.

For your convenience, a reference table of time orders of magnitude is provided below (faster at 
the top).

symbol	    name	        unit (s)
ns	        nanosecond	    10-9
µs (us)	    microsecond	    10-6
ms	        millisecond	    10-3
s	        second	        100
'''

# # Create a list of integers (0-50) using list comprehension
# nums_list_comp = [num for num in range(51)]
# print(nums_list_comp)

# # Create a list of integers (0-50) by unpacking range
# nums_unpack = [*range(51)]
# print(nums_unpack)

# from timeit import timeit
# time_exe1 = timeit("""nums_list_comp = [num for num in range(51)]""")
# time_exe2 = timeit("""nums_unpack = [*range(51)]""")
# print(time_exe1,time_exe2)

'''
Question:
Use %timeit within your IPython console (i.e. not within the script.py window) to compare the 
runtimes for creating a list of integers from 0 to 50 using list comprehension vs. unpacking the 
range object. Don't include the print() statements when timing.

Which method was faster?

Possible Answers

List comprehension was faster than unpacking range().

Unpacking the range object was faster than list comprehension.  (Answer:True)

Both methods had the same runtime.
'''

#----------------------Using %timeit: specifying number of runs and loops-----------------------#
'''
A list of 480 superheroes has been loaded into your session (called heroes). You'd like to analyze 
the runtime for converting this heroes list into a set. Instead of relying on the default settings 
for %timeit, you'd like to only use 5 runs and 25 loops per each run.

What is the correct syntax when using %timeit and only using 5 runs with 25 loops per each run?

Possible Answers:

timeit -runs5 -loops25 set(heroes)
%%timeit -r5 -n25 set(heroes)
%timeit set(heroes), 5, 25
%timeit -r5 -n25 set(heroes) True
'''

#----------------------Using %timeit: formal name or literal syntax-----------------------#
'''
Python allows you to create data structures using either a formal name or a literal syntax. 
In this exercise, you'll explore how using a literal syntax for creating a data structure 
can speed up runtimes.

data structure	    formal name	    literal syntax
list	                list()	           []
dictionary	            dict()	           {}
tuple	                tuple()	           ()
'''
# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))

from timeit import timeit
time_exe1 = timeit("""formal_list = list()""")
time_exe2 = timeit("""literal_list = []""")
print(time_exe1, time_exe2)

'''
Question
Use %timeit in your IPython console to compare runtimes between creating a list using the formal 
name (list()) and the literal syntax ([]). Don't include the print() statements when timing.
Which naming convention is faster?

Possible Answers:

Using the formal name (list()) to create a list is faster.

Using the literal syntax ([]) to create a list is faster. True

Both naming conventions have the same runtime.'''
