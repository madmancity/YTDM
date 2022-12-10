import pandas as pd
from addsw import addsw
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
# This code is adjustable in the following ways:
# The amount of titles analyzed can be adjusted by changing the value of variable r
# The top5 can be changed to top 10 or any other range by changing the value of variable x
# Words can be removed from consideration by using s.add in the addsw file the same way "fastidiously" is added

# Create empty dictionary
words = {}
# Create custom tokenizer to separate words but remove punctuation
tokenizer = RegexpTokenizer(r'\w+')

# Check if word contains numbers
def wordornot(word):
    return word.isascii()


# Import nltk stopword set
stopwords = set(stopwords.words('english'))
# Add certain words to stopwords set
addsw(stopwords)
# Create filtered version of youtube title
def tokenize(title):
    # Tokenize the sentence
    wordtokens = tokenizer.tokenize(title)
    # Create array for filtered title
    filtered_title = []
    # For every word in the title
    for word in wordtokens:
        # Make all words lowercase for computational ease
        word = word.lower()
        # Find words that are not stopwords, are words, and are made up entirely of letters
        if word not in stopwords and wordornot(word) == True and word.isnumeric() == False:
            # Add them to filtered title array
            filtered_title.append(word)
    # Iterate through words in title
    for word in filtered_title:
        # If word already found in a title
        if duplicate(words, word):
            # Add 1 to the count of that word
            words[word] += 1
        # If word is new
        else:
            # Create new key value pair for title and its one appearance so far
            words[word] = 1
    # Return title for printing
    return filtered_title
# Check if word already exists
def duplicate(wordsdct, key):
    # If the word is already a key in the dictionary
    if key in wordsdct.keys():
        # Duplicate is true
        return True
    # If word is new to dictionary
    else:
        # Duplicate is false
        return False


# Read csv and add to dataframe, replace this with filepath of csv in users system
df = pd.read_csv("C:\\Users\\liamr\\Documents\\USvideos.csv");


# Print the amount of titles that are going to be analyzed, adjustable by changing value of r
r = 40949
for i in range(1, r):
    # Print tokenized title
    print(tokenize(df.loc[i]['title']))
# Find the average word count
avg = sum(words.values()) / len(words)
# Print average word count
print("Average word appearance count is: " + str(avg))
# Create dictionary for top 5 words with their appearance numbers
top5 = {}
# Adjust amount of words displayed by changing x's value to the desired number of entries to be displayed + 1
x = 16
for i in range(1, x):
    # Find the largest value in the dictionary
    maxvalue = max(words.values())
    # Find the key corresponding to the largest value in the dictionary
    maxkey = max(words, key=words.get)
    # Print rank of word, word, and amount of times that word appeared
    print("#" + str(i) + " Most common word is: " + maxkey + " with " + str(maxvalue) + " appearances")
    # Add that key to the top 5
    top5[maxkey] = maxvalue
    # Delete that key, value pair from the dictionary to allow the finding of the next highest value
    del words[maxkey]
# Add the words back to the words dictionary
words.update(top5)


