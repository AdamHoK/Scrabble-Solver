
#TODO: Fix issue when there are two instances of the same letter, i.e. GRASS, or ADAM

from FunctionsFile import questionMark, sort

with open("dictionary.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

letters=input("Enter your letters here"
              "\n'?' for a blank tile"
              "\n Commas after word to indicate start and/or end letters"
              "\n Final input should look like this:"
              "\n <LETTERS> [,START LETTER] [,END LETTER]"
              "\n Include Start and/ or end letters in initial letters' input"
              "\n> ")

backup, letters=letters.split(), letters.split()[0]

letters=''.join(questionMark(letters))
#final(letters, letters)

words={}

for word in array:
    counter=0
    for letter in letters:
        if letter in word:
            counter+=1
    words[word]=counter


perfect=[]
results={}

sort(words, perfect, letters, results, backup)

linebreak=0
for output in perfect:
    linebreak+=1
    if linebreak%3==0:
        print()
    else:
        print(output, end=" ")

#print(results)
