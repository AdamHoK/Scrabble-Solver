import operator

def checker(letters, word):
    for letter in letters:
        if letter not in word: #If the letter is not in the word i.e. 'A' is not in 'TIGER'
            return False
    return True

def questionMark(input):
    global l
    global amount
    amount=0
    l=list(input)
    for letter in l:
        if letter=='?':
            amount+=1
            l.pop(l.index(letter))
    return l


def sort(x, perfect, letters, results, backup):
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))
    for i in sorted_x:
        wordFixed=i[0]
        wordFixed=wordFixed[:-1]

        if amount>0:
            if checker(letters, wordFixed) and len(wordFixed)<=(len(letters)+amount) and \
                            wordFixed[0]==final(backup, wordFixed)[0] and \
                            wordFixed[len(wordFixed)-1]==final(backup, wordFixed)[1]:

                perfect.append(wordFixed)  #If all the letters are in the word,
                results[wordFixed] = i[1] #but there are other letters as well

        elif amount==0:

            '''If the length of the word is the same
            as the amount of correct characters in the word
            And if start and end match up'''

            if len(wordFixed)==i[1] + final(backup, wordFixed)[2] and len(wordFixed) > 1 and \
                           \
                            wordFixed[0]==final(backup, wordFixed)[0] and \
                            wordFixed[len(wordFixed) - 1]==final(backup, wordFixed)[1]:

                perfect.append(wordFixed)
                results[wordFixed]=i[1] #Appends the word and it's char length to a dict.

    return sorted_x


def final(inputWord, w):
    if len(inputWord)>=2:
        start=inputWord[1]
        start=start[:-1] #To get rid of the comma
        x=1
    else:
        start=w[0]
        x=0
    if len(inputWord)==3:
        end=inputWord[2]
        x+=1
    else:
        end=w[len(w)-1]

    return start, end, x
