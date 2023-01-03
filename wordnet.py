try:
    import nltk
except ImportError:
    print('NLKT not found. Downloading WordNet corpus...')
    import nltk
    nltk.download('wordnet')

from nltk.corpus import wordnet
import random


# Set the number of outputs to generate
num_outputs = 200

# Create a list of words that start with the required letters
words = [word for word in wordnet.words() if word[0].lower() in ['s', 'h', 'a', 'i']]

# Set the symbol substitutions
substitutions = {
    's': ['5', '$'],
    'h': ['#'],
    'a': ['@'],
    'i': ['!'],
    'e': ['3']
}

# Open a text file for writing
with open('output.txt', 'w') as file:
# Loop through the specified number of outputs
    for i in range(num_outputs):
        # Choose a random word from each list
        word1 = random.choice(words)
        word2 = random.choice(words)
        word3 = random.choice(words)
        word4 = random.choice(words)
        
        # Substitute the letters with symbols
        for letter, symbol_options in substitutions.items():
            symbol = random.choice(symbol_options)
            word1 = word1.replace(letter, symbol)
            word2 = word2.replace(letter, symbol)
            word3 = word3.replace(letter, symbol)
            word4 = word4.replace(letter, symbol)
        
        # Combine the words using CamelCase
        compound_word = '_'.join([word1, word2, word3, word4]).title()

        
        # Print the compound word
        print(compound_word)

        # Write the compound word to the file
        file.write(compound_word + '\n')