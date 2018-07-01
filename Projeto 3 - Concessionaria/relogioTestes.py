from time import clock
class Relogio:
    'Classe simples usada para cronometrar as operações'    
    def __init__(self):
        self.tempo = clock()
    def getTempo(self):
        return str(clock() - self.tempo)
