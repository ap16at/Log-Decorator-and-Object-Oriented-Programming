# Andrew Perez-Napan
# ap16at
# Due Date: 1-29-21
# The program in this file is the individual work of Andrew Perez-Napan

import time
import sys


def log(*args):
    if len(args) == 1 and type(*args) == str:
        def decorator(func):
            def wrapper(*arg):
                out = sys.stdout
                file = open("logger.txt", "a")
                sys.stdout = file
                file.write("**************************************************\n")
                file.write("Calling function " + func.__name__ + ".\n")

                if len(arg) > 0:
                    file.write("Arguments:\n")
                    for i in arg:
                        file.write("\t -" + str(i) + " of type " + type(i).__name__ + "." + "\n")
                else:
                    file.write("No arguments.\n")

                file.write("Output: " + "\n")
                start = time.perf_counter()
                retval = func(*arg)
                total = time.perf_counter() - start
                file.write("Execution time: " + "%.5f s." % total + "\n")

                if retval is not None:
                    file.write("Return value: "+str(retval)+" of type "+type(retval).__name__+".\n")
                else:
                    file.write("No return value.\n")
                file.write("**************************************************\n\n")

                sys.stdout = out
                file.close()

            return wrapper

        return decorator
    else:
        def decorator(func):
            def wrapper(*arg):
                print("**************************************************")
                print("Calling function " + func.__name__)

                if len(arg) > 0:
                    print("Arguments:")

                    for i in arg:
                        print('\t - {0} of type {1}.'.format(str(i), type(i).__name__))
                else:
                    print("No arguments.")

                print("Output:")
                start = time.perf_counter()
                retval = func(*arg)
                total = time.perf_counter() - start
                print("Execution time: ", "%.5f s." % total)

                if retval is not None:
                    print('Return value: {0} of type {1}.'.format(retval, type(retval).__name__))
                else:
                    print("No return value.")
                print("**************************************************\n")

            return wrapper

        return decorator


@log()
def factorial(*nums_list):
    results = []
    for number in nums_list:
        res = number
        for i in range(number-1, 0, 1):
            res = i*res
        results.append(res)
        return results


@log("logger.txt")
def waste_time(a, b, c):
    print("Wasting time.")
    time.sleep(5)
    return a, b, c


@log("logger.txt")
def gcd(a, b):
    print("The GCD of", a, "and", b, "is ", end="")
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print(abs(a))
    return abs(a)


@log()
def print_hello():
    print("Hello!")


@log(10)
def print_goodbye():
    print("Goodbye!")


if __name__ == "__main__":
    factorial(4, 5)
    waste_time("one", 2, "3")
    gcd(15, 9)
    print_hello()
    print_goodbye()
