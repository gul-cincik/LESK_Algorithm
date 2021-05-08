import codecs
from Tools.scripts.treesync import raw_input
from nltk.tokenize import word_tokenize
from  nltk.corpus import stopwords, wordnet
from  nltk.stem import WordNetLemmatizer, PorterStemmer

#The filter function takes the given query/sentence as an input and returns list of tokens which are lemmatized
def filter(sentence):
    filtered_sentence = []
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("turkish"))
    words = word_tokenize(sentence)

    for w in words:
        if w not in stop_words:
            filtered_sentence.append(lemmatizer.lemmatize(w))

    return filtered_sentence

def similarity_check(word1, word2):
    word1 = word1 + ".n.01"
    word2 = word2 + ".n.01"
    try:
        w1 = wordnet.synset(word1)
        w2 = wordnet.synet(word2)
        return w1.wup_similarity(w2)
    except:
        return 0

def synonyms_creator(word):
    synonyms = []

    for syn in wordnet.synsets(word):
        for i in syn.lemmas():
            synonyms.append(i.name())

    return synonyms

def filter_sentence(sentence):
    filtered_sentence = []
    lemmatizer = WordNetLemmatizer()
    ps = PorterStemmer()

    stop_words = set(stopwords.words("turkish"))
    words = word_tokenize(sentence)

    for w in words:
        if w not in stop_words:
            filtered_sentence.append(lemmatizer.lemmatize(ps.stem(w)))
            for i in synonyms_creator(w):
                filtered_sentence.append(i)

    return filtered_sentence


if __name__ == '__main__':
    cricfile = codecs.open("Plant_gül.txt", 'r', "utf-8")
    sent1 = cricfile.read().lower()
    vampirefile = codecs.open("Verb_gül.txt", 'r', 'utf-8')
    sent2 = vampirefile.read().lower()
    sent3 = "start"

    while(sent3 != "end"):
        sent3 = raw_input("Enter query: ").lower()

        filtered_sent1 = []
        filtered_sent2 = []
        filtered_sent3 = []

        counter1 = 0
        counter2 = 0
        sent31_similarity = 0
        sent32_similarity = 0
        filtered_sent1 = filter(sent1)
        filtered_sent2 = filter(sent2)
        filtered_sent3 = filter(sent3)

        for i in filtered_sent3:
            for j in filtered_sent1:
                counter1 += 1
                sent31_similarity = sent31_similarity + similarity_check(i, j)

            for j in filtered_sent2:
                counter2 += 1
                sent32_similarity = sent32_similarity + similarity_check(i, j)

        filtered_sent1 = []
        filtered_sent2 = []
        filtered_sent3 = []

        filtered_sent1 = filter_sentence(sent1)
        filtered_sent2 = filter(sent2)
        filtered_sent3 = filter(sent3)

        sent1_count = 0
        sent2_count = 0

        for i in filtered_sent3:
            for j in filtered_sent1:
                if(i == j):
                    sent1_count = sent1_count + 1
            for j in filtered_sent2:
                if(i == j):
                    sent2_count = sent2_count + 1

        if((sent1_count + sent31_similarity) > (sent2_count + sent32_similarity)):
            print("Plant")
        else:
            print("nesne almayan eylem:  hoşuna ya da tuhafına giden olaylar, durumlar, sözler vb. karşısında, yüzün kasılmasının yanı sıra, genellikle kesik kesik, değişik oranda sesli bir biçimde neşe duygusunu açığa vurmak.")
