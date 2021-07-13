import re
findout=re.compile("i*")
print(findout.findall("Osman is a good boy"))
print(re.split("[a-e]", "Hi this is Osman"))
print(re.sub("shi", "dim", "I am Shirin. yes it is Shirin",flags=re.IGNORECASE))
regex=r"([a-zA-Z]+) (\d+)"
match=re.search(regex, "I was born on June24")

try:
 print(match.start(),match.end())
except:
    print("Not Present")
def checkPresent(date):
    if (not date):
        print("Empty")
    else:
        regex=r"([a-zA-Z]+) (\d+)"
        match=re.search(regex,date)
        try:
            print(match.start(),match.end())
        except:
            print("Not Present")
checkPresent("")
checkPresent("I was born on June 24")            


