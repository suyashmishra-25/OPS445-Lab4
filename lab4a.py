#!/usr/bin/env python3

def join_sets(set1, set2):
    """ Returning all the nnumber from set 1 and set2"""

    return set1 | set2
def match_sets(set1, set2):

    """ Returning the nunmber matching in set1 and set2"""

    return set1 & set2
def diff_sets(set1, set2):

    """ Returning the number that are unique in set1 and set2"""

    return set1 ^ set2
if __name__ == '__main__':
    set1 = set(range(1, 10))
    set2 = set(range(5, 15))


    print(f"set1: {set1}")

    print(f"set2: {set2}")

    print(f"Union (join): {join_sets(set1, set2)}")

    print(f"Intersection (match): {match_sets(set1, set2)}")

    print(f"Symmetric Difference (diff): {diff_sets(set1, set2)}")


