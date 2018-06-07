def Convert(string):
    li = list(string.split(" "))
    return li

def inputText(text):
    convert = ' '.join(Convert(text)[0:1])
    return convert

def inpu(text):
    return ' '.join(Convert(text)[1:])
