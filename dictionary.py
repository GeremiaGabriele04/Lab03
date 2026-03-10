class Dictionary:
    def __init__(self, language: str):
        self.language = language
        self._parole = []

    def loadDictionary(self, path:str):
        with open(path, "r", encoding="utf-8") as file:
            for riga in file:
                riga = riga.strip()
                self._parole.append(riga)
        return self._parole


    def printAll(self):
        for parola in self._parole:
            print(parola)

    @property
    def dict(self):
        return self._parole
