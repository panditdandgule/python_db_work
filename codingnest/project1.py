import re
f2=open('output.txt','w')
count=0
with open('access_log','r') as f:
    for line in f:
        check=re.findall('[0-9]{2}\.[0-9]{3}\.[0-9]{2}\.[0-9]{2}',line)
        for line in check:
            count+=1
            f2.write(line+"\n")
print("Extracted all ips successfully..")
print("Total Count:",count)
f2.close()
