import time


def factorial(num):
    if num < 0:
        raise Exception("Please input positive number")
    if((num == 1) or (num == 0)):
        return 1
    else:
        return num*factorial(num-1)


if __name__ == "__main__":
    max_length = 500
    list_normal = []

    compre_start = time.time()
    list_compre = [factorial(x) for x in range(0, max_length)]
    # print(f"length of list_compre : {len(list_compre)}")
    compre_end = time.time()

    normal_start = time.time()
    for x2 in range(0, max_length):
        list_normal.append(factorial(x2))
    normal_end = time.time()

    print(f"list comprehension: {compre_end-compre_start}, normal: {normal_end-normal_start}")


    # print(list_compre)
    # print(list_normal)