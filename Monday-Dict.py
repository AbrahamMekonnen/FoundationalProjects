with open("Encrypted.txt","r+") as f:
    text = f.read()
abc = "abcdefghijklmnopqrwxyz"
values = {}
for i in text:
    if i in abc:
        values[i] = text.count(i)
dyct_sort = sorted(values, key = lambda order:order[0].lower())
print(dyct_sort)
