"""Task 6. A very simple example should be prepared
to show how to do word sense disambiguation using
the LESK algorithm on a Turkish corpus.
Here, the student can be flexible about corpus and glossary,
in other words, a corpus with a few sentences and a dictionary with a few definitions can be prepared."""
class Synset():
    def init(self,name,definition):
        self._name=name
        if isinstance (definition,str):
            self._definition=definition
        else:
            self._list=definition
    def repr(self):
        return "%s: '%s' " % (self._name, self._definition)
    def name(self):
        return self._name
    def list(self):
        return self._list
    def definition(self):
        return self._definition
    def get(self, str):
        for set in self._list:
            if set.name() == str:
                return set.list()
from transformers import AutoTokenizer
tokenizer=AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-cased")
Pas1=Synset("Pas1","Hava,nem,su ya da sulu çözeltilerin etkisiyle demir ve alaşımlarının yüzeyinde oluşan, hidroksit ve karbonatları da içeren kırmızı-kahverenkli demir oksit")
Pas2=Synset("Pas2"," Bazı asalak mantarların çeşitli bitkilerde oluşturduğu portakal sarısı veya kahverengi lekeler")
Pas3=Synset("Pas3","Bazı top oyunlarında oyunculardan birinin topu takım arkadaşına geçirmesi")




pas=Synset("pas",[Pas1,Pas2,Pas3])

_synsets=Synset("_synsets",[pas])
def lesk(context_sentence,ambiguous_word,synsets=None):
    context=set(context_sentence)

    if synsets is None:
        synsets=_synsets.get(ambiguous_word)

    if not synsets:
        return None
    sense=max(
    (len(context.intersection(ss.definition().split())),ss)for ss in synsets
    )
    return sense
text="Demirin tozu ve pası dev işçilerin kirpiklerine yağar, gözlerine dolardı"
context=tokenizer.tokenize(text)
result=lesk(text,"pas")
print(result)