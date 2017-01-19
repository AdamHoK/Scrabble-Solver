
#TODO: Fix issue when there are two instances of the same letter, i.e. GRASS, or ADAM

from FunctionsFile import questionMark, sort

with open("dictionary.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

letters=input("\nEnter your letters here"
              "\n'?' for a blank tile"
              "\n Commas after word to indicate start and/or end letters"
              "\n Final input should look like this:"
              "\n <LETTERS> [,START LETTER] [,END LETTER]"
              "\n Include Start and/ or end letters in initial letters' input"
              "\n\n> ")

letters=letters.upper()
backup, letters=letters.split(), letters.split()[0]

letters=''.join(questionMark(letters))
print(letters)
#final(letters, letters)

words={}

for word in array:
    counter=[]
    '''This loop only has to make a dict with the word
    and the amount of correct chars in the word'''
    for letter in letters:
        if letter in word:
            counter.append(letter)

        while counter.count(letter)>word.count(letter):
            counter.pop(counter.index(letter))

        #if len(counter)==4 and len(word)-1==4:
        #    print(word, len(word), counter, len(counter))

        if counter!=0:
            words[word]=len(counter)

perfect=[]
results={}

sort(words, perfect, letters, results, backup)

linebreak=0

for output in sorted(perfect, key=len):#, reverse=True):
    linebreak+=1

    if linebreak%3!=0:
        print(output, end=" ")
    else:
        print(output,"\n")

print()
