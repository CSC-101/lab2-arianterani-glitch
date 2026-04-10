#Task 4a

from typing import Optional

def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # What is the value of test on each call? test1: False  test2: True
    if test:                            # What is this check preventing?    The test prevents the access of idx that is
                                        # outside the bounds of the list, preventing an index error
        return L[idx]
    else:
        return None

first = checked_access([1, 0, 1], 9)     # What is the value of first?  first: None
second = checked_access([1, 0, 1], 2)    # What is the value of second? second: 1
print()

#Task4b
def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # For which call below is this statement evaluated
                                                      # and what are the values being added?
    # first1 is being evaluated since the list length is greather than
    # 2. The values being added are the strings length for each position of string in the list.
    # It adds up to 9, (4 in 'this' + 2 in 'is' + 3 in 'the' = 9)

    elif len(L) > 1:                                  # For which call below is this statement evaluated
                                                      # and what are the values being added?
        result = len(L[0]) + len(L[1])                # The last call (third3) is being evaluated here, with the result
                                                      # being 11


    elif len(L) > 0:

        result = len(L[0])                            # For which call below is this statement evaluated
    else:                                             # and what are the values being added?
        result = 0                                    # The second call here since the length of the list is above 0 but
                                                      # is not greater than 1. The values being added results in 11.
    return result

first1 = length_sum(["this", "is", "the", "first", "call"])
second2 = length_sum(["second call"])
third3 = length_sum(["another", "call"])
print()

#Task 4c
def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first_1 = surprising(words, "Avoid")
second_2 = surprising(words, "such.")
                                                 # What is the value of words at this point? words: ['this', 'is', 'confusing', 'code', 'AVOID', 'such.']
                                                 # What are the values of first and second at this point? first and second = words
                                                 # What happened? .append added "Avoid" and "such." after the 2 function calls
                                                 # to the original list: words.
print()