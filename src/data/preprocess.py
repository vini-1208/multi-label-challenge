import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from textblob import TextBlob
import contractions

def removeContractions(x):
    """
    Convert contractions to elongated words.
     e.g. `you're` will be converted to `you are`
    """
    x = [contractions.fix(word) for word in x.split()]
    return " ".join(x)

def removePunctuation(sentence):
    '''removes punctuations'''
    sentence = re.sub(r'[?|!|\'|"|#]',r'',sentence)
    sentence = re.sub(r'[.|,|)|(|\|/]',r' ',sentence)
    sentence = sentence.strip()
    sentence = sentence.replace("\n"," ")
    return sentence

def removeNumbers(sentence):
    '''removes numbers'''
    alpha_sent = ""
    for word in sentence.split():
        alpha_word = re.sub('[^a-z A-Z]+', '', word)
        alpha_sent += alpha_word
        alpha_sent += " "
    alpha_sent = alpha_sent.strip()
    return alpha_sent

def word_counts(txt):
   '''check # of words post processing'''
   return len(re.findall('\w+', txt))

def removeStopWords(sentence):
    '''removes stopwords'''
    stop_words = stopwords.words('english')
    sentence = sentence.split()
    sentence = [word for word in sentence if word not in stop_words]
    sentence = " ".join(sentence)
    return sentence

def lemmatize(sentence):
    '''returns lemmatized text'''
    sent = TextBlob(sentence)
    tag_dict = {"J": 'a', "N": 'n', "V": 'v', "R": 'r'}
    words_tags = [(w, tag_dict.get(pos[0], 'n')) for w, pos in sent.tags]    
    lemma_list = [wd.lemmatize(tag) for wd, tag in words_tags]
    return " ".join(lemma_list)

def preprocess_data(df,col):
    '''Applies series of preprocessing functions and returns a clean text column '''
    preprocess_text = df[col].str.lower().values.tolist()
    preprocess_text = [removeContractions(text) for text in preprocess_text]
    preprocess_text = [removePunctuation(text) for text in preprocess_text]
    preprocess_text = [removeNumbers(text) for text in preprocess_text]
    preprocess_text = [removeStopWords(text) for text in preprocess_text]
    preprocess_text = [lemmatize(text) for text in preprocess_text]
    df['preprocessed_text'] = preprocess_text
    return df