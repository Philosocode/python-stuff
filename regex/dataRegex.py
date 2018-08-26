import re
pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')
with open('data.txt', 'r') as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match)
