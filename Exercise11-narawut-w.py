num=int(input("input number:"))
text=""
for i in range(num):
    for j in range(num-i):
        text+=" "
    for j in range(i+1):
        text+="*"
    for j in range(i):
        text+="*"
    text+="\n"
print(text)