import os
for i in range(255):
	str = 'A'*i
	print(i)
	os.system("./ovrflw "+str)
