f = open("C:/Kuliah/test.txt", "w")
f.write("Woops! I have deleted the content!")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("C:/Kuliah/test.txt", "r")
print(f.read())
