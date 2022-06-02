#g=green letter is at the excect position
#y=yellow letter is in word but not at the position
#w= letter is not in the word


def green(index,letter,words):
    for word in words[:]:
        if(word[index]!=letter):
            words.remove(word)
    return words


def yellow(index,letter,words):
    for word in words[:]:
        part=word[0:index]+word[index+1:]
        if(word[index]==letter) or (letter not in part):
            words.remove(word)
    return words

def white(letter,words):
    for word in words[:]:
        if letter in word:
            words.remove(word)
    return words
def edge_case(letter,words,index,count):
    for word in words:
        part=word[0:index]+word[index+1:]
        if(word[index]==letter) or (letter not in part):
            words.remove(word)
        elif(word[0:index].count(letter)!=count or word.count(letter)!=count):
            words.remove(word)
