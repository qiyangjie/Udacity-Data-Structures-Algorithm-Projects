def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
       """
    if len(ints)<= 0:
        return

    min_num = ints[0]
    max_num = ints[0]

    for i in range(1, len(ints)):
        if ints[i] < min_num:
            min_num = ints[i]

        if ints[i] > max_num:
            max_num = ints[i]

    return min_num, max_num


if __name__ == '__main__':
    # Example Test Case of Ten Integers
    import random

    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

    # corner case
    print("Pass" if (get_min_max([]) is None) else "Fail")
    print("Pass" if (get_min_max([1, 1]) == (1, 1)) else "Fail")
    print("Pass" if (get_min_max([-1, 3, 7]) == (-1, 7)) else "Fail")
