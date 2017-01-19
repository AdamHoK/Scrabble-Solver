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
    print(l)
    for letter in l:
        print(letter)
        if letter=='?':
            amount+=1
    while l.count("?")!=0:
        l.pop(l.index(letter))
    return l


def sort(x, perfect, letters, results, backup):
    sorted_x = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
    for i in sorted_x:

        wordFixed=i[0]
        correctLength=i[1]
        wordFixed = wordFixed[:-1]
        if len(wordFixed)>2:

            '''If the length of the word is equal to or smaller than
            the length of the input + the amount of blank tiles'''

            if amount>0:
                if checker(letters, wordFixed) and len(wordFixed)<=(len(letters)+amount) and \
                    \
                    wordFixed[0]==final(backup, wordFixed)[0] and \
                    wordFixed[len(wordFixed)-1]==final(backup, wordFixed)[1]:

                    perfect.append(wordFixed)  #If all the letters are in the word,
                    results[wordFixed] = i[1] #but there are other letters as well

            elif amount==0:

                '''If the length of the word is the same
                as the amount of correct characters in the word
                And if start and end match up'''

                if len(wordFixed)==(correctLength + final(backup, wordFixed)[2]) and \
                    \
                    wordFixed[0]==final(backup, wordFixed)[0] and \
                    wordFixed[len(wordFixed) - 1]==final(backup, wordFixed)[1]:
                    perfect.append(wordFixed)
                    results[wordFixed]=i[1] #Appends the word and it's char length to a dict.

    #return sorted_x


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
