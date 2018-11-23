num = raw_input().rstrip()
numLen = len(num)
mid = numLen >> 1
if (numLen & 1):
	print(num[:mid] + "*" + num[mid+1:])
else:
	print(num[:mid-1] + "**" + num[mid+1:])
