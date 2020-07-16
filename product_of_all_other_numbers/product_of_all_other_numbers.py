'''
Input: a List of integers
Returns: a List of integers
'''

'''
Understand
----
The output of the list at each index is going to be the 
product of ALL of the other elements in the list except for 
the current element.

We want to solve this without using division.

Input: [1, 7, 3, 4]
calculating [7*3*4, 1*3*4, 1*7*4, 1*7*3]
Expected Output: [84, 12, 28, 21]


'''

'''
Plan
----
Get the length of the input array
Make three lists, Left, Right and Output
We would need to loop over Left and Right lists and the product of
Left and Right would be sent to Output list.

These lists will need the same # of indeces as the input so we can do this by
saying [0] * length of the input.

Left list index contains the product of all numbers to the left of index
The element at L[0] would be 1 because there are no elements on the left.

Right list index would contain the product of all the numbers to the right of index.

For the Right we would do the same thing but in reverse.
We would start with the initial value of 1 in Right length - 1 where length is the 
number of elements in the array and update R index in reverse. 
'''


def product_of_all_other_numbers(arr):
    length = len(arr)

    left, right, output = [0]*length, [0]*length, [0]*length

    left[0] = 1
    for i in range(1, length):
        left[i] = arr[i-1] * left[i-1]

    right[length - 1] = 1
    for i in reversed(range(length - 1)):
        right[i] = arr[i + 1] * right[i + 1]

    for i in range(length):
        output[i] = left[i] * right[i]

    return output


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
