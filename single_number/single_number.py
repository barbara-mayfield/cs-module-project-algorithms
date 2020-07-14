from collections import Counter

'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# U
# - We are inputing a list where every int shows up twice except ONE
# - If number shows up more than one time it won't be returned
# - Need to find a way to identify duplicates in a list and print the one that doesn't have a duplicate
# - We are getting integers in return

# P
#   - Create a new list where the single int will be stored and returned
#   - Look through the list and find the non-duped integer
#   - If item matches another in the list, do not add it to the new list
#   - We could also import Counter to find least-common element


# E
def single_number(arr):
    # Your code here
    counter = Counter(arr)
    return min(counter, key=counter.get)


# R


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
