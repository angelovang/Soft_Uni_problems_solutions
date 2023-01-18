import re

pattern = r'\b_([a-zA-Z0-9]+)\b'

line = input()
matches = re.findall(pattern,line)
if matches:
    print(','.join(matches))
  


