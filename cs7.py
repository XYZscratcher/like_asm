#author:XYZscratcher
text=""
while not("END"in text):
    text+=input("")
    text+="\n"
def textReplace(text):
    functions=[["print","ECHO"],["input","INP"],["def","DEF"],["replace","RE"]]
    tokens=[["(","<"],[")",">"],[":","THEN"],["    ","00"],["=","DB"],["#",";"],["==","EQU"],["<","LSS"],[">","GTR"]]
    keywords=[["and","AND"],["or","OR"],["not","NOT"],["if","IF"],["elif","ELSEIF"],["else","ELSE"],["while","WHILE"]]
    replaceWords=functions+tokens+keywords
    i=0
    while i<len(replaceWords):
        text=text.replace(replaceWords[i][1],replaceWords[i][0])
        i+=1
    text=text.replace("END","")
    return text
print("="*10,end="")
print("运行结果",end="")
print("="*10)
exec(textReplace(text))
#print(textReplace(text))


