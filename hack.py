import sys
f = open(sys.argv[1], 'r')
g = open(sys.argv[2], 'rb')
i = 0
data1=f.read()
data2=g.read()
data2=data2.decode("utf-8")
out=""
for i in range(len(data1)):
    t=ord(data1[i]) ^ ord(data2[i])
    print (chr(t),end="")
    i+=1
f.close()
g.close()
