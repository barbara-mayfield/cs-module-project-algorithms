'''
Input: a List of integers
Returns: a List of integers
'''

'''
Understand
----
We're writing a function that takes an array (list) of numbers and moves
each number that is NOT 0 to the left side of the arr and then returns the altered
arr. 
So essentially we are moving all the 0's to the end of the array
'''

'''
Plan
----
Create an index pointer to store the index of the next available position
Move through the array and if the arr[i] is not zero, 
swap the element at the index 'count' with the element 
at the index 'i'
'''


def moving_zeroes(arr):
    # Your code here
    count = 0

    for i in arr:
        # if the current element is not 0,
        # put the el at next free position in list
        if i:
            arr[count] = i
            count += 1

    # move all the 0's to the end of the list
    for i in range(count, len(arr)):
        arr[i] = 0
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
