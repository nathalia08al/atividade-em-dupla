class Animal:
  def __init__(self, nome, idade, espécie ):
       self.nome= nome
       self.idade= idade
       self.espécie= espécie
  def barulho(self):
    return f"{self.nome} emitiu barulho"
if __name__ == "__main__":
    animal1= Animal("alex", 10,"leão" )
    print("graaah")
    print(animal1.nome, animal1.idade, animal1.espécie)
    print(animal1.barulho())