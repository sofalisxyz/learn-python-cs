# print numbers from 1 to n recursively
def print_nums(n):
    if n > 0:
        print_nums(n - 1)
        print(n)