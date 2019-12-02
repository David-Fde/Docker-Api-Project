from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

def tokenization(text):
    tokens = nltk.word_tokenize(text)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    tokens_clean = [e for e in tokens if e not in stop_words]
    return tokens_clean