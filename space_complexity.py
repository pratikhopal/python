#space complexity with O(n)

def sum(n):
    print(n)
    if n<=0:
        print(n)
        return 0
    print(n)
    return n + sum(n-1)


sum(3)