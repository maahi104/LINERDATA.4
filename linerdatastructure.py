# # QUESTION 7

def move_negative(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

# Example usage
arr = []
n = int(input("Enter number of elements: "))
for i in range(0, n):
    ele = int(input("Enter element: "))
    arr.append(ele)
arr = move_negative(arr)
print(arr)

# # QUESTION 8

def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)
    reverse = ""
    while len(stack) > 0:
        reverse += stack.pop()
    return reverse

# Example usage
string = input("Enter a string to reverse: ")
print(f"The reversed string is: {reverse_string(string)}")
