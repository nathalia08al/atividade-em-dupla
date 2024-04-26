class Carro:
    def __init__(self, marca, modelo,ano, cor ):
       self.marca= marca
       self.modelo= modelo
       self.ano= ano
       self.cor= cor
    def ligar(self):
     return f"{self.modelo} carro ligado"
    def desligar(self):
     return f"{self.modelo} carro desligado"
    def acelerar(self):
       return f"{self.modelo} acelerando o carro"
if __name__ =="__main__":
   carro1= Carro("fiat", "uno", 2000, "preto")
   carro2= Carro("fiat", "palio", 2000, "branco")
   print(carro1.ligar())
   print(carro1.acelerar())
   print(carro1.desligar())