def print_items(n):
    for  i in range(n):
        print(i)
    for  j in range(n):
        print(j)

print_items(14)

## This ran n+n times
## so it becomes O(2n) which is same as O(n)


def print_items1(a,b):
    for  i in range(a):
        print(i)
    for  j in range(b):
        print(j)

print_items1(2,3)

## Here it is not O(n) as a,b are separate. So it is O(a+b)

