from nltk import word_tokenize

# Define disposable words and remove them from futher processing
def load_stop_words(fileName):
    with open(fileName,"r", encoding = "utf-8") as stop_words_file:
        return stop_words_file.read().lower().splitlines()

def remove_stop_words(vocabulary, stop_words):
    ''' The function takes in a list of words (vocabulary) and a list of stop words and returns a new vocabulary, where all the stop words have been removed. '''
    return [word for word in vocabulary if word not in stop_words]
