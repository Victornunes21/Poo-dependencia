class Eletrodomestico:
    def __init__(self,ligado,voltagem,consumo):
        self.ligado = ligado
        self.voltagem = voltagem
        self.consumo = consumo 

    def isLigado(self):
        return (self.ligado)

    def setLigado(self,ligado):
        self.ligado = ligado

geladeira = Eletrodomestico(True,220,800)
print("A geladeira esta ligada?", geladeira.isLigado())
