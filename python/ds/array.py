################
# 1d array
arr: list = []

arr.append("a")
assert len(arr) == 1
assert "a" == arr[0]
arr.remove("a")
assert len(arr) == 0

arr.append("b")
arr.clear()
assert len(arr) == 0

print("Done")


################
# 2D array using list comprehension
rows, cols = (3, 4)
two_d_arr = [["a" for c in range(cols)] for j in range(rows)]
two_d_arr[0][0] = "b"
print(two_d_arr)

# Flatten 2D array
flat_arr = [i for row in two_d_arr for i in row]
print(flat_arr)

# Access kth row
k = 1
print(two_d_arr[k])

# Access kth column
k = 2
print([row[k] for row in two_d_arr])

print("Done")
