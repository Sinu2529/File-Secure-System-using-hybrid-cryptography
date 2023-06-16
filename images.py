file = open('model.jpg',"rb")

image = file.read()
file.close()

image = bytearray(image)

key = 48

for i,j in enumerate(image):
	image(i) == j^key

	file = open("decrpyt.jpg","wb")
	file.write(image)
	file.close
