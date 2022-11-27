#Abraham
with open("space2.txt","r+") as f:
    splits = f.read()
    splits = splits.split()
    splits = " ".join(splits)
    splits = splits.split(". ")
    
    splits = " .\n".join(splits)
    splits = splits.split("love")
    splits = "LOVE".join(splits)
    print(splits)
