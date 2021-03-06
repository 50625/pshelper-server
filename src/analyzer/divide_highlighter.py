# from koalanlp.Util import initialize, finalize
# from koalanlp.proc import SentenceSplitter, Tagger
# from koalanlp import API
from konlpy.tag import Kkma


# initialize(OKT='LATEST')  #: HNN=2.0.3
# splitter = SentenceSplitter(API.OKT)
# tagger = Tagger(API.EUNJEON)

kkma = Kkma()

class DivideHighlighter:
    @staticmethod
    def getPosBySentence(sentence):
        posses = kkma.pos(sentence)
        pos_dict = {}
        sentence_formatted = sentence
        for pos in posses:
            if pos[1] == 'MAC':
                pos_dict[pos[0]] = pos[1]
        for key in pos_dict:
            sentence_formatted = sentence_formatted.replace(key, "<strong>"+key+"</strong>")
        print(sentence_formatted)
        return sentence_formatted

    @staticmethod
    def getDevidedContent(content):
        sentences = kkma.sentences(content)
        sentence_list = []
        print("===== Sentence =====")
        for sentence in sentences:
            print(sentence)
            sentence_list.append(DivideHighlighter.getPosBySentence(sentence))
        return sentence_list