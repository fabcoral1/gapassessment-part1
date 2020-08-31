# Function will return the largest word and the largest word reversed based on array argument 'content'.
def largestwordandreverse(content):
    # Condition to check if file is empty or if it only has spaces.
    if len(content) == 0 or (len(content) == 1 and content[0].rstrip() == ''):
        largestword = "Largest word was not obtained since file is empty."
        largestwordreverse = "Largest word reversed was not obtained since file is empty."
    else:
        largestcnt = 0
        largestidx = 0
        # Iteration over array 'content' to obtain the length of the largest word and its index.
        for idx, word in enumerate(content):
            if len(word.rstrip()) > largestcnt:
                largestcnt = len(word.rstrip())
                largestidx = idx
        largestword = str(content[largestidx]).rstrip()
        largestwordreverse = largestword[::-1]
    return largestword, largestwordreverse


# Set filename with the name of the file containing the list of words.
filename = 'file.txt'
file = open(filename, 'r')
content = file.readlines()
# Prints largest word and largest word reversed.
print('\n'.join(map(str, largestwordandreverse(content))))