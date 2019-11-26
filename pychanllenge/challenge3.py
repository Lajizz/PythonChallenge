#http://www.pythonchallenge.com/pc/def/equality.html
import re
with open('file.txt', 'r') as f:
    s = f.read()
result=re.findall("[^A-Z]+[A-Z]{3}[a-z][A-Z]{3}[^A-Z]+",s)
print(result)
