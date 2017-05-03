import random


def main():
    k = 10
    n = 50
    arr = []
    found_arr = []
    for i in range(n):
        arr += [random.randint(0, n)]
    for a in arr:
        if a not in found_arr and len(found_arr) <= k:
            found_arr += [a]
    print(found_arr)
if __name__ == '__main__':
    main()
