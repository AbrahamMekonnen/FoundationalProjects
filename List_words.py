import re
f = open("List_words.txt","r+")
read = f.read()
vowels = ["A","e","I","i","O","o","U","u","E","e"]




Found_words = []
Found_letters = []

for w in read.split():
    
    
    if w.startswith("a") and w.endswith("a"):
        Found_words.append(w)

        
print(len(Found_words))
            

            
