n = int(input())

# for i in range(1, n + 1):
# 	for j in range(1, n - i + 1):
# 		print(' ', end = '')
# 	for k in range(1, i + 1):
# 		print(k, end = '')
# 	print()


# for i in range(0, n + 1):
# 	for j in range(1, n - i + 1):
# 		print(n - i, end = '')
# 	print()


for i in range(1, n + 1):
	for j in range(1, n-i+1):
		print(' ', end = '')
	for k in range(1, i + 1):
		print(i + k - 1, end = '')
	for l in range(i, 1, -1):
		print(i + l - 2, end = '')
	print()