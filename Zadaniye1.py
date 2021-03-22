a = input()
b = input()

if len(a) <= len(b):
	print("error")
else:
	a=b+a[len(b)+1:len(a)-len(b)]
print(a)