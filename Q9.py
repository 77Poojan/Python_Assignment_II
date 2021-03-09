# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

	# Check base case
	if high >= low:

		mid = (high + low) // 2

		# If element is present at the middle itself
		if arr[mid] == x:
			return mid

		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		# Else the element can only be present in right subarray
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		# Element is not present in the array
		return -1

# Test array
arr=[]
num = int(input("Enter size of your list: "))

for i in range(0,num):
    elements = int(input(f'\nEnter the element<{i}> for your list: '))
    arr.append(elements)

x = int(input("\nEnter number to be searched : "))

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("\nElement found at index => ", str(result))
else:
	print("\nElement not found.")
