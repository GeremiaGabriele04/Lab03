import dictionary
import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dictionaries = []

    def addDict(self, lingua):
        if lingua == "Italiano":
            return self.dictionaries.loadDictionary("Italian.txt")

        if lingua == "Inglese":
            return self.dictionaries.loadDictionary("English.txt")

        if lingua == "Spagnolo":
            return self.dictionaries.loadDictionary("Spanish.txt")

    def printDic(self, language):
        dizionario_vuoto = []
        if language == "Italiano":
            dizionario_vuoto = self.addDict("Italiano")
            for parola in dizionario_vuoto:
                print(parola)
        if language == "Inglese":
            dizionario_vuoto = self.addDict("Inglese")
            for parola in dizionario_vuoto:
                print(parola)
        if language == "Spagnolo":
            dizionario_vuoto = self.addDict("Spagnolo")
            for parola in dizionario_vuoto:
                print(parola)

    def searchWord(self, words, language):
        pass
