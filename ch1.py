#----------------------------Foundations for efficiencies----------------------------#
'''
In this chapter, you'll learn what it means to write efficient Python code. You'll explore 
Python's Standard Library, learn about NumPy arrays, and practice using some of Python's built-in 
tools. This chapter builds a foundation for the concepts covered ahead.'''

#----------------------------Welcome!----------------------------#
#----------------------------Pop quiz: what is efficient----------------------------#
'''
In the context of this course, what is meant by efficient Python code?

Possible Answers

Code that executes quickly for the task at hand, minimizes the memory footprint and follows 
Python's coding style principles. True

Code that has a fast runtime, consumes a small amount of memory and can be verbose/hard to interpret (readability doesn't matter).

Code that returns a correct result regardless of the execution time and resource consumption.

Correct! Writing efficient Python code minimizes runtime and memory usage while also following 
the idioms in the Zen of Python'''

#----------------------------A taste of things to come----------------------------#
'''
In this exercise, you'll explore both the Non-Pythonic and Pythonic ways of looping over a list.

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

Suppose you wanted to collect the names in the above list that have six letters or more. 
In other programming languages, the typical approach is to create an index variable (i), 
use i to iterate over the list, and use an if statement to collect the names with six letters 
or more:

i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1

Let's explore some more Pythonic ways of doing this.'''

# '''
# 1) Print the list, new_list, that was created using a Non-Pythonic approach.'''
# # Print the list created using the Non-Pythonic approach
# names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
# i = 0
# new_list= []
# while i < len(names):
#     if len(names[i]) >= 6:
#         new_list.append(names[i])
#     i += 1
# print(new_list)

# '''
# 2) A more Pythonic approach would loop over the contents of names, rather than using an index variable.
# Print better_list.'''
# # Print the list created by looping over the contents of names
# better_list = []
# for name in names:
#     if len(name) >= 6:
#         better_list.append(name)
# print(better_list)

# '''
# 3) The best Pythonic way of doing this is by using list comprehension. Print best_list.'''
# # Print the list created by using list comprehension
# best_list = [name for name in names if len(name) >= 6]
# print(best_list)

'''
Great work! Don't get too caught up in the coding concepts just yet (you'll practice using lists, 
for loops, and list comprehensions later on). The important thing to notice here is that following 
some of Python's guiding principles allows you to write cleaner and more efficient code.

Remember, Pythonic code == efficient code. You'll explore these, and other, Pythonic concepts 
later on in the course, but for now, this is just a taste of things to come!'''

#----------------------------Zen of Python----------------------------#
'''
In the video, we covered the Zen of Python written by Tim Peters, which lists 19 idioms 
that serve as guiding principles for any Pythonista. Python has hundreds of Python Enhancement 
Proposals, commonly referred to as PEPs. The Zen of Python is one of these PEPs and is documented 
as PEP20.

One little Easter Egg in Python is the ability to print the Zen of Python using the command 
import this. Let's take a look at one of the idioms listed in these guiding principles.

Type and run the command import this within your IPython console and answer the following question:

What is the 7th idiom of the Zen of Python?'''

# import this

'''
Possible Answers:

Flat is better than nested.
Beautiful is better than ugly.
Readability counts. ----------------------------(True)
Python is the best programming language ever.

That's correct! Python has a design philosophy that emphasizes readability. Throughout the 
course, you'll see that writing efficient Python code goes hand in hand with writing code 
that is easy to understand. Faster code is good, but faster & readable code is best!'''


#----------------------------Building with built-ins----------------------------#
'''
Built-in practice: range()
In this exercise, you will practice using Python's built-in function range(). Remember that 
you can use range() in a few different ways:

1) Create a sequence of numbers from 0 to a stop value (which is exclusive). This is useful when 
you want to create a simple sequence of numbers starting at zero:

range(stop)

# Example
list(range(11))

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
2) Create a sequence of numbers from a start value to a stop value (which is exclusive) with a step 
size. This is useful when you want to create a sequence of numbers that increments by some value other 
than one. For example, a list of even numbers:

range(start, stop, step)

# Example
list(range(2,11,2))

[2, 4, 6, 8, 10]
'''
# Create a range object that goes from 0 to 5
nums = range(0, 6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1,12,2)]
print(nums_list2)