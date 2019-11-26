#!/usr/bin/env python3.7
#http://www.pythonchallenge.com/pc/def/ocr.html
with open('file.txt', 'r') as f:
    file_data = f.read()

characters = []
data = list(file_data)

for i in range(len(data)):
    if (65 <= ord(data[i]) <= 90) or (97 <= ord(data[i]) <= 122):
        characters.append(data[i])

text = "".join(characters)
print(text)