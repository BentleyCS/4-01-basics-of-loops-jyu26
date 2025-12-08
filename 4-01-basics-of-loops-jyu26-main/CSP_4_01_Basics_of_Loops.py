#All questions must use a loop for full points.
import random

def oddNumbers(n:int) ->str:
    """
    Print out all odd numbers from 1 to n(inclusive) in a single string seperated by spaces.
    example oddNumbers(5) -> "1 3 5"
    example oddNumbers(8) -> "1 3 5 7"
    example oddNumbers(-8) -> ""
    """
    x = 1
    string =""
    while x<=n:
        string = string + f"{x} "
        x+=2
    correctString = string[:len(string)-1]
    print(correctString)
    return(correctString)
oddNumbers(9)

def backwards(n)-> int:
    """
    modify the below function such that it prints out all the numbers from n to 1
    inclusive starting at n and counting down to 1
    example backwards(5) -> "5 4 3 2 1"
    example backwards(8) -> "8 7 6 5 4 3 2 1"
    example backwards(-2) -> ""
    """

    string = ""
    while n>=1:
        string = string + f"{n} "
        n-=1
    correctString = string[:len(string)-1]
    print(correctString)
    return(correctString)
backwards(8)



def randomRepeating():
    """
    Print out a random number from 1-10 until you get a 10. Then print out how many
    times it took to roll a 10
    NOTE: Given randomness no test for this question
    :return:
    """
    tries = 0

    x=random.randint(1,10)
    while x<10:
        tries += 1
        x=random.randint(1,10)
    tries += 1
    print(f"it took {tries} tries to get a 10")
    return(tries)

randomRepeating()

def randomRange(n):
    """
    Generate a random number from 1 to 100 n number of times. Then after that is
    done print out what the highest number and the lowers number was from the rolled numbers.
    NOTE: Given randomness no test for this question
    :param n:
    :return:
    """

    """
    highest=1
    lowest=100
    for x in range(0,n):
        n=random.randint(1,100)
        print(n)
        if n>highest:
            highest = n
        if n<lowest:
            lowest = n
    print(f"highest = {highest}, lowest = {lowest}")
    """

    for x in range(0,n):
        n = random.randint(1,100)
        if x==0:
            highest = n
            lowest = n
        print(n)
        if n>highest:
            highest = n
        if n<lowest:
            lowest = n
    print(f"highest = {highest}, lowest = {lowest}")
randomRange(20)

def reverse(word:str)->str:
    """
    Takes in a string as an argument and return the given string in reverse.
    example reverse("cat") -> "tac"
    example reverse("Hello") -> "olleH"
    """
    reversed = ""
    for x in range(len(word)-1,-1,-1):
        reversed += word[x]
        print(f"x={x}, word[x]={word[x]}, reversed={reversed}")

    print(reversed)
    return(reversed)

def fizzBuzzContinuous(n):
    """
    Modify the function such that it does the fizzbuzz operation on all numbers
    from 1 to n(inclusive).
    Fizz buzz is defined as
    if the number is divisble by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.

    As with above questions add each anseer to a string and return the final string.
    :param n:
    :return:
    """
    result=""
    for x in range(1,n+1):
        if x%3==0 and x%5==0:
            result+= "fizzbuzz "
        elif x%5==0:
            result+= "buzz "
        elif x%3==0:
            result+= "fizz "
        else:
            result+= str(x)+ " "
    resultFinal = result[:len(result)-1]

    return(resultFinal)


def collatz(n):
    """
    Modify this function such that it mimics the collatz conjecture starting at n
    and prints out each number.
    The collatz conjecture is that if n is an even number divide it by 2. if n is
    an odd number multiply it by 3 and add 1.
    Repeat this process until n == 1.
    :param n:
    :return:
    """
    x=n
    result = ""
    while x!=1:
        result += str(x)+" "
        if x%2==0:
            x=int(x/2)
        else:
            x = x*3+1
    result += str(x)
    return(result)

def fibonacci(n):
    """
    for the given argument n print out the first n numbers of the fibonacci
    sequence in a single string sperated by spaces.
    The fibonacci sequence is defined as a sequence that starts with 0 then 1 as
    the first two numbers. Every subsequent number is the prior two numbers added together.
    Example fibonacci(6) -> "0 1 1 2 3 5"
    Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    Example fibonacci(1) -> "0"
    :param n:
    :return:
    """

    if n==0:
        return ("")
    elif n==1:
        return("0")

    i = 0
    j = 1
    result = "0 1"
    for x in range (2,n):
        result += " " + str(i+j)
        i, j = j, i+j
    return (result)

print(fibonacci(300))