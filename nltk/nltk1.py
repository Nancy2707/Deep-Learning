from nltk.tokenize import word_tokenize,sent_tokenize
# from nltk.tokenize import word_tokenize
data="""Natural language processing (NLP) is a machine learning technology that gives computers the ability to interpret, manipulate, and comprehend human-language.Natural language processing (NLP) is a machine learning technology that gives computers the ability to interpret.Manipulate, and comprehend human language.Natural language processing (NLP) is a machine learning technology.That gives computers the ability to interpret, manipulate, and comprehend human language."""
# print(nlp)
# print(w)
# w=word_tokenize(data)
# import nltk
# e=nltk.download("averaged_perceptron_tagger")
# # print(e)
# from nltk import pos_tag
# pos=pos_tag(data)
# print(pos)
import nltk
# percept=nltk.download("averaged_perceptron_tagger")
# punket=nltk.download('punkt')
# w=word_tokenize(data)
# print(w)
# print("\n\n")
# from nltk import pos_tag
# pos=pos_tag(w)
# print(pos)
# print("\n\n")
# sent=sent_tokenize(data)
# print(sent)
# for i in sent:
#     print("\n")
#     print(i)
from nltk.stem import LancasterStemmer,RegexpStemmer,PorterStemmer,SnowballStemmer
lan=LancasterStemmer()
regex=RegexpStemmer('ing')
porter=PorterStemmer()
snow=SnowballStemmer('english')
# l=lan.stem("mouse")
l=regex.stem("mouse")
# l=porter.stem("mice")
# l=snow.stem("mouse")
print(l)
from nltk.stem import WordNetLemmatizer
wordnet=nltk.download('wordnet')
print(wordnet)
wordLem=WordNetLemmatizer()
lem=wordLem.lemmatize('mice')
print('mice::',lem)