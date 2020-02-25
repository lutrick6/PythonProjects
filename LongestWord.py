# Finding longest word in list

ll = ['I', 'is', 'one', 'cool', 'kiddo', 'without', 'the', 'hype']
word = ''
for i in ll:
    if len(i) > len(word):
        word = i
print(word, len(word))

for i in ll: #Runs through the list ll above
    if len(i) >= len(word): #If i's length: len(i) is greater or equal to length of word
        words = [i, word] #Update words with all
print("there are {} words: {}".format(len(words), words))


