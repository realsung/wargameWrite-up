# decimal number to ASCII Code
import base64
a = "86 71 57 107 89 88 107 103 97 88 77 103 89 83 66 110 98 50 57 107 73 71 82 104 101 83 52 103 86 71 104 108 73 69 70 49 100 71 104 76 90 88 107 103 97 88 77 103 86 109 86 121 101 86 90 108 99 110 108 85 98 50 53 110 86 71 57 117 90 48 100 49 99 109 107 104"
string=[]
for i in a.split(' '):
	string += chr(int(i))

print(string)
result="".join(string)

print(result)
print(base64.b64decode(result))
# AuthKey : VeryVeryTongTongGuri!