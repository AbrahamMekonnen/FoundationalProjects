import re
strings = "HelloHiHowAreYou"

#( "_".join(re.findall(r'[A-Z][a-z]+(?: [A-Z][\w]+)*', strings)))
expression = [strings[i:]for i in range(len(strings)) for y in range(len(strings)-1) if strings[i].isupper() and strings[i+y].islower()]
print(expression)
