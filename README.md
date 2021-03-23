# pands-problem-sheet
Weekly problem sheets

Contents:
1. bmi.py - week 2 exercise
2. secondstring.py - week 3 exercise
3. collatz.py - week 4 exercise
4. weekday.py - week 5 exercise
5. squareroot.py - week 6 exercise
6. es.py - week 7 exercise
7. plottask.py - week 8 exercise


Details:
1. bmi.py - this program calculates Body Mass Index (BMI)
The inputs are the person's height in centimetres and weight in kilograms.
The output is their weight divided by their height in metres squared.
Reference to BMI claculation formula: https://en.wikipedia.org/wiki/Body_mass_index

2. secondstring.py - this program asks a user to input a string and outputs every second letter in reverse order.
Two solutions are offered for this task, the second one is just a shorter/combined version of the first.
Reference on how to reverce a string: https://www.w3schools.com/python/python_howto_reverse_string.asp

3. collatz.py - this program asks the user to input any positive integer and outputs the successive values of the following calculation:
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
Program ends when the current value is one.

4. weekday.py - this program outputs whether or not today is a weekday.
References:
To get today's date https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
To get day's number https://www.hellocodeclub.com/python-get-day-of-week/

5. squareroot.py - this program finds approximate square root of a positive floating-point number (entered by user) using Newton's method.
Calculation is based on the following formula:
root = 0.5 * (guess + (num/guess))
where num - number of which we are trying to find a square root
guess - number which we assume to be a square root of num
Reference: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N

6. es.py - this program reads in a text file and outputs the number of letter e's it contains.
Reference to parcing arguments using sys
 https://stackoverflow.com/questions/7033987/python-get-files-from-command-line and
 https://realpython.com/python-command-line-arguments/#a-few-methods-for-parsing-python-command-line-arguments

7. plottask.py - this program displays a plot of the functions f(x)=x, g(x)=x**2 and h(x)=x**3 in the range [0, 4] on the one set of axes.
Reference: mainly w3wchools Python Matplotlib has been used