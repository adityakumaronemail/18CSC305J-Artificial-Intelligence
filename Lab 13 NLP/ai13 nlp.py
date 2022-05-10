from nltk.tokenize import sent_tokenize, word_tokenize 
example_string = """ 
... Muad'Dib learned rapidly because his first training was in how to learn. 
... And the first lesson of all was the basic trust that he could learn. ... It's shocking to find how many people do not believe they can learn, ... and how many more believe learning to be difficult.""" sent_tokenize(example_string) 
word_tokenize(example_string) 
Filtering stop words: 
nltk.download("stopwords") 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
worf_quote = "Sir, I protest. I am not a merry man!" 
words_in_quote = word_tokenize(worf_quote) 
words_in_quote 
stop_words = set(stopwords.words("english")) 
filtered_list = []
for word in words_in_quote: 
if word.casefold() not in stop_words: 
filtered_list.append(word) 
filtered_list = [ 
word for word in words_in_quote if word.casefold() not in stop_words ] 
filtered_list 

Stemming: 
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
stemmer = PorterStemmer() 
string_for_stemming = """ 
The crew of the USS Discovery discovered many discoveries. Discovering is what explorers do.""" 
words = word_tokenize(string_for_stemming) 
words 
stemmed_words = [stemmer.stem(word) for word in words] 
stemmed_words 
Tagged parts of speech: 
from nltk.tokenize import word_tokenize 
sagan_quote = """ 
If you wish to make an apple pie from scratch, 
you must first invent the universe.""" 
words_in_sagan_quote = word_tokenize(sagan_quote) 
import nltk 
nltk.pos_tag(words_in_sagan_quote) 
jabberwocky_excerpt = """ 
... 'Twas brillig, and the slithy toves did gyre and gimble in the wabe: ... all mimsy were the borogoves, and the mome raths outgrabe.""" words_in_excerpt = word_tokenize(jabberwocky_excerpt) 
nltk.pos_tag(words_in_excerpt) 
Lemmatizing: 
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer() 
lemmatizer.lemmatize("scarves") 
string_for_lemmatizing = "The friends of DeSoto love scarves."
words = word_tokenize(string_for_lemmatizing) 
words 
lemmatized_words = [lemmatizer.lemmatize(word) for word in words] lemmatized_words 
lemmatizer.lemmatize("worst") 
lemmatizer.lemmatize("worst", pos="a") 
Chunking: 
from nltk.tokenize import word_tokenize 
lotr_quote = "It's a dangerous business, Frodo, going out your door." words_in_lotr_quote = word_tokenize(lotr_quote) 
words_in_lotr_quote 
nltk.download("averaged_perceptron_tagger") 
lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote) 
lotr_pos_tags 
grammar = "NP: {<DT>?<JJ>*<NN>}" 
chunk_parser = nltk.RegexpParser(grammar) 
tree = chunk_parser.parse(lotr_pos_tags)
