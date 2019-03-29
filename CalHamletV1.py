#CalHamletV1.py
def getText():
    txt = open("哈姆雷特.txt","r").read()
    txt = txt.lower()
    for ch in '!@#$%^&*[]\{}\|?/><_+-=()~`':
        txt = txt.replace(ch," ")
    return txt

hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(11):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))