from time import clock
class Relogio:
    'Classe simples usada para cronometrar as operações'    
    def __init__(self):
        self.tempo = clock()
    def __del__(self):
        print("Tempo de Operação:", str(clock() - self.tempo))
