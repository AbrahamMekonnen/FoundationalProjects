import re
with open("web.txt", "r+", encoding = 'utf-8', errors = "ignore") as f:
    contents = f.read()
    


    
pattern = re.findall(r"[\w\d_.!?]+@[\w\d]+\.[\w]{2,3}",contents)

text = "hello 34h hoadf34 gadg543q hoad f353 hado5334w hd;gl;twer"
patterns = re.findall(r'[\d]+', text)

print(patterns)
