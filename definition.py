from PyDictionary import PyDictionary
class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        dictironary = PyDictionary()
        return dictironary.meaning(self.term)
