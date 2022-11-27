def pal(string):
        
    if string[::-1] == string:
        return True
    return False
flipped = pal("mom")
print(flipped)
