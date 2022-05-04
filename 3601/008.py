s = input()
out=""
for i in s:
    if i in "abc":
        out += "2"
    elif i in "def":
        out += "3"
    elif i in "ghi":
        out += "4"
    elif i in "jkl":
        out += "5"
    elif i in "mno":
        out += "6"
    elif i in "pqrs":
        out += "7"
    elif i in "tuv":
        out += "8"
    elif i in "wxyz":
        out += "9"
    elif i.isdigit():
        out += i
    elif i.isupper():
        if i == "Z":
            out += "a"
        else:
            i = chr(ord(i.lower())+1)
            out += i
    else:
        out += i
print(out)


            