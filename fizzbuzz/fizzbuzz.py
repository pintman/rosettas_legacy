
def fizzbuzz(n):
    """
    >>> fizzbuzz(1)
    1
    >>> fizzbuzz(3)
    Fizz
    >>> fizzbuzz(6)
    Fizz
    >>> fizzbuzz(30)
    FizzBuzz
    >>> fizzbuzz(10)
    Buzz
    """
    if n % 3 == 0 and n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

if __name__ == '__main__':
    for i in range(1, 101):
        fizzbuzz(i)
