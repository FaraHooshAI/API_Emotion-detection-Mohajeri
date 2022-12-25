import hazm
import re

class Preprocessing:
    def __init__(self):
        pass

    def normalize(self, text):
        normalizer = hazm.Normalizer()
        return normalizer.normalize(text)

    def remove_emojis(self, text):
        pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           "]+", flags = re.UNICODE)
        
        return pattern.sub('', text)
    
    def remove_english_words(self, text):
        return  re.sub('\s*[A-Za-z]+\b', '' , text)

    def remove_hashtags(self, text):
        text = re.sub("#[A-Za-z0-9_]+","", text)
        text = re.sub("#[\u06F0-\u06F9\u0660-\u0669\u0621-\u0628\u062A-\u063A\u0641-\u0642\u0644-\u0648\u064E-\u0651\u0655\u067E\u0686\u0698\u06A9\u06AF\u06BE\u06CC_]+","", text)
        return text
    
    def remove_specific_character(self, text, char):
        return text.replace(char, '')

    def remove_mentions(self, text):
        return re.sub("@[A-Za-z0-9_]+","", text)

    def sentence_tokenize(self, text):
        tokenizer = hazm.SentenceTokenizer()
        return tokenizer.tokenize(text)

    def word_tokenize(self, sentence):
        tokenizer = hazm.WordTokenizer()
        return tokenizer.tokenize(sentence)

    def remove_stop_words(self, words):
        stop_words = hazm.stopwords_list()
        return list(filter(lambda x: x not in stop_words, words))

    def remove_character_duplications(self, word):
        return re.sub(r'(.)\1+', r'\1', word)
