with open("list.txt", "w+") as f:
    write = f.write("hi how are you doing. attempt number one should work")


vowel = "aioue"
with open("list.txt", "r+") as f:
    read = f.read()

counter =  {i:read.count(i) for i in read if i in vowel}
print(sorted(counter))

        
    
    

    
