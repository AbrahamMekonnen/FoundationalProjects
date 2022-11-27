
words = "helloahg asc asd pasdaaskdf askdjla jioiusess"
count = {i: words.count(i) for i in words if i not in " "}

print(count)
