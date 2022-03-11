import re
matchcase=re.finditer("a{1,3}","ababaaabac")
for match in matchcase:
    print(match.start(),"..",match.group())