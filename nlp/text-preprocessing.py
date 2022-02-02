#import text
file = r"C:/Users/10inm/Desktop/CodeAcademy/Practice/nlp_wiki.txt"
with open(file, 'r') as f:
    nlp_text = f.read()
    f.close()
    
#print(nlp_text)

"""
NOISE REMOVAL
"""
import re

# remove punctuation     
nlp_no_punc = re.sub(r'[\!\.\,\"\'\?\(\)]', '', nlp_text)
# print text
#print(nlp_no_punc)
# remove whitespace
nlp_white = re.sub(r'\s{2,9}', '', nlp_no_punc)
# print text
#print(nlp_white)

"""
TOKENIZATION
"""
from nltk.tokenize import word_tokenize

# tokenize the text
nlp_tokenized = word_tokenize(nlp_white)
#print(nlp_tokenized)

"""
NORMALIZATION
"""
# lower case words
nlp_tokenized_lower = [token.lower() for token in nlp_tokenized]
#print(nlp_tokenized_lower)

# remove stopwords
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
nlp_nostop = [token for token in nlp_tokenized_lower if token not in stop_words]
#print(nlp_nostop)

# POS tagging
from nltk import pos_tag
nlp_tagged = pos_tag(nlp_nostop)
#print(nlp_tagged)

# lemmatization
from nltk.stem import WordNetLemmatizer

# instantiate lemmatizer
lemmatizer = WordNetLemmatizer()

# lemmatize text
nlp_lem = [lemmatizer.lemmatize(token) for token in nlp_nostop]
print("Original Text")
print(nlp_nostop)
print("Lemmatized text")
print(nlp_lem)