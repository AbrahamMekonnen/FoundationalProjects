from bs4 import BeautifulSoup
import re
with open("stuff.mhtml", "r+") as f:
    document = BeautifulSoup(f, "html.parser")

emails = re.findall(r'[\w\d_.]+@[\w\d]+[\w]',document)
print(emails)
