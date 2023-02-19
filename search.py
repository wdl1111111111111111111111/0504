import re
inputStr="host_ip :192.168.1.1"
replacedStr = re.sub(r":([\S]+)", "222", inputStr)
print(replacedStr)