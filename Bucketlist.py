#Abraham
with open("myfiless.txt", "w") as f:
    L = ["get a good grade", "join the soccer team \n", "graduate \n","get a job (hopefully) \n","live life"]
    f.writelines(L)
    f.close()

with open("myfiless.txt", "a") as f:
    f.write("\n")
    f.write("hello")
x = ("This appears to be the only pirority for now")

with open("myfiless.txt", "r+") as f:
    f.read()
    f.truncate(16)
    f.write(x)

    
    
    

