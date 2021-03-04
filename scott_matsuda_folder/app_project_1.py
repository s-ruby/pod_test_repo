'''
A couple of weeks ago, Yusuf lectured in class and shared with us some python code dealing with probability theory 
based on a coin-flipping scenario.  He mentioned an absolute value, a positive number 
denoting the difference in outcomes.  For example, if I were to flip a coin 10 times and get 6 heads and 4 tails, 
the difference in outcomes would be 2 (the difference between 4 and 6).  I would assume that the more times a coin 
is flipped, the greater the chance that the probability for either outcome (heads or tails) would be 0.5.  Also I
would expect the absolute value of the difference in outcomes to increase as the number of times a coin is flipped increases.
In lieu of examining the math (pen, paper, and crazy formulas), let's check it out in code!

from https://stackoverflow.com/questions/14882530/python-coin-toss
'''

import random

def coinToss(number):
    recordList, heads, tails = [], 0, 0 # multiple assignment
    for i in range(number): # do this 'number' amount of times
         flip = random.randint(0, 1)
         if (flip == 0):
            #   print("Heads")
              recordList.append("Heads")
         else:
            #   print("Tails")
              recordList.append("Tails")
    
    return abs(int(recordList.count("Heads")) - int(recordList.count("Tails")))

firstNumber = input('Pick an even number between 2 and 100: ')
firstResult = coinToss(int(firstNumber))
secondNumber = input('Pick a second even number that is considerably larger than the first: ')
secondResult = coinToss(int(secondNumber))
response = input(f"If you were to flip a coin, either {firstNumber} or {secondNumber} times, which number do you think would produce the greater number of differences in outcomes? ")
if response == firstNumber and firstResult > secondResult:
    print(f"You are correct.  Flipping a coin {firstNumber} times leads to a difference of {firstResult} outcomes, whereas flipping a coin {secondNumber} times amounts to a difference of {secondResult} outcomes!")
if response == secondNumber and secondResult > firstResult:
    print(f"You are correct.  Flipping a coin {secondNumber} times leads to a difference of {secondResult} outcomes, whereas flipping a coin {firstNumber} times amounts to a difference of {firstResult} outcomes!")
if response == firstNumber and firstResult < secondResult:
    print(f"Sorry, you are wrong.  Flipping a coin {firstNumber} times results in a difference of {firstResult} outcomes, whereas flipping a coin {secondNumber} times produces a difference of {secondResult} outcomes!")
if response == secondNumber and secondResult < firstResult:
    print(f"Sorry, you are wrong.  Flipping a coin {secondNumber} times results in a difference of {secondResult} outcomes, whereas flipping a coin {firstNumber} times produces a difference of {firstResult} outcomes!")
if (response == firstNumber or response == secondNumber) and firstResult == secondResult:
    print(f"The results are identical.  Flipping a coin {firstNumber} times or {secondNumber} times both result in {firstResult} different outcomes!")
