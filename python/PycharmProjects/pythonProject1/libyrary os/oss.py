with open("myfile.txt", "r") as f:
    data = f.read()

f = open("baso.txt", "w")
f.write("Hello, world!")
f.close()
